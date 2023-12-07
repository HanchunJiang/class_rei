import numpy as np

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=========input==============#
data_fid=np.loadtxt('output/reio_camb04_cl.dat')
data_p=np.loadtxt('output/reio_camb05_cl.dat')
data_m=np.loadtxt('output/reio_camb06_cl.dat')
data1=np.loadtxt('output/reio_camb07_cl.dat')
data_l1=np.loadtxt('output/reio_camb08_cl.dat')
data_lfid=np.loadtxt('output/reio_camb09_cl.dat')

BB_fid=data_fid[0:2000,4]
BB_p=data_p[0:2000,4]
BB_m=data_m[0:2000,4]
BB1=data1[0:2000,4]
BB_l1=data_l1[0:2000,4]
BB_lfid=data_lfid[0:2000,4]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F=0
for i in range(2000):
    #if (BB_fid[i]+spectrum[i])!=0:
    #F+=(2*(i+2))/2*f_sky*((BB_p[i]-BB_m[i])/0.02/(BB_fid[i]+spectrum[i]))**2
    #F+=(2*(i+2))/2*f_sky*1/(BB_fid[i]+spectrum[i])**2*(BB1[i]+spectrum[i])**2
    F+=(2*(i+2))/2*f_sky*1/(BB_lfid[i]+spectrum[i])**2*(BB_l1[i]+spectrum[i])**2

print(np.sqrt(1/F))