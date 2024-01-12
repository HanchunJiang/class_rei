import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt('output/reio_camb00_cl_lensed.dat')
data2=np.loadtxt('output/reio_mine00_cl_lensed.dat')

l1=data1[:,0]
l2=data2[:,0]
EE1=data1[:,1]
EE2=data2[:,1]

plt.loglog(l2,EE2)
plt.loglog(l1,EE1)
plt.savefig("check_EE.jpg")