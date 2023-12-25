import numpy as np

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1
sigma_tau_planck=0.0071

#=========input==============#
data_lfid=np.loadtxt('reio_camb00_cl.dat')
data_l1p=np.loadtxt('reio_camb01_cl.dat')
data_l1m=np.loadtxt('reio_camb02_cl.dat')
data_l2p=np.loadtxt('reio_camb03_cl.dat')
data_l2m=np.loadtxt('reio_camb04_cl.dat')

delta_1=0.00005
delta_2=0.00001

#========function==============#
def Fisher(fid,NN,ip,im,jp,jm,delta_i,delta_j):
    sum=0
    for k in range(len(fid)):
        sum+=(2*(k+2)+1)/2*f_sky/(fid[k]+NN[k])**2*(ip[k]-im[k])/2/delta_i*(jp[k]-jm[k])/2/delta_j
    return sum

BB_lfid=data_lfid[0:2000,2]
BB_l1p=data_l1p[0:2000,2]
BB_l1m=data_l1m[0:2000,2]
BB_l2p=data_l2p[0:2000,2]
BB_l2m=data_l2m[0:2000,2]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F_11=1.5*Fisher(BB_lfid,spectrum,BB_l1p,BB_l1m,BB_l1p,BB_l1m,delta_1,delta_1)
F_22=1.5*(Fisher(BB_lfid,spectrum,BB_l2p,BB_l2m,BB_l2p,BB_l2m,delta_2,delta_2)+1/sigma_tau_planck**2)
F_12=Fisher(BB_lfid,spectrum,BB_l1p,BB_l1m,BB_l2p,BB_l2m,delta_1,delta_2)

print(np.sqrt(1/F_11))
print(np.sqrt(1/F_22))
print(np.sqrt(F_11*F_22)/F_12)