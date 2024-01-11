import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1
sigma_tau_planck=1e-4#0.0071

#=========input==============#
data_lfid=np.loadtxt('reio_camb00_cl_lensed.dat')
data_l1p=np.loadtxt('reio_camb01_cl_lensed.dat')
data_l1m=np.loadtxt('reio_camb02_cl_lensed.dat')
data_l2p=np.loadtxt('reio_camb03_cl_lensed.dat')
data_l2m=np.loadtxt('reio_camb04_cl_lensed.dat')

delta_1=0.00005
delta_2=0.0001

p1_value=0.1
p2_value=0.0561

p1_name="r"
p2_name="tau"

#========function==============#
def Fisher(fid,NN,ip,im,jp,jm,delta_i,delta_j):
    sum=0
    for k in range(len(fid)):
        sum+=(2*(k+2)+1)/2*f_sky/(fid[k]+NN[k])**2*(ip[k]-im[k])/2/delta_i*(jp[k]-jm[k])/2/delta_j
    return sum

BB_lfid=data_lfid[0:2000,2]
BB_l1p=data_l1p[0:2000,2]
BB_l1m=data_l1m[0:2000,2]
BB_l2p=data_l2p[0:2000,2]
BB_l2m=data_l2m[0:2000,2]

spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

F_11=1.5*Fisher(BB_lfid,spectrum,BB_l1p,BB_l1m,BB_l1p,BB_l1m,delta_1,delta_1)
F_22=1.5*(Fisher(BB_lfid,spectrum,BB_l2p,BB_l2m,BB_l2p,BB_l2m,delta_2,delta_2)+1/sigma_tau_planck**2)
F_12=1.5*Fisher(BB_lfid,spectrum,BB_l1p,BB_l1m,BB_l2p,BB_l2m,delta_1,delta_2)

p1_sigma=np.sqrt(1/F_11)
p2_sigma=np.sqrt(1/F_22)
p1p2_sigma=np.sqrt(F_11*F_22)/F_12

F  = np.array([[F_11,F_12], [F_12, F_22]])  
print(F)  
C=np.linalg.inv(F)
print(C)
p1_sigma=np.sqrt(C[0,0])
p2_sigma=np.sqrt(C[1,1])
p1p2_sigma=C[0,1]

a=np.sqrt((p1_sigma**2+p2_sigma**2)/2.0+np.sqrt((p1_sigma**2-p2_sigma**2)**2/4.0+p1p2_sigma**2))
b=np.sqrt((p1_sigma**2+p2_sigma**2)/2.0-np.sqrt((p1_sigma**2-p2_sigma**2)**2/4.0+p1p2_sigma**2))
theta=np.arctan(2*p1p2_sigma/(p1_sigma**2-p2_sigma**2))/2.0


'''
rs=np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))
taus=np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0))

post=np.zeros((len(rs),len(taus)))
for i in range(len(rs)):
    for j in range(len(taus)):
        post[i,j]=np.exp(-0.5*rs[i]*F_12*taus[j])

fig = plt.figure()
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)),np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)))
contour=ay.contourf(X,Y,post)#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel(p2_name)
ay.set_ylabel(p1_name)
fig.colorbar(contour)
plt.savefig("fisher.jpg")
plt.show()
'''

fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')
e = Ellipse(xy = (p1_value,p2_value), width = a * 2, height = b * 2, angle=theta*180/3.14)
ax.add_artist(e)
ax.set_xlabel(p1_name)
ax.set_ylabel(p2_name)
plt.xlim(p1_value-2*a, p1_value+2*a)
plt.ylim(p2_value-5*b,p2_value+5*b)
plt.savefig("fisher.jpg")
plt.show()

print(p1_sigma)
print(p2_sigma)
print(p1p2_sigma)

print(np.sqrt(1/F_11))
print(np.sqrt(1/F_22))
print(np.sqrt(F_11*F_22)/F_12)