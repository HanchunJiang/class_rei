import numpy as np

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========input==============#
data_lfid=np.loadtxt('reio_camb00_cl_lensed.dat')
data_l1p=np.loadtxt('reio_camb01_cl_lensed.dat')
data_l1m=np.loadtxt('reio_camb02_cl_lensed.dat')
data_l2p=np.loadtxt('reio_camb03_cl_lensed.dat')
data_l2m=np.loadtxt('reio_camb04_cl_lensed.dat')

delta_1=0.000005
delta_2=0.0001

p1_value=0.001
p2_value=0.0561

p1_name="r"
p2_name="tau"

#========function==============#
def Fisher(EE_fid,BB_fid,NN,EE_ip,EE_im,BB_ip,BB_im,EE_jp,EE_jm,BB_jp,BB_jm,delta_i,delta_j):
    sum=0
    for i in range(len(EE_fid)):
        C=np.array([[BB_lfid[i]+spectrum[i],0],[0,EE_lfid[i]+spectrum[i]]])
        C_prime_i=(np.array([[BB_ip[i],0],[0,EE_ip[i]]])-np.array([[BB_im[i],0],[0,EE_im[i]]]))/2/delta_i
        C_prime_j=(np.array([[BB_jp[i],0],[0,EE_jp[i]]])-np.array([[BB_jm[i],0],[0,EE_jm[i]]]))/2/delta_j
        matrix=np.linalg.inv(C)*C_prime_i*np.linalg.inv(C)*C_prime_j
        sum+=(2*(i+2)+1)/2*f_sky*matrix.trace()
    return sum

BB_lfid=data_lfid[0:2000,2]
BB_l1p=data_l1p[0:2000,2]
BB_l1m=data_l1m[0:2000,2]
BB_l2p=data_l2p[0:2000,2]
BB_l2m=data_l2m[0:2000,2]

EE_lfid=data_lfid[0:2000,1]
EE_l1p=data_l1p[0:2000,1]
EE_l1m=data_l1m[0:2000,1]
EE_l2p=data_l2p[0:2000,1]
EE_l2m=data_l2m[0:2000,1]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#Fisher(EE_fid,BB_fid,NN,EE_ip,EE_im,BB_ip,BB_im,EE_jp,EE_jm,BB_jp,BB_jm,delta_i,delta_j)
F_11=1.5*Fisher(EE_lfid,BB_lfid,spectrum,EE_l1p,EE_l1m,BB_l1p,BB_l1m,EE_l1p,EE_l1m,BB_l1p,BB_l1m,delta_1,delta_1)
F_22=1.5*Fisher(EE_lfid,BB_lfid,spectrum,EE_l2p,EE_l2m,BB_l2p,BB_l2m,EE_l2p,EE_l2m,BB_l2p,BB_l2m,delta_2,delta_2)
F_12=1.5*Fisher(EE_lfid,BB_lfid,spectrum,EE_l1p,EE_l1m,BB_l1p,BB_l1m,EE_l2p,EE_l1m,BB_l2p,BB_l2m,delta_1,delta_2)

print(1/np.sqrt(F_11))
print(1/np.sqrt(F_22))
