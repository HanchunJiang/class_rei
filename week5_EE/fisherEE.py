import numpy as np

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========input==============#
#data_fid=np.loadtxt('output/reio_camb04_cl.dat')
#data_p=np.loadtxt('output/reio_camb05_cl.dat')
#data_m=np.loadtxt('output/reio_camb06_cl.dat')
#data1=np.loadtxt('output/reio_camb07_cl.dat')
data_lp=np.loadtxt('reio_camb01_cl.dat')
data_lm=np.loadtxt('reio_camb02_cl.dat')
data_lfid=np.loadtxt('reio_camb00_cl.dat')

BB_lp=data_lp[0:2000,2]
BB_lm=data_lm[0:2000,2]
BB_lfid=data_lfid[0:2000,2]

EE_lp=data_lp[0:2000,1]
EE_lm=data_lm[0:2000,1]
EE_lfid=data_lfid[0:2000,1]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F=0
for i in range(2000):
    #if (BB_fid[i]+spectrum[i])!=0:
    C=np.array([[BB_lfid[i]+spectrum[i],0],[0,EE_lfid[i]+spectrum[i]]])
    C_prime=(np.array([[BB_lp[i],0],[0,EE_lp[i]]])-np.array([[BB_lm[i],0],[0,EE_lm[i]]]))/2/0.00005

    matrix=np.linalg.inv(C)*C_prime*np.linalg.inv(C)*C_prime
    #print(matrix)
    F+=(2*(i+2)+1)/2*f_sky*matrix.trace()
    #F+=(2*(i+2)+1)/2*f_sky*1/(BB_fid[i]+spectrum[i])**2*(BB1[i]+spectrum[i])**2
    #F+=(2*(i+2)+1)/2*f_sky*1/(BB_lfid[i]+spectrum[i])**2*(BB_l1[i]+spectrum[i])**2

print(np.sqrt(1/F))
