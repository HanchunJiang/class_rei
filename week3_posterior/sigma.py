import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#======input=========#
p1_start=0.09#input("p1_start ")
p1_end=0.10995#input("p1_end ")
p1_step=0.00005#input("p1_step ")
p1_name="r"#input("p1_name ")
p2_start=0.051#input("p2_start ")
p2_end=0.057#input("p2_end ")
p2_step=0.00001#input("p2_step ")
p2_name="tau_reio"#input("p2_name ")

chi2_BB=np.load("/home/hcjiang/class/chi21_BB.npy")
chi2_BB=chi2_BB[0:400,:]

#=====function==========#
def posterior(chi2):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j])
            #print(chi2[i,j])
    print(post)
    return post

def fit_curve(P,sigma,mu):
    result=np.zeros(len(P))
    for i in range(len(P)):
        result[i]=(P[i]-mu)**2/sigma**2
    return result
    
def func(r,sigma,mu):
    return np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

post=posterior(chi2_BB)
#print(post.shape[0])
#print(post.shape[1])
post_p1=np.zeros(post.shape[0])
post_p2=np.zeros(post.shape[1])

for i in range(post.shape[0]):
    for j in range(post.shape[1]):
        post_p1[i]+=post[i,j]*0.00005

for i in range(post.shape[1]):
    for j in range(post.shape[0]):
        post_p2[i]+=post[j,i]*0.00001

sigma0=1e-5
plsq=leastsq(residuals,sigma0,args=(post_p1,np.arange(p1_start,p1_end,p1_step),0.1))
print(plsq[0])
plt.plot(np.arange(p1_start,p1_end,p1_step),post_p1)
plt.xlabel(p1_name)
plt.ylabel("P("+p1_name+")")
plt.savefig(p1_name+"2D_posterior.jpg")
plt.show()
plt.cla()

sigma0=1e-5
plsq=leastsq(residuals,sigma0,args=(post_p2,np.arange(p2_start,p2_end,p2_step),0.054))
print(plsq[0])
plt.plot(np.arange(p2_start,p2_end,p2_step),post_p2)
plt.xlabel(p2_name)
plt.ylabel("P("+p2_name+")")
plt.savefig(p2_name+"2D_posterior.jpg")
plt.show()
plt.cla()


