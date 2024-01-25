import numpy as np
import os

total_xe=np.load("totalxe.npy")
total_z=np.load("totalz.npy")

content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_many_tanh\n','lensing=yes\n','thermodynamics_verbose=4\n']

def write_ps(zs,xes):
    with open('check.ini','w') as f:
            for i in range(len(content)):
                f.write(content[i])
            f.write("many_tanh_num=")
            f.write(str(int(len(zs)))+"\n")
            f.write("many_tanh_z=")
            for i in zs:
                 f.write(str(round(i,10))+",")
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.write("\n")
            f.write("many_tanh_xe=")
            for i in xes:
                 f.write(str(round(i,10))+",")
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.write("\n")

for i in range(len(total_xe)):
    write_ps(total_z[i],total_xe[i])
    os.system('../class check.ini')


