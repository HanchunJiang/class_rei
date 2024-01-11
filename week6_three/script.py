import os
import numpy as np

#=====input=======
p1_value=0.001
p1_name="r"
p2_value=0.5
p2_name="reionization_width"
p3_value=0.0561
p3_name="tau_reio"

steps=4 #sigma/step
ranges=3 #range*step

delta1=0.000005
delta2=0.0001
delta3=0.0005

open1=0#additional condition for powerspectrum

#======power spectrum for fisher==========
content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_camb\n','lensing=yes\n']

#Fiducial
with open('reio_camb.ini','w') as f:
    for i in range(len(content)):
        f.write(content[i])
    f.write(p1_name+'='+str(round(p1_value,10))+'\n')
    f.write(p2_name+'='+str(round(p2_value,10))+'\n')
    f.write(p3_name+'='+str(round(p3_value,10))+'\n')
os.system('./class reio_camb.ini')

#others
for p1,p2,p3 in [(p1_value+delta1,p2_value,p3_value),(p1_value-delta1,p2_value,p3_value),(p1_value,p2_value+delta2,p3_value),(p1_value,p2_value-delta2,p3_value),(p1_value,p2_value,p3_value+delta3),(p1_value,p2_value,p3_value-delta3)]:
    with open('reio_camb.ini','w') as f:
        for i in range(len(content)):
            f.write(content[i])
        f.write(p1_name+'='+str(round(p1,10))+'\n')
        f.write(p2_name+'='+str(round(p2,10))+'\n')
        f.write(p3_name+'='+str(round(p3,10))+'\n')
    os.system('./class reio_camb.ini')

os.system("mv output/reio_camb*dat .")
os.system("rm -rf reio_camb*t.dat")
os.system("rm -rf reio_camb*s.dat")
os.system("rm -rf reio_camb*l.dat")

#===========Fisher=============
os_str = 'python3 week6_three/fisherEEn.py '
for i in [p1_value,p2_value,p3_value,delta1,delta2,delta3]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
f.close()

with open('result.txt','w') as f:
    f.write(str(res)+'\n')
    f.write("===Fisher Finish===\n")

print("======Fisher Finish======")
#==========Power Spectrum=======
p1_sigma=float(res[0])
p2_sigma=float(res[1])
p3_sigma=float(res[2])

os_str = 'python3 week6_three/powerspectrum_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,p3_value,p3_sigma,p3_name,steps,ranges,open1]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()

print("======PS Finish======")

#=========chi2========
os_str = 'python3 week6_three/chi2_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,p3_value,p3_sigma,p3_name,steps,ranges]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()
print("======chi2 Finish======")

#=========sigma========
os.system("mkdir week6_result")
os_str = 'python3 week6_three/sigma.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,p3_value,p3_sigma,p3_name,steps,ranges]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
print(res)
f.close()

with open('result.txt','a') as f:
    f.write(str(res)+'\n')
    f.write("===sigma Finish===\n")
print("======sigma Finish======")


