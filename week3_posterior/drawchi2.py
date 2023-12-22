import numpy as np
import matplotlib.pyplot as plt
#======input=========#
p1_start=0.09#input("p1_start ")
p1_end=0.10995#input("p1_end ")
p1_step=0.00005#input("p1_step ")
p1_name="r"#input("p1_name ")
p2_start=0.051#input("p2_start ")
p2_end=0.057#input("p2_end ")
p2_step=0.00001#input("p2_step ")
p2_name="tau_reio"#input("p2_name ")

#=======functions=========#
def posterior(chi2):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j])
            #print(chi2[i,j])
    print(post)
    return post

chi2_BB=np.load("/home/hcjiang/class/chi21_BB.npy")
#chi2_BB=chi2_BB[0:400,:]

fig = plt.figure()
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(float(p2_start),float(p2_end),float(p2_step)),np.arange(float(p1_start),float(p1_end),float(p1_step)))
contour=ay.contourf(X,Y,posterior(chi2_BB))#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel(p2_name)
ay.set_ylabel(p1_name)
fig.colorbar(contour)
plt.savefig("chi2_2D.jpg")
plt.show()
