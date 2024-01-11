import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt('output/reio_mine00_thermodynamics.dat')
data2=np.loadtxt('output/reio_camb00_thermodynamics.dat')

z1=data1[:,1]
z2=data2[:,1]
xe1=data1[:,3]
xe2=data2[:,3]

plt.loglog(z1,xe1)
plt.loglog(z2,xe2)
plt.savefig("check_xe.jpg")