import os
import numpy as np
#=====input=======
p_start=input("p_start ")
p_end=input("p_end ")
p_step=input("p_step ")
p_name=input("p_name ")
open1=bool(input("any additional condition?"))

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']
if open1==True:
    content.append(input("content ")+'\n')


k=0
for p in np.arange(float(p_start),float(p_end),float(p_step)):
    with open(p_name+'1_0_'+str(int(k/100))+'_.ini','w') as f:
        for i in range(len(content)):
            f.write(content[i])
        f.write(p_name+'='+str(round(p,10))+'\n')
    os.system('./class '+p_name+'1_0_'+str(int(k/100))+'_.ini')
    k+=1

os.system("rm -rf "+p_name+"1*.ini")
