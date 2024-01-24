import os
import numpy as np

#=====input=======
p1_start=0.0004
p1_end=0.0016
p1_step=0.00005
p1_name="r"
p2_start=7.5
p2_end=8.5
p2_step=0.05
p2_name="z_reio"

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
for i in [p1_start,p1_end,p1_step,p1_name,p2_start,p2_end,p2_step,p2_name]:
    os_str += str(i)+' '
f = os.popen(os_str, 'r')
res = f.readlines()
print(res)
f.close()
print("======draw Finish======")


