import numpy as np

#======input=========#
p1_value=0.1
p1_sigma=0.0002303
p1_name="r"#input("p1_name ")
p2_value=0.0561
p2_sigma=0.0001085
p2_name="tau_reio"#input("p2_name ")

#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=======functions=========#
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(2000)
    for i in np.arange(2,2002,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#chi2
def chi2(Cl_fid,Cl,sigma):
    '''
    Cl_fid: ground truth
    Cl: PS we want to calculate chi2
    sigma: error
    '''
    sum=0
    for i in range(min(len(Cl),len(sigma))):
        sum+=(Cl_fid[i]-Cl[i])**2/sigma[i]**2
        #print(sum)
    print(sum)
    return sum

#========result========#
chi2_BB=np.zeros((len(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))),len(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)))))

#====Array=======#
#noise ps
spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#Cl_fid
data_fid=np.loadtxt('reio_camb00_cl.dat')
BB_fid=data_fid[0:2000,2]
errors_BB=error(BB_fid,spectrum)

j=-1
for p1 in np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)):
    j+=1
    p=0
    for i in range(len(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)))):
        if (i%100)<10:
            data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_0'+str(i%100)+'_cl.dat')
        else:
            data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_'+str(i%100)+'_cl.dat')
        BBs=data[0:2000,2]
        chi2_BB[j,i]=chi2(BB_fid,BBs,errors_BB)

np.save("chi21_BB_prior.npy",chi2_BB)

