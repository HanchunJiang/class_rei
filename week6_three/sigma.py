import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#======input=========#
p1_value=0.001
p1_sigma=0.0001806
p1_name="r"#input("p1_name ")
p2_value=0.5
p2_sigma=0.1316
p2_name="reionization_width"#input("p2_name ")
p3_value=0.0561
p3_sigma=0.0003851
p3_name="tau_reio"#input("p3_name ")

p_value=[p1_value,p2_value,p3_value]
p_sigma=[p1_sigma,p2_sigma,p3_sigma]
p_name=[p1_name,p2_name,p3_name]

chi2_total=np.load("chi21_Wishert.npy")

#=====function==========#
def posterior(chi2):
    post=np.zeros((chi2.shape[0],chi2.shape[1],chi2.shape[2]))
    for i in range(chi2.shape[0]):
        for j in range(chi2.shape[1]):
            for k in range(chi2.shape[2]):
                post[i,j,k]=np.exp(-0.5*chi2[i,j,k])
    print(post)
    return post

def func(r,p,mu):
    sigma=p[0]
    N=p[1]
    return N*np.exp(-(r-mu)**2/2/sigma**2)

def residuals(p,y,x,mu):
    return y-func(x,p,mu)

def fit(sigma0,N0,posts,values,sigmas,i):
    plsq=leastsq(residuals,[sigma0,N0],args=(posts[i],np.arange(float(values[i]-3*sigmas[i]),float(values[i]+3*sigmas[i]),float(sigmas[i]/4.0)),values[i]))
    print(plsq[0])
    return plsq[0]

def draw_1D(plsq,posts,values,sigmas,names,i):
    plt.plot(np.arange(float(values[i]-3*sigmas[i]),float(values[i]+3*sigmas[i]),float(sigmas[i]/4.0)),posts[i])
    plt.plot(np.arange(float(values[i]-3*sigmas[i]),float(values[i]+3*sigmas[i]),float(sigmas[i]/4.0)),[func(j,plsq,values[i]) for j in np.arange(float(values[i]-3*sigmas[i]),float(values[i]+3*sigmas[i]),float(sigmas[i]/4.0))])
    plt.xlabel(names[i])
    plt.ylabel("P("+names[i]+")")
    plt.savefig("week6_result/"+names[i]+"1D_posterior.jpg")
    plt.show()
    plt.cla()

def draw_2D(orders,values,sigmas,names,posts):
    fig = plt.figure()
    ay=fig.add_subplot()
    i=orders[0]
    j=orders[1]
    k=orders[2]
    X,Y = np.meshgrid(np.arange(float(values[j]-3*sigmas[j]),float(values[j]+3*sigmas[j]),float(sigmas[j]/4.0)),np.arange(float(values[i]-3*sigmas[i]),float(values[i]+3*sigmas[i]),float(sigmas[i]/4.0)))
    contour=ay.contourf(X,Y,posts[k])#,colors=['blue','lightsteelblue','white'])
    ay.set_xlabel(names[j])
    ay.set_ylabel(names[i])
    fig.colorbar(contour)
    plt.savefig("week6_result/"+str(k)+"2D_posterior.jpg")
    plt.show()


#========variables=========#
post=posterior(chi2_total)
#print(post.shape[0])
#print(post.shape[1])
post_p1=np.zeros(post.shape[0])
post_p2=np.zeros(post.shape[1])
post_p3=np.zeros(post.shape[2])
post_p1p2=np.zeros((post.shape[0],post.shape[1]))
post_p1p3=np.zeros((post.shape[0],post.shape[2]))
post_p2p3=np.zeros((post.shape[1],post.shape[2]))

for i in range(post.shape[0]):
    for j in range(post.shape[1]):
        for k in range(post.shape[2]):
            post_p1[i]+=post[i,j,k]*p2_sigma/4*p3_sigma/4
            post_p2[j]+=post[i,j,k]*p1_sigma/4*p3_sigma/4
            post_p3[k]+=post[i,j,k]*p1_sigma/4*p2_sigma/4
            post_p1p2[i,j]+=post[i,j,k]*p3_sigma/4
            post_p1p3[i,k]+=post[i,j,k]*p2_sigma/4
            post_p2p3[j,k]+=post[i,j,k]*p1_sigma/4

post_ps=[post_p1,post_p2,post_p3]
post_pps=[post_p1p2,post_p1p3,post_p2p3]

sigma0=[1e-3,0.01,1e-3]
for i in [0,1,2]:
    N0=1e8
    plsq=fit(sigma0[i],N0,post_ps,p_value,p_sigma,i)
    draw_1D(plsq,post_ps,p_value,p_sigma,p_name,i)

for i in [[0,1,0],[0,2,1],[1,2,2]]:
    draw_2D(i,p_value,p_sigma,p_name,post_pps)




