import numpy as np
import matplotlib.pyplot as plt
#======input=========#
'''
z_start=float(input("z_start"))
z_end=float(input("z_end"))
z_step=float(input("z_step"))
r_start=float(input("r_start"))
r_end=float(input("r_end"))
r_step=float(input("r_step"))
'''

p_start=float(input("p_start "))
p_end=float(input("p_end "))
p_step=float(input("p_step "))
p_name=input("p_name ")

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
#chi2_EE=np.zeros((len(np.arange(z_start,z_end,z_step)),len(np.arange(r_start,r_end,r_step))))
chi2_EE=np.zeros((1,len(np.arange(p_start,p_end,p_step))))
#chi2_BB=np.zeros((1,len(np.arange(p_start,p_end,p_step))))

#====Array=======#
#noise ps
spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#Cl_fid
data_fid=np.loadtxt('output/reio_mine00_cl_lensed.dat')
EE_fid=data_fid[0:2000,1]
#BB_fid=data_fid[0:2000,2]
#errors_EE=error(EE_fid,spectrum)
errors_EE=error(EE_fid,spectrum)
for i in range(len(np.arange(p_start,p_end,p_step))):
    if (i%100)<10:
        data=np.loadtxt('output/'+p_name+'1_0_'+str(int(i/100))+'_0'+str(i%100)+'_cl.dat')
    else:
        data=np.loadtxt('output/'+p_name+'1_0_'+str(int(i/100))+'_'+str(i%100)+'_cl.dat')
    EEs=data[0:2000,1]
    #BBs=data[0:2000,2]
    #errors_EE=error(EEs,spectrum)
    #chi2_EE[j,i]=chi2(EE_fid,EEs,errors_EE)
    #errors_BB=error(BBs,spectrum)
    chi2_EE[0,i]=chi2(EE_fid,EEs,errors_EE)

#np.save("chi21_EE.npy",chi2_EE)
max_chi=np.max(chi2_EE[0])
min_i=0
min_chi=0
for i in range(len(chi2_EE[0])):
    chi2_EE[0,i]-=max_chi
    if chi2_EE[0,i]<min_chi:
        min_chi=chi2_EE[0,i]
        min_i=i
np.save("chi21_EE_"+p_name+".npy",chi2_EE)
print(min_i)
print(np.arange(p_start,p_end,p_step)[min_i])

