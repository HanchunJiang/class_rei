import numpy as np

files=['/Users/hanchunjiang/class_public-3.2.0/output/reio_camb02_cl.dat']
data=[]
for data_file in files:
    data.append(np.loadtxt(data_file))

