import numpy as np
import os
import csv
import matplotlib.pyplot as plt

num_pair=20#要求的成功个数
suc=0#成功个数
num_point=3#一组几个随机点
z_start=6
z_end=22
xe_start=0
xe_end=1.0
ell=31
tau_threshold=0.045

with open("planck.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    cols = [float(row[1]) for row in reader]

data2=np.loadtxt('/home/hcjiang/class/output/base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_cl_lensed.dat')
EE_fid=data2[0:ell-2,2]*(2.7255e6)**2
points=[cols[i] for i in range(len(cols)) if i%2==0]
errors=[cols[i] for i in range(len(cols)) if i%2==1]
errors=[errors[i]-points[i] for i in range(len(points))]

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_many_tanh\n','lensing=yes\n','thermodynamics_verbose=1\n','r=0.001\n']

def write_ps(zs,xes):
    with open('check.ini','w') as f:
            for i in range(len(content)):
                f.write(content[i])
            f.write("many_tanh_num=")
            f.write(str(int(len(zs)))+"\n")
            f.write("many_tanh_z=")
            for i in zs:
                 f.write(str(round(i,10))+",")
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.write("\n")
            f.write("many_tanh_xe=")
            for i in xes:
                 f.write(str(round(i,10))+",")
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.write("\n")

def record(zs,xes,totalz,totalxe):
     with open('week8_random/randomlog.txt','a') as f:
          f.write(str(zs)+"\n")
          f.write(str(xes)+"\n")
     totalz.append(zs)
     totalxe.append(xes)

def get_tau():
     with open('file.txt','r') as f:  # 打开文件
          lines = f.readlines()  # 读取所有行
          last_line = lines[-1]  # 取最后一行
     return float(last_line)

def calculate_chi2(EE,EE_planck,errors,ell):
     sum=0
     #numerator=[]
     #denominator=[]

     for i in range(len(EE_planck)):
          #numerator.append((EE[i]*(2.7255e6)**2-EE_planck[i])**2)
          #denominator.append(errors[i]**2)
          sum+=(EE[i]*(2.7255e6)**2-EE_planck[i])**2/errors[i]**2
     with open('week8_random/chi_log.txt','a') as f:
          f.write(str(sum)+'\n')
     #plt.plot(np.arange(2,ell,1),numerator,label="numerator")
     #plt.plot(np.arange(2,ell,1),denominator,label="denominator")
     #plt.legend()
     #plt.savefig("week8_random/chi.jpg")
     return sum-ell+2

totalxe=[]
totalz=[]

while(suc<num_pair):
    zs=z_start+(z_end-z_start)*np.random.rand(num_point)
    zs=np.sort(zs)
    xes=xe_start+(xe_end-xe_start)*np.random.rand(num_point)
    write_ps(zs,xes)
    os.system('./class check.ini')
    data1=np.loadtxt('output/check00_cl_lensed.dat')
    EE=data1[0:ell-2,1]
    chi2=calculate_chi2(EE,EE_fid,errors,ell)
    os.system('rm -rf output/check*dat')
    if chi2<np.sqrt(2*(ell-2)) and get_tau()>tau_threshold:
        record(zs,xes,totalz,totalxe)
        suc+=1

#=====test=========
'''
zs=[6,8,10]
xes=[1.08,0.2,0.9]
write_ps(zs,xes)
os.system('./class check.ini')
data1=np.loadtxt('output/check00_cl_lensed.dat')
EE=data1[0:ell-2,1]
chi2=calculate_chi2(EE,EE_fid,errors)
'''
np.save("week8_random/totalxe.npy",totalxe)
np.save("week8_random/totalz.npy",totalz)