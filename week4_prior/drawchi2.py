import numpy as np
import matplotlib.pyplot as plt
#======input=========#
p1_value=0.1
p1_sigma=0.0002303
p1_name="r"#input("p1_name ")
p2_value=0.0561
p2_sigma=0.0001085
p2_name="tau_reio"#input("p2_name ")

#=======functions=========#
def posterior(chi2,tau,tau0,sigma_tau):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j]-0.5*(tau[j]-tau0)**2/sigma_tau**2)
            #print(chi2[i,j])
    print(post)
    return post

chi2_BB=np.load("/home/hcjiang/class/chi21_BB_prior.npy")

fig = plt.figure()
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)))
contour=ay.contourf(X,Y,posterior(chi2_BB,np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),0.0561,0.0071))#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel(p2_name)
ay.set_ylabel(p1_name)
fig.colorbar(contour)
plt.savefig("chi2_2D.jpg")
plt.show()
