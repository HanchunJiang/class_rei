import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#======input=========#
p1_value=0.1
p1_sigma=0.0002303
p1_name="r"#input("p1_name ")
p2_value=0.0561
p2_sigma=0.0001085
p2_name="tau_reio"#input("p2_name ")

chi2_BB=np.load("/home/hcjiang/class/chi21_BB_Wishert.npy")

#=====function==========#
def posterior(chi2,tau,tau0,sigma_tau):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j]-0.5*(tau[j]-tau0)**2/sigma_tau**2)
            #print(chi2[i,j])
    print(post)
    return post

def func(r,p,mu):
    sigma=p[0]
    N=p[1]
    return N*np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

post=posterior(chi2_BB,np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),0.0561,0.0071)
#print(post.shape[0])
#print(post.shape[1])
post_p1=np.zeros(post.shape[0])
post_p2=np.zeros(post.shape[1])

#sum=0
for i in range(post.shape[0]):
    for j in range(post.shape[1]):
        post_p1[i]+=post[i,j]*p2_sigma/10
        #sum+=post_p1[i]*p1_sigma/10

#post_p1=[post_p1[i]/sum for i in range(len(post_p1))]
#print(sum)
#sum=0
for i in range(post.shape[1]):
    for j in range(post.shape[0]):
        post_p2[i]+=post[j,i]*p1_sigma/10
        #sum+=post_p2[i]*p2_sigma/10

#post_p2=[post_p2[i]/sum for i in range(len(post_p2))]
#print(sum)
sigma0=1e-4
N0=1
plsq=leastsq(residuals,[sigma0,N0],args=(post_p1,np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),0.1))
print(plsq[0])
plt.plot(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),post_p1)
plt.plot(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),[func(i,plsq[0],0.1) for i in np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))])
plt.xlabel(p1_name)
plt.ylabel("P("+p1_name+")")
plt.savefig(p1_name+"2D_posterior.jpg")
plt.show()
plt.cla()

sigma0=1e-4
N0=1
plsq=leastsq(residuals,[sigma0,N0],args=(post_p2,np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),0.0561))
print(plsq[0])
plt.plot(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),post_p2)
plt.plot(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),[func(i,plsq[0],0.0561) for i in np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0))])
plt.xlabel(p2_name)
plt.ylabel("P("+p2_name+")")
plt.savefig(p2_name+"2D_posterior.jpg")
plt.show()
plt.cla()


