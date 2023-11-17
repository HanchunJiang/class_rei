import numpy as np
import matpoltlib.pyplot as plt
f_sky=1
delta_l=1
NNs=np.load("spectrum.npy")

files=['/Users/hanchunjiang/class_public-3.2.0/output/reio_camb02_cl.dat']
data=[]
for data_file in files:
    data.append(np.loadtxt(data_file))

curve=data[0]
TTs=curve[0:800,1]

errors=np.zeros(182)
for i in np.arange(2,184,1):
    errors[i-2]=(TTs[i-2]+NNs[i-2]/np.sqrt((i+0.5)*f_sky*delta_l))

print(errors)