import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt('output/reio_camb02_thermodynamics.dat')
data2=np.loadtxt('output/reio_mine00_thermodynamics.dat')

z1=data1[0:1200,1]
z2=data2[0:1200,1]
xe1=data1[0:1200,3]
xe2=data2[0:1200,3]

plt.plot(z1,xe1,label="reio_tanh")
plt.plot(z2,xe2,label="reio_exp")
plt.savefig("check_xe1.pdf")