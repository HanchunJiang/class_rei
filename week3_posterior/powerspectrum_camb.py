import os
import numpy as np
#=====input=======
p1_start=0.07#input("p1_start ")
p1_end=0.15#input("p1_end ")
p1_step=0.01#input("p1_step ")
p1_name="r"#input("p1_name ")
p2_start=0.3#input("p2_start ")
p2_end=0.7#input("p2_end ")
p2_step=0.01#input("p2_step ")
p2_name="reionization_width"#input("p2_name ")

open1=input("any additional condition?")
open1=bool(int(open1))

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']

if open1==True:
    temp=input("content ")
    content.append(temp+'\n')

j=-1
for p1 in np.arange(float(p1_start),float(p1_end),float(p1_step)):
    j+=1
    p=0
    for p2 in np.arange(float(p2_start),float(p2_end),float(p2_step)):
        with open('chi1_'+str(j)+'_'+str(int(p/100))+'_.ini','w') as f:
            for i in range(len(content)):
                f.write(content[i])
            f.write(p1_name+'='+str(round(p1,10))+'\n')
            f.write(p2_name+'='+str(round(p2,10))+'\n')
        os.system('./class chi1_'+str(j)+'_'+str(int(p/100))+'_.ini')
        p+=1

os.system("rm -rf chi1*.ini")
