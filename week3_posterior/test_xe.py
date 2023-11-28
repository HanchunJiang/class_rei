import numpy as np
import matplotlib.pyplot as plt

files=['/Users/hanchunjiang/class_public-3.2.0/output/reio_camb04_thermodynamics.dat','/Users/hanchunjiang/class_public-3.2.0/output/reio_mine14_thermodynamics.dat']
data=[]
for data_file in files:
    data.append(np.loadtxt(data_file))

curve0=data[0]
z0=curve0[:,1]
X_e0=curve0[:,3]

curve1=data[1]
z1=curve1[:,1]
X_e1=curve1[:,3]

z0=z0[z0<30]
z1=z1[z1<30]
plt.plot(z0,X_e0[:len(z0)])
plt.plot(z1,X_e1[:len(z1)])
plt.show()
