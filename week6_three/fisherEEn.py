import numpy as np
import sys

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========input==============#
data_lfid=np.loadtxt('reio_camb00_cl_lensed.dat')

data_lp=[np.loadtxt('reio_camb01_cl_lensed.dat'),np.loadtxt('reio_camb03_cl_lensed.dat'),np.loadtxt('reio_camb05_cl_lensed.dat')]
data_lm=[np.loadtxt('reio_camb02_cl_lensed.dat'),np.loadtxt('reio_camb04_cl_lensed.dat'),np.loadtxt('reio_camb06_cl_lensed.dat')]

try:
    p_value=[float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]
    delta=[float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])]
except Exception as e:
    print("Input Error:", e)

p_name=["r","tau","width"]

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
EE_lfid=data_lfid[0:2000,1]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F_ii=[]
for i in range(len(delta)):
    EE_lp=data_lp[i][0:2000,1]
    EE_lm=data_lm[i][0:2000,1]
    BB_lp=data_lp[i][0:2000,2]
    BB_lm=data_lm[i][0:2000,2]
    F_ii.append(1/np.sqrt(1.5*Fisher(EE_lfid,BB_lfid,spectrum,EE_lp,EE_lm,BB_lp,BB_lm,EE_lp,EE_lm,BB_lp,BB_lm,delta[i],delta[i])))

for i in range(len(F_ii)):
    print(F_ii[i])
