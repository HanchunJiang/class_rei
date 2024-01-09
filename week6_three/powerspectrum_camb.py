import os
import numpy as np
#=====input=======
p1_value=0.001
p1_sigma=0.0001806
p1_name="r"#input("p1_name ")
p2_value=0.5
p2_sigma=0.1316
p2_name="reionization_width"#input("p2_name ")
p3_value=0.0561
p3_sigma=0.0003851
p3_name="tau_reio"#input("p3_name ")


open1=input("any additional condition?")
open1=bool(int(open1))

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']

if open1==True:
    temp=input("content ")
    content.append(temp+'\n')

k=-1
for p1 in np.arange(float(p1_value-3*p1_sigma),float(p1_value+3*p1_sigma),float(p1_sigma/4.0)):
    k+=1
    j=-1
    for p2 in np.arange(float(p2_value-3*p2_sigma),float(p2_value+3*p2_sigma),float(p2_sigma/4.0)):
        j+=1
        p=0
        for p3 in np.arange(float(p3_value-3*p3_sigma),float(p3_value+3*p3_sigma),float(p3_sigma/4.0)):
            with open('chi1_'+str(k)+'_'+str(j)+'_'+str(int(p/100))+'_.ini','w') as f:
                for i in range(len(content)):
                    f.write(content[i])
                f.write(p1_name+'='+str(round(p1,10))+'\n')
                f.write(p2_name+'='+str(round(p2,10))+'\n')
                f.write(p3_name+'='+str(round(p3,10))+'\n')
            os.system('./class chi1_'+str(k)+'_'+str(j)+'_'+str(int(p/100))+'_.ini')
            p+=1

os.system("rm -rf chi1*.ini")
