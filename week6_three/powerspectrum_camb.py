import os
import numpy as np
import sys
#=====input=======
try:
    p1_value=float(sys.argv[1])
    p1_sigma=float(sys.argv[2])
    p1_name=sys.argv[3]
    p2_value=float(sys.argv[4])
    p2_sigma=float(sys.argv[5])
    p2_name=sys.argv[6]
    p3_value=float(sys.argv[7])
    p3_sigma=float(sys.argv[8])
    p3_name=sys.argv[9]
    steps=float(sys.argv[10])
    ranges=float(sys.argv[11])
    open1=bool(int(sys.argv[12]))
except Exception as e:
    print("Input Error:", e)

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']

if open1==True:
    temp=input("content ")
    content.append(temp+'\n')

k=-1
for p1 in np.arange(float(p1_value-ranges*p1_sigma),float(p1_value+ranges*p1_sigma),float(p1_sigma/steps)):
    k+=1
    j=-1
    for p2 in np.arange(float(p2_value-ranges*p2_sigma),float(p2_value+ranges*p2_sigma),float(p2_sigma/steps)):
        j+=1
        p=0
        for p3 in np.arange(float(p3_value-ranges*p3_sigma),float(p3_value+ranges*p3_sigma),float(p3_sigma/steps)):
            with open('chi1_'+str(k)+'_'+str(j)+'_'+str(int(p/100))+'_.ini','w') as f:
                for i in range(len(content)):
                    f.write(content[i])
                f.write(p1_name+'='+str(round(p1,10))+'\n')
                f.write(p2_name+'='+str(round(p2,10))+'\n')
                f.write(p3_name+'='+str(round(p3,10))+'\n')
            os.system('./class chi1_'+str(k)+'_'+str(j)+'_'+str(int(p/100))+'_.ini')
            p+=1

os.system("rm -rf chi1*.ini")
