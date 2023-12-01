import numpy as np
import matplotlib.pyplot as plt
#======input=========#
'''
z_start=float(input("z_start"))
z_end=float(input("z_end"))
z_step=float(input("z_step"))
r_start=float(input("r_start"))
r_end=float(input("r_end"))
r_step=float(input("r_step"))
'''
z_start=5
z_end=10
z_step=0.4
r_start=0.01
r_end=0.3
r_step=0.04

#=======functions=========#
def posterior(chi2):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j])
            #print(chi2[i,j])
    print(post)
    return post



chi2_EE=np.load("chi2_EE.npy")
chi2_BB=np.load("chi2_BB.npy")

fig = plt.figure()
'''
ax = fig.add_subplot(projection='3d')
#ax=fig.add_subplot()
x=[i for i in np.arange(z_start,z_end,z_step) for j in range(len(np.arange(r_start,r_end,r_step)))]
y=[j for i in range(len(np.arange(z_start,z_end,z_step))) for j in np.arange(r_start,r_end,r_step)]
z=[chi2_EE[i,j] for i in range(len(np.arange(z_start,z_end,z_step))) for j in range(len(np.arange(r_start,r_end,r_step)))]

#CS = ax.contourf(X, Y, Z, [4,8],colors=['blue','lightsteelblue','white'])
ax.scatter(x,y,z)
ax.set_xlabel("z_reio")
ax.set_ylabel("r")
ax.set_zlabel(r"$\chi^2$")
#ax.contourf(X,Y,posterior(chi2_EE),colors=['blue','lightsteelblue','white'])
plt.show()
'''
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(r_start,r_end,r_step),np.arange(z_start,z_end,z_step))
contour=ay.contourf(X,Y,posterior(chi2_EE))#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel("r")
ay.set_ylabel("z_reio")
fig.colorbar(contour)
plt.show()
