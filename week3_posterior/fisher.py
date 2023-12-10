import numpy as np

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========input==============#
data_lfid=np.loadtxt('output/reio_camb09_cl.dat')
data_lrp
data_lrm
data_lzp
data_lzm

delta_z
delta_r

#========function==============#
def Fisher(fid,NN,ip,im,jp,jm,delta_i,delta_j):
    sum=0
    for k in range(len(fid)):
        sum+=(2*(i+2)+1)/2*f_sky/(fid[k]+NN[k])**2*(ip[k]-im[k])/2/delta_i*(jp[k]-jm[k])/2/delta_j
    return sum

BB_lfid=data_lfid[0:2000,4]
BB_lrp=data_lrp[0:2000,4]
BB_lrm=data_lrm[0:2000,4]
BB_lzp=data_lzp[0:2000,4]
BB_lzm=data_lzm[0:2000,4]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F_rr=Fisher(BB_lfid,spectrum,BB_lrp,BB_lrm,BB_lrp,BB_lrm,delta_r,delta_r)
F_zz=Fisher(BB_lfid,spectrum,BB_lzp,BB_lzm,BB_lzp,BB_lzm,delta_z,delta_z)
F_rz=Fisher(BB_lfid,spectrum,BB_lrp,BB_lrm,BB_lzp,BB_lzm,delta_r,delta_z)

print(1/np.sqrt(F_rr))
print(1/np.sqrt(F_zz))
print(np.sqrt(F_rr*F_zz)/F_rz)