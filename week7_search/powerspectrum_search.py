import os
import numpy as np
import sys
#=====input=======
try:
    p1_start=float(sys.argv[1])
    p1_end=float(sys.argv[2])
    p1_step=float(sys.argv[3])
    p1_name=sys.argv[4]
    p2_start=float(sys.argv[5])
    p2_end=float(sys.argv[6])
    p2_step=float(sys.argv[7])
    p2_name=sys.argv[8]
    open1=bool(int(sys.argv[9]))
except Exception as e:
    print("Input Error:", e)

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
