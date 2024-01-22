import numpy as np
import sys

#======input=========#
try:
    p1_start=float(sys.argv[1])
    p1_end=float(sys.argv[2])
    p1_step=float(sys.argv[3])
    p1_name=sys.argv[4]
    p2_start=float(sys.argv[5])
    p2_end=float(sys.argv[6])
    p2_step=float(sys.argv[7])
    p2_name=sys.argv[8]

except Exception as e:
    print("Input Error:", e)

ell=2002
#======parameters=========#
Tcmb=2.75*10**6
sigma_nu=2*np.pi/180/60
theta_nu=30*np.pi/180/60
f_sky=1
delta_l=1

#=======functions=========#
def error(PS,NN):
    '''calculate sigma in chi2'''
    errors=np.zeros(ell-2)
    for i in np.arange(2,ell,1):
        errors[i-2]=((PS[i-2]+NN[i-2])/np.sqrt((i+0.5)*f_sky*delta_l))
    #print(errors)
    return errors

#chi2
def chi2_Gauss(Cl_fid,Cl,sigma):
    '''
    Cl_fid: ground truth
    Cl: PS we want to calculate chi2
    sigma: error
    '''
    sum=0
    for i in range(min(len(Cl),len(sigma))):
        sum+=(Cl_fid[i]-Cl[i])**2/sigma[i]**2
        #print(sum)
    return sum

def chi2(Cl_fid,Cl,NN):
    sum=0
    for i in range(min(len(Cl),len(NN))):
        sum+=(2*(i+2)+1)*((Cl_fid[i]+NN[i])/(Cl[i]+NN[i])+np.log(Cl[i]+NN[i])-(2*(i+2)-1)/(2*(i+2)+1)*np.log(Cl_fid[i]+NN[i]))
    return sum


#========result========#
#chi2_BB=np.zeros((len(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))),len(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)))))
#chi2_EE=np.zeros((len(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))),len(np.arange(float(p2_value-5*p2_sigma),float(p2_value+5*p2_sigma),float(p2_sigma/10.0)))))
chi2_total=np.zeros((len(np.arange(float(p1_start),float(p1_end),float(p1_step))),len(np.arange(float(p2_start),float(p2_end),float(p2_step)))))
#chi2_total=np.zeros(len(np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0))))

#====Array=======#
#noise ps
spectrum=np.zeros(2000)
for i in np.arange(2,2002,1):
    spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))

#Cl_fid
data_fid=np.loadtxt('reio_many00_cl_lensed.dat')
BB_fid=data_fid[0:2000,2]
EE_fid=data_fid[0:2000,1]
#errors_BB=error(BB_fid,spectrum)

j=-1
for p1 in np.arange(float(p1_start),float(p1_end),float(p1_step)):
    j+=1
    for i in range(len(np.arange(float(p2_start),float(p2_end),float(p2_step)))):
        if (i%100)<10:
            data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_0'+str(i%100)+'_cl_lensed.dat')
        else:
            data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_'+str(i%100)+'_cl_lensed.dat')
        BBs=data[0:2000,2]
        #print(BBs)
        EEs=data[0:2000,1]
        #print(EEs)

        #chi2_BB[j,i]
        chi2_BB=chi2(BB_fid,BBs,spectrum[0:ell-2])#errors_BB)
        chi2_EE=chi2(EE_fid,EEs,spectrum[0:ell-2])
        chi2_total[j,i]=chi2_BB+chi2_EE

max_chi=np.max(chi2_total)
for i in range(chi2_total.shape[0]):
    for j in range(chi2_total.shape[1]):
        chi2_total[i,j]=chi2_total[i,j]-max_chi

np.save("week7_search/chi21_Wishert.npy",chi2_total)
