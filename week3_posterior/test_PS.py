import numpy as np
import matplotlib.pyplot as plt

#=========input=============#
z_start=7.6711
z_end=7.6712
z_step=100
r_start=0.01
r_end=0.26
r_step=0.01

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========functions==============#
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(2000)
    for i in np.arange(2,2002,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#=========noise ps============#
spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#=========draw ps============#
j=-1
for z_reio in np.arange(z_start,z_end,z_step):
    j+=1
    for i in range(len(np.arange(r_start,r_end,r_step))):
        if i<10:
            data=np.loadtxt('output/chi_'+str(j)+'_0'+str(i)+'_cl.dat')
        else:
            data=np.loadtxt('output/chi_'+str(j)+'_'+str(i)+'_cl.dat')
        BBs=data[0:2000,4]
        errors_BB=error(BBs,spectrum)
        plt.loglog(np.arange(2,2002,1),BBs[0:2000])
        plt.errorbar(np.arange(2,2002,1),BBs[0:2000],yerr=errors_BB)

data=np.loadtxt('output/reio_camb04_cl.dat')
BBs=data[0:2000,4]
errors_BB=error(BBs,spectrum)
plt.loglog(np.arange(2,2002,1),BBs[0:2000])
plt.errorbar(np.arange(2,2002,1),BBs[0:2000],yerr=errors_BB)
plt.show()
