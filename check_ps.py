import numpy as np
import matplotlib.pyplot as plt
import csv

Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

ell=31

points=[]
errors=[]

with open("planck.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    cols = [float(row[1]) for row in reader]

points=[cols[i] for i in range(len(cols)) if i%2==0]
errors=[cols[i] for i in range(len(cols)) if i%2==1]
errors=[errors[i]-points[i] for i in range(len(points))]
print(points)
print(errors)
#=========functions==============#
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(ell-2)
    for i in np.arange(2,ell,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#=========noise ps============#
spectrum=np.zeros(ell-2)
for i in np.arange(2,ell,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

data1=np.loadtxt('reio_camb01_cl_lensed.dat')
data2=np.loadtxt('reio_many00_cl_lensed.dat')

l1=data1[:,0]
l2=data2[:,0]
EE1=data1[:,1]
EE2=data2[:,1]

#errors_EE2=error(EE2,spectrum)
#errors_EE1=error(EE1,spectrum)
plt.plot(l2[0:ell-2],EE2[0:ell-2]*(2.7255e6)**2,label="reio_many")
plt.plot(l1[0:ell-2],EE1[0:ell-2]*(2.7255e6)**2,label="reio_camb")
plt.errorbar(np.arange(2,ell,1),points,yerr=errors,label="paper",fmt="o")
#plt.errorbar(np.arange(2,ell,1),EE2[0:ell-2],yerr=errors_EE2,label="reio_many")
#plt.errorbar(np.arange(2,ell,1),EE1[0:ell-2],yerr=errors_EE1,label="reio_camb")
plt.yscale('log')
plt.legend()
plt.savefig("check_EE1.jpg")