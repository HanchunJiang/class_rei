import os
import numpy as np

#=====input=======
p1_value=0.001
p1_name="r"
p2_value=7.7
p2_name="z_reio"

steps=10 #sigma/step
ranges=5 #range*step

delta1=0.000005
delta2=0.0001

open1=0#additional condition for powerspectrum

#======power spectrum for fisher==========
content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_mine\n','lensing=yes\n','thermodynamics_verbose=3\n']

#Fiducial
with open('reio_mine.ini','w') as f:
    for i in range(len(content)):
        f.write(content[i])
    f.write(p1_name+'='+str(round(p1_value,10))+'\n')
    f.write(p2_name+'='+str(round(p2_value,10))+'\n')
os.system('./class reio_mine.ini')

#others
for p1,p2 in [(p1_value+delta1,p2_value),(p1_value-delta1,p2_value),(p1_value,p2_value+delta2),(p1_value,p2_value-delta2)]:
    with open('reio_mine.ini','w') as f:
        for i in range(len(content)):
            f.write(content[i])
        f.write(p1_name+'='+str(round(p1,10))+'\n')
        f.write(p2_name+'='+str(round(p2,10))+'\n')
    os.system('./class reio_mine.ini')

os.system("mv output/reio_mine*dat .")
os.system("rm -rf reio_mine*t.dat")
os.system("rm -rf reio_mine*s.dat")
os.system("rm -rf reio_mine*l.dat")

#===========Fisher=============
os_str = 'python3 week5_EE/fisherEE.py '
for i in [p1_value,p2_value,delta1,delta2]:
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

p1_value=0.001
p2_value=8.15

os_str = 'python3 week5_EE/powerspectrum_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges,open1]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()

print("======PS Finish======")

#=========chi2========
os_str = 'python3 week5_EE/chi2_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges,'reio_mine00_cl_lensed.dat']:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()
print("======chi2 Finish======")

#=========sigma========
os.system("mkdir week5result")
os_str = 'python3 week5_EE/sigma.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
print(res)
f.close()

with open('result.txt','a') as f:
    f.write(str(res)+'\n')
    f.write("===sigma Finish===\n")
print("======sigma Finish======")


