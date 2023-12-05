import numpy as np

#=========parameters=========#
f_sky=1

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

F=0
for i in range(2000):
    if BB_fid[i]!=0:
        #F+=(2*(i+2))/2*f_sky*((BB_p[i]-BB_m[i])/0.02/BB_fid[i])**2
        #F+=(2*(i+2))/2*f_sky*1/BB_fid[i]**2*BB1[i]**2
        F+=(2*(i+2))/2*f_sky*1/BB_lfid[i]**2*BB_l1[i]**2

print(np.sqrt(1/F))