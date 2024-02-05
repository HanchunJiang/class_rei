import os
import numpy as np
import sys

#=====input=======

try:
    num=float(sys.argv[1])#到时候画图用的序号
    p1_value=float(sys.argv[2])
    p2_value=float(sys.argv[3])

except Exception as e:
    print("Input Error:", e)

open1=0
p1_sigma=0.0001
p2_sigma=0.05
ranges=7
steps=4
p1_name="r"
p2_name="z_reio"

os_str = 'python3 week5_EE/powerspectrum_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges,open1]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()

print("======PS Finish======")

#=========chi2========
os_str = 'python3 week5_EE/chi2_camb.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges,'output/check00_cl_lensed.dat']:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()
print("======chi2 Finish======")

#=========sigma========
os.system("mkdir week8result")
os_str = 'python3 week5_EE/sigma.py '
for i in [p1_value,p1_sigma,p1_name,p2_value,p2_sigma,p2_name,steps,ranges,num]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
print(res)
f.close()

with open('result.txt','a') as f:
    f.write(str(res)+'\n')
    f.write("===sigma Finish===\n")
print("======sigma Finish======")

#========delete=========
os.system("rm -rf output/chi*dat")


