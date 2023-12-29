import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#======input=========#
p1_value=0.1
p1_sigma=0.0002821
p1_name="r"#input("p1_name ")

chi2_BB=np.load("/home/hcjiang/class/chi21_total_Wishert_1d.npy")

#=====function==========#
def posterior(chi2):
    post=np.zeros(len(chi2))
    for i in range(len(chi2)):
        post[i]=np.exp(-0.5*chi2[i])
        #print(chi2[i,j])
    print(post)
    return post

def func(r,p,mu):
    sigma=p[0]
    N=p[1]
    return N*np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

post=posterior(chi2_BB)
#print(post.shape[0])
#print(post.shape[1])

sigma0=1e-4
N0=10
plsq=leastsq(residuals,[sigma0,N0],args=(post,np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),0.1))
print(plsq[0])
plt.plot(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),post)
plt.plot(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)),[func(i,plsq[0],0.1) for i in np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))])
plt.xlabel(p1_name)
plt.ylabel("P("+p1_name+")")
plt.savefig(p1_name+"1D_posterior.jpg")
plt.show()
plt.cla()


