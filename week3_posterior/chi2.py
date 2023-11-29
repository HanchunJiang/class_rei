import numpy as np
import matplotlib.pyplot as plt
#======input=========#
z_start=float(input("z_start"))
z_end=float(input("z_end"))
z_step=float(input("z_step"))
r_start=float(input("r_start"))
r_end=float(input("r_end"))
r_step=float(input("r_step"))


#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=======functions=========#

#errors (sigma)
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(2000)
    for i in np.arange(2,2002,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#chi2
def chi2(Cl_fid,Cl,sigma):
    '''
    Cl_fid: ground truth
    Cl: PS we want to calculate chi2
    sigma: error
    '''
    sum=0
    for i in range(min(len(Cl),len(sigma))):
        sum+=(Cl_fid[i]-Cl[i])**2/sigma[i]**2
        #print(sum)
    print(sum)
    return sum

#========result========#
chi2_EE=np.zeros((len(np.arange(z_start,z_end,z_step)),len(np.arange(r_start,r_end,r_step))))
chi2_BB=np.zeros((len(np.arange(z_start,z_end,z_step)),len(np.arange(r_start,r_end,r_step))))

#====Array=======#
#noise ps
spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#Cl_fid
data_fid=np.loadtxt('output/reio_camb04_cl.dat')
EE_fid=data_fid[0:2000,2]
BB_fid=data_fid[0:2000,4]

j=-1
for z_reio in np.arange(z_start,z_end,z_step):
    j+=1
    for i in range(len(np.arange(r_start,r_end,r_step))):
        if i<10:
            data=np.loadtxt('output/chi_'+str(j)+'_0'+str(i)+'_cl.dat')
        else:
            data=np.loadtxt('output/chi_'+str(j)+'_'+str(i)+'_cl.dat')
        EEs=data[0:2000,2]
        BBs=data[0:2000,4]
        errors_EE=error(EEs,spectrum)
        chi2_EE[j,i]=chi2(EE_fid,EEs,errors_EE)
        errors_BB=error(BBs,spectrum)
        chi2_BB[j,i]=chi2(BB_fid,BBs,errors_BB)

np.save("chi2_EE.npy",chi2_EE)
np.save("chi2_BB.npy",chi2_BB)

