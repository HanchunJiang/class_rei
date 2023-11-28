import os
import numpy as np

#content=['output=pCl\n','modes=s,t\n','ic=ad\n','r=0.1\n','omega_b=0.030\n','z_reio=']
content=['output=pCl\n','modes=s,t\n','reio_parametrization=reio_mine\n']

for z_reio in np.arange(5,31,1):
    for r in np.arange(0.05,0.8,0.05):
        with open('chi'+str(z_reio)+'.ini','w') as f:
            for i in range(len(content)):
                f.write(content[i])
            f.write('r='+str(round(r,3))+'\n')
            f.write('z_reio='+str(z_reio)+'\n')
        os.system('./class chi'+str(z_reio)+'.ini')
