import os
import numpy as np
#=====input=======
z_start=input("z_start")
z_end=input("z_end")
z_step=input("z_step")
r_start=input("r_start")
r_end=input("r_end")
r_step=input("r_step")

content=['output=tCl,pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_mine\n','lensing=yes\n']

j=-1
for z_reio in np.arange(float(z_start),float(z_end),float(z_step)):
    j+=1
    for r in np.arange(float(r_start),float(r_end),float(r_step)):
        with open('chi_'+str(j)+'_.ini','w') as f:
            for i in range(len(content)):
                f.write(content[i])
            f.write('r='+str(round(r,5))+'\n')
            f.write('z_reio='+str(round(z_reio,5))+'\n')
        os.system('./class chi_'+str(j)+'_.ini')

os.system("rm -rf chi*.ini")
