import numpy as np
import matplotlib.pyplot as plt
f_sky=1
delta_l=1
NNs=np.load("spectrum.npy")

#files=['/Users/hanchunjiang/class_public-3.2.0/output/reio_camb02_cl.dat']
files=['/Users/hanchunjiang/class_public-3.2.0/output/reio_camb03_cl_lensed.dat']
data=[]
for data_file in files:
    data.append(np.loadtxt(data_file))

curve=data[0]
TTs=curve[0:1999,1]
EEs=curve[0:1999,2]
TEs=curve[0:1999,3]
BBs=curve[0:1999,4]

errors=np.zeros(1999)

#对于TT EE BB

for i in np.arange(2,2001,1):
    errors[i-2]=((BBs[i-2]+NNs[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
'''
#对于TE
for i in np.arange(2,2001,1):
    errors[i-2]=np.sqrt((TEs[i-2]**2+(TTs[i-2]+NNs[i-2])*(EEs[i-2]+NNs[i-2]))/((2*i+1)*f_sky*delta_l))
'''

plt.loglog(np.arange(2,2001,1),BBs[0:1999])
plt.errorbar(np.arange(2,2001,1),BBs[0:1999],yerr=errors)
plt.xlabel("l")
plt.ylabel(r"$C_l^{BB}$")
plt.show()