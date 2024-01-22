import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#======input=========#
p1_start=8.5#input("p1_start ")
p1_end=9.3#input("p1_end ")
p1_step=0.001#input("p1_step ")
p1_name="z_reio"#input("p1_name ")

chi2_EE=np.load("/home/hcjiang/class/chi21_EE_"+p1_name+".npy")
#chi2_BB=chi2_BB[0:400,:]

#=====function==========#
def posterior(chi2):
    post=np.zeros(len(chi2))
    for i in range(len(chi2)):
        post[i]=np.exp(-0.5*chi2[i])
    print(post)
    return post

def fit_curve(P,sigma,mu):
    result=np.zeros(len(P))
    for i in range(len(P)):
        result[i]=(P[i]-mu)**2/sigma**2
    return result
    
def func(r,p,mu):
    sigma=p[0]
    N=p[1]
    return N*np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

post=posterior(chi2_EE[0])
print(post)
#print(post.shape[0])
#print(post.shape[1])

sigma0=1e-1
plsq=leastsq(residuals,[sigma0,1e10],args=(post,np.arange(p1_start,p1_end,p1_step),8.893))
print(plsq[0])
plt.plot(np.arange(p1_start,p1_end,p1_step),post)
plt.plot(np.arange(p1_start,p1_end,p1_step),[func(j,plsq[0],8.9) for j in np.arange(p1_start,p1_end,p1_step)])
plt.xlabel(p1_name)
plt.ylabel("P("+p1_name+")")
plt.savefig(p1_name+"2D_posterior.jpg")
plt.show()
plt.cla()


