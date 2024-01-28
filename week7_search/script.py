import os
import numpy as np
import sys

#=====input=======
p1_start=0.0004
p1_end=0.0016
p1_step=0.0001
p1_name="r"
p2_start=7
p2_end=12
p2_step=0.1
p2_name="z_reio"

try:
    num=float(sys.argv[1])#到时候画图用的序号

except Exception as e:
    print("Input Error:", e)

open1=0#additional condition for powerspectrum

#==========Power Spectrum=======
os_str = 'python3 week7_search/powerspectrum_search.py '
for i in [p1_start,p1_end,p1_step,p1_name,p2_start,p2_end,p2_step,p2_name,open1]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()

print("======PS Finish======")

#=========chi2========
os_str = 'python3 week7_search/chi2_camb.py '
for i in [p1_start,p1_end,p1_step,p1_name,p2_start,p2_end,p2_step,p2_name]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
f.close()
print("======chi2 Finish======")

#=========draw chi2========
os_str = 'python3 week7_search/draw_chi.py '
for i in [p1_start,p1_end,p1_step,p1_name,p2_start,p2_end,p2_step,p2_name,num]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
print(res)
f.close()
print("======draw Finish======")

#========delete=========
os.system("rm -rf output/chi*dat")


