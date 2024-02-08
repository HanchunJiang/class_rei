import numpy as np
import powerspectrum as ps
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

class posterior:
    p1_range=[]
    p2_range=[]
    name=[]
    post=[]
    best_fit=[]
    sigma=[]
    spectrum=[]
    ell=0

    def __init__(self,ell=2002,fid_root=" ",p_name=["r","z_reio"],p1_range=[],p2_range=[],ps_exist=False,sigma_nu=2*np.pi/180/60,Tcmb=2.75*10**6,theta_nu=30*np.pi/180/60,save_npy=False,save_root=" ",verbose=True):
        self.p1_range=p1_range.copy()
        self.p2_range=p2_range.copy()
        self.name=p_name.copy()
        self.ell=ell
        self.spectrum=np.zeros(ell-2)
        for i in np.arange(2,ell,1):
            self.spectrum[i-2]=(sigma_nu/Tcmb)**2*np.exp(i*(i+1)*theta_nu**2/8/np.log(2))
        if ps_exist==False:
            ps.run_fit_ps([self.p1_range,self.p2_range],self.name,verbose=verbose)
        self.get_posterior_2D(fid_root,save_npy,save_root)
        self.get_best_fit()

    def chi2(self,Cl_fid,Cl):
        sum=0
        for i in range(min(len(Cl),len(self.spectrum))):
            sum+=(2*(i+2)+1)*((Cl_fid[i]+self.spectrum[i])/(Cl[i]+self.spectrum[i])+np.log(Cl[i]+self.spectrum[i])-(2*(i+2)-1)/(2*(i+2)+1)*np.log(Cl_fid[i]+self.spectrum[i]))
        return sum
    
    def cal_post(self,chi2):
        post=np.zeros((chi2.shape[0],chi2.shape[1]))
        for i in range(chi2.shape[0]):
            for j in range(chi2.shape[1]):
                post[i,j]=np.exp(-0.5*chi2[i,j])
        return post

    def get_posterior_2D(self,fid_root,save_npy=False,save_root=" "):
        #ps.run_fit_ps([self.p1_range,self.p2_range],self.name)
        chi2_total=np.zeros((len(self.p1_range),len(self.p2_range)))
        data_fid=np.loadtxt(fid_root+'_cl_lensed.dat')
        BB_fid=data_fid[0:self.ell-2,2]
        EE_fid=data_fid[0:self.ell-2,1]

        for j in range(len(self.p1_range)):
            for i in range(len(self.p2_range)):
                if (i%100)<10:
                    data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_0'+str(i%100)+'_cl_lensed.dat')
                else:
                    data=np.loadtxt('output/chi1_'+str(j)+'_'+str(int(i/100))+'_'+str(i%100)+'_cl_lensed.dat')
                BBs=data[0:self.ell-2,2]
                EEs=data[0:self.ell-2,1] 
                chi2_BB=self.chi2(BB_fid,BBs)
                chi2_EE=self.chi2(EE_fid,EEs)
                chi2_total[j,i]=chi2_BB+chi2_EE

        max_chi=np.max(chi2_total)
        for i in range(chi2_total.shape[0]):
           for j in range(chi2_total.shape[1]):
                chi2_total[i,j]=chi2_total[i,j]-max_chi
        
        self.post=self.cal_post(chi2_total)

        if save_npy==True:
            np.save(save_root+"post.npy",chi2_total)
    
    def get_best_fit(self):
        a=np.argmax(self.post)
        maxi=int(a/self.post.shape[0])
        maxj=a%self.post.shape[1]
        best_fit_p1=self.p1_range[maxi]
        best_fit_p2=self.p2_range[maxj]
        self.best_fit=[best_fit_p1,best_fit_p2]
    
    def draw_2D(self,root="week8result1/post_"):
        fig = plt.figure()
        ay=fig.add_subplot()
        X,Y = np.meshgrid(self.p2_range,self.p1_range)
        contour=ay.contourf(X,Y,self.post)#,colors=['blue','lightsteelblue','white'])
        ay.set_xlabel(self.name[1])
        ay.set_ylabel(self.name[0])
        fig.colorbar(contour)
        plt.savefig(root+"2D.jpg")

#=====post for small and final============#
class post_sigma(posterior):
    post_p1=[]
    post_p2=[]
    ranges=1
    steps=1
    p_sigma_before=[]
    p_sigma=[]
    def __init__(self,ell=2002,fid_root=" ",p_name=["r","z_reio"],p_value=[],p_sigma=[],ps_exsit=False,steps=1,ranges=1,sigma_nu=2*np.pi/180/60,Tcmb=2.75*10**6,theta_nu=30*np.pi/180/60,save_npy=False,save_root=" ",verbose=True):
        p1_range=np.arange(float(p_value[0]-ranges*p_sigma[0]),float(p_value[0]+ranges*p_sigma[0]),float(p_sigma[0]/steps))
        p2_range=np.arange(float(p_value[1]-ranges*p_sigma[1]),float(p_value[1]+ranges*p_sigma[1]),float(p_sigma[1]/steps))
        self.ranges=ranges
        self.steps=steps
        self.p_sigma_before=p_sigma.copy()
        posterior.__init__(self,ell,fid_root,p_name,p1_range,p2_range,ps_exsit,sigma_nu,Tcmb,theta_nu,save_npy,save_root,verbose)
        self.get_posterior_1D(p_sigma,steps)
    
    def get_posterior_1D(self,p_sigma,steps):
        self.post_p1=np.zeros(self.post.shape[0])
        self.post_p2=np.zeros(self.post.shape[1])

        for i in range(self.post.shape[0]):
            for j in range(self.post.shape[1]):
                self.post_p1[i]+=self.post[i,j]*p_sigma[1]/steps
                self.post_p2[j]+=self.post[i,j]*p_sigma[0]/steps
    
    def func(r,p,mu):
        sigma=p[0]
        N=p[1]
        return N*np.exp(-(r-mu)**2/2/sigma**2)

    def residuals(self,p,y,x,mu):
        return y-self.func(x,p,mu)
    
    def fit(self,sigma0,N0,post,value,sigma):
        fit_array=np.arange(value-self.ranges*sigma,value+self.ranges*sigma,sigma/self.steps)
        fit_array=self.correct(fit_array,len(post),value,sigma)
        plsq=leastsq(self.residuals,[sigma0,N0],args=(post,fit_array,value))
        print(plsq[0])
        return plsq[0],fit_array
    
    def correct(fit_array,len_post,value,sigma,ranges):
        if len(fit_array)<len_post:#待测试
            fit_array=np.append(fit_array,value+ranges*sigma)
        elif len(fit_array)>len_post:
            fit_array=fit_array[0:-1]
        return fit_array.copy()
    
    def get_sigma(self,save=False,draw=True,root=" "):
        post_ps=[self.post_p1,self.post_p2]
        sigma0=[10**(int(np.log10(self.p_sigma_before[0]))),10**(int(np.log10(self.p_sigma_before[1])))]
        for i in [0,1]:
            N0=1e12
            plsq,fit_array=self.fit(sigma0[i],N0,post_ps[i],self.best_fit[i],self.p_sigma_before[i])
            self.p_sigma.append(plsq[0])
            if save==True:
                with open(root+'sigma1.txt','a') as f:
                    f.write(str(plsq[0])+"\n")
            if draw==True:
                self.draw_1D(plsq,fit_array,post_ps[i],self.best_fit[i],self.name[i],root)
    
    def draw_1D(self,plsq,fit_array,post,value,name,root):
        plt.plot(fit_array,post)
        plt.plot(fit_array,[self.func(j,plsq,value) for j in fit_array])
        plt.xlabel(name)
        plt.ylabel("P("+name+")")
        plt.savefig(root+"_"+name+"1D_posterior.jpg")
        plt.cla()

#=====post for large and middle============#
class post_search(posterior):
    def __init__(self,ell=2002,fid_root=" ",p_name=["r","z_reio"],p_start=[],p_end=[],p_step=[],ps_exist=False,sigma_nu=2*np.pi/180/60,Tcmb=2.75*10**6,theta_nu=30*np.pi/180/60,save_npy=False,save_root=" ",verbose=True):
        p1_range=np.arange(float(p_start[0]),float(p_end[0]),float(p_step[0]))
        p2_range=np.arange(float(p_start[1]),float(p_end[1]),float(p_step[1]))
        posterior.__init__(self,ell,fid_root,p_name,p1_range,p2_range,ps_exist,sigma_nu,Tcmb,theta_nu,save_npy,save_root,verbose)


