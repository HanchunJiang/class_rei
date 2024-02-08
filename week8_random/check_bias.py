import numpy as np
import os

total_xe=np.load("week8_random/totalxe.npy")
total_z=np.load("week8_random/totalz.npy")
best_fit1=np.loadtxt("week8result/best_fit1.txt")

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
j=0
for i in range(len(total_xe)):
    write_ps(total_z[i],total_xe[i])
    os.system('./class check.ini')#生成fiducial model

    #os.system('python3 week7_search/script.py '+str(i))
    os_str='python3 week8_random/script.py '
    os_str+=str(i)
    os_str+=" "
    os_str+=str(best_fit1[j])
    os_str+=" "
    j+=1
    os_str+=str(best_fit1[j])
    j+=1
    os.system(os_str)
    
    os.system("rm -rf output/check*dat")


