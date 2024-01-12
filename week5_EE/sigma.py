import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import sys

#======input=========#
try:
    p1_value=float(sys.argv[1])
    p1_sigma=float(sys.argv[2])
    p1_name=sys.argv[3]
    p2_value=float(sys.argv[4])
    p2_sigma=float(sys.argv[5])
    p2_name=sys.argv[6]
    steps=float(sys.argv[7])
    ranges=float(sys.argv[8])

except Exception as e:
    print("Input Error:", e)

chi2_total=np.load("chi21_Wishert.npy")
p_value=[p1_value,p2_value]
p_sigma=[p1_sigma,p2_sigma]
p_name=[p1_name,p2_name]
#=====function==========#
def posterior(chi2):
    post=np.zeros((chi2.shape[0],chi2.shape[1]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            post[i,j]=np.exp(-0.5*chi2[i,j])
        #print(chi2[i,j])
    return post

def func(r,p,mu):
    sigma=p[0]
    N=p[1]
    return N*np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

def draw_1D(plsq,posts,values,sigmas,names,i):
    plt.plot(np.arange(float(values[i]-ranges*sigmas[i]),float(values[i]+ranges*sigmas[i]),float(sigmas[i]/steps)),posts[i])
    plt.plot(np.arange(float(values[i]-ranges*sigmas[i]),float(values[i]+ranges*sigmas[i]),float(sigmas[i]/steps)),[func(j,plsq,values[i]) for j in np.arange(float(values[i]-ranges*sigmas[i]),float(values[i]+ranges*sigmas[i]),float(sigmas[i]/steps))])
    plt.xlabel(names[i])
    plt.ylabel("P("+names[i]+")")
    plt.savefig("week5result/"+names[i]+"1D_posterior.jpg")
    plt.show()
    plt.cla()

def fit(sigma0,N0,posts,values,sigmas,i):
    plsq=leastsq(residuals,[sigma0,N0],args=(posts[i],np.arange(float(values[i]-ranges*sigmas[i]),float(values[i]+ranges*sigmas[i]),float(sigmas[i]/steps)),values[i]))
    print(plsq[0])
    return plsq[0]

post=posterior(chi2_total)
post_p1=np.zeros(post.shape[0])
post_p2=np.zeros(post.shape[1])

for i in range(post.shape[0]):
    for j in range(post.shape[1]):
        post_p1[i]+=post[i,j]*p2_sigma/steps
        post_p2[j]+=post[i,j]*p1_sigma/steps

post_ps=[post_p1,post_p2]

sigma01=10**(int(np.log10(p1_sigma)))
sigma02=10**(int(np.log10(p2_sigma)))
sigma0=[sigma01,sigma02]
for i in [0,1]:
    N0=1e26
    plsq=fit(sigma0[i],N0,post_ps,p_value,p_sigma,i)
    draw_1D(plsq,post_ps,p_value,p_sigma,p_name,i)

fig = plt.figure()
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(float(p2_value-ranges*p2_sigma),float(p2_value+ranges*p2_sigma),float(p2_sigma/steps)),np.arange(float(p1_value-ranges*p1_sigma),float(p1_value+ranges*p1_sigma),float(p1_sigma/steps)))
contour=ay.contourf(X,Y,posterior(chi2_total))#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel(p2_name)
ay.set_ylabel(p1_name)
fig.colorbar(contour)
plt.savefig("week5result/post_2D.jpg")
plt.show()



