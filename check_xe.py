import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt('output/reio_camb00_thermodynamics.dat')
data2=np.loadtxt('output/reio_many00_thermodynamics.dat')

z1=data1[0:1200,1]
z2=data2[0:1200,1]
xe1=data1[0:1200,3]
xe2=data2[0:1200,3]

plt.plot(z1,xe1,label="reio_camb")
plt.plot(z2,xe2,label="reio_double")
plt.savefig("check_xe.jpg")