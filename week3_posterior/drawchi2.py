import numpy as np
import matplotlib.pyplot as plt

chi2_EE=np.load("chi2_EE.npy")
chi2_BB=np.load("chi2_BB.npy")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x=[i for i in np.arange(5,31,1) for j in range(len(np.arange(0.05,0.8,0.05)))]
y=[j for i in range(len(np.arange(5,31,1))) for j in np.arange(0.05,0.8,0.05)]
z=[chi2_BB[i,j] for i in range(len(np.arange(5,31,1))) for j in range(len(np.arange(0.05,0.8,0.05)))]

ax.scatter(x,y,z)
plt.show()
