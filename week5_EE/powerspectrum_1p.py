import os
import numpy as np
#=====input=======
p1_value=0.1
p1_sigma=0.0002821
p1_name="r"#input("p1_name ")

open1=input("any additional condition?")
open1=bool(int(open1))

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']
if open1==True:
    content.append(input("content ")+'\n')


k=0
for p in np.arange(float(p1_value-5*p1_sigma),float(p1_value+5*p1_sigma),float(p1_sigma/10.0)):
    with open(p1_name+'1_0_'+str(int(k/100))+'_.ini','w') as f:
        for i in range(len(content)):
            f.write(content[i])
        f.write(p1_name+'='+str(round(p,10))+'\n')
    os.system('./class '+p1_name+'1_0_'+str(int(k/100))+'_.ini')
    k+=1

os.system("rm -rf "+p1_name+"1*.ini")
