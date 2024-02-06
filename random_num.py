import numpy as np
import os
import powerspectrum as ps

class random_num:
    redshift=[]
    xe=[]
    root="output/check"#生成路径
    num=0
    
    def __init__(self,isnpy=False,redshift=None,xe=None,verbose=True,file_name="check.ini",root="output/check",p_name=["r"],p_value=[0.001],num=0,z_start=6,z_end=22,xe_start=0,xe_end=1.0,ell=31,EE_fid=[],errors=[],open_tau=False,tau_threshold=0.045):
        '''
        if isnpy==False:
            redshift: tuple
            xe: tuple
        if isnpy==True:
            num: the numbers random points you want to generate
        '''
        if isnpy==True:#已经有了结果
            self.redshift=redshift.copy()
            self.xe=xe.copy()
            self.num=len(self.xe)
            self.root=root
            self.p_name=p_name
            self.p_value=p_value
            self.file_name=file_name

        if isnpy==False:#还未测试
            self.root=root
            self.num=num
            while(1):
                zs=z_start+(z_end-z_start)*np.random.rand(num)
                zs=np.sort(zs)
                xes=xe_start+(xe_end-xe_start)*np.random.rand(num)
                ps.write_ps_many(p_name,p_value,zs,xes,file_name,verbose,root)
                os.system('./class '+file_name)
                data1=np.loadtxt(root+'00_cl_lensed.dat')
                EE=data1[0:ell-2,1]
                chi2=self.calculate_chi2(EE,EE_fid,errors,ell,root)
                os.system('rm -rf '+root+'*dat')
                if chi2<np.sqrt(2*(ell-2)):
                    if open_tau==True:
                        if self.get_tau()>tau_threshold:
                            self.redshift=zs.copy()
                            self.xe=xes.copy()
                            break
                    else:
                        self.redshift=zs.copy()
                        self.xe=xes.copy()
                        break

    def calculate_chi2(EE,EE_fid,errors,ell,chi_root):#还未测试
        for i in range(len(EE)):
            sum+=(EE[i]*(2.7255e6)**2-EE_fid[i])**2/errors[i]**2
        with open(chi_root+'chi_log.txt','a') as f:
            f.write(str(sum)+'\n')
        return sum-ell+2
    
    def get_tau():#还未测试
        with open('/home/hcjiang/class/optical_depth.txt','r') as f:  # 打开文件
            lines = f.readlines()  # 读取所有行
            last_line = lines[-1]  # 取最后一行
        return float(last_line)

    def run(self,verbose=1):
        ps.write_ps_many(self.p_name,self.p_value,self.redshift,self.xe,self.file_name,verbose,self.root)
        os.system('./class '+self.file_name)

    
    

           

