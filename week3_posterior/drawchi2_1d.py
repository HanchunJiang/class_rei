import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#=========input==============#
p_start=float(input("p_start "))
p_end=float(input("p_end "))
p_step=float(input("p_step "))
p_name=input("p_name ")

chi2_BB=np.load("chi21_EE_"+p_name+".npy")
print(chi2_BB)

#=======functions============#
def posterior(chi2):
    #post=np.zeros((chi2.shape[0],chi2.shape[1]))
    post=np.zeros(len(chi2))
    for i in range(len(chi2)):
        post[i]=np.exp(-0.5*chi2[i])
    print(post)
    return post

def fit_curve(P,sigma):
    result=np.zeros(len(P))
    for i in range(len(P)):
        result[i]=(P[i]-0.1)**2/sigma**2
    return result
    
def func(r,sigma):
    return np.exp(-(r-0.1)**2/2/sigma**2)

def residuals(p,y,x):
    return y-func(x,p)

#==========posterior=============#
post_BB=posterior(chi2_BB[0])
sum=0
for i in range(len(post_BB)):
    sum+=post_BB[i]

print(sum)
N=1/sum
print(N)

#=========sigma==========#
sigma0=1e-5
plsq=leastsq(residuals,sigma0,args=(post_BB,np.arange(p_start,p_end,p_step)))
print(plsq[0])
plt.plot(np.arange(p_start,p_end,p_step),chi2_BB[0])
#plt.plot(np.arange(p_start,p_end,p_step),fit_curve(np.arange(p_start,p_end,p_step),plsq[0]))
plt.xlabel(p_name)
plt.ylabel(r"$\chi^2$")
plt.savefig(p_name+"_chi2.jpg")
plt.show()
plt.cla()

plt.plot(np.arange(p_start,p_end,p_step),[func(i,plsq[0]) for i in np.arange(p_start,p_end,p_step)])
plt.plot(np.arange(p_start,p_end,p_step),post_BB)
plt.xlabel(p_name)
plt.ylabel("P("+p_name+")")
plt.savefig(p_name+"_posterior.jpg")
plt.show()


