import posterior as pt
import powerspectrum as ps
import numpy as np
import os

print("p_value=0.001 and 0.01")

best_fit_10=[]
best_fit_10_2002=[]
best_fit_2002=[]

for r in [0.001,0.01]:
    ps.write_ps("check",["r","z_reio"],[r,8.5],"reio_mine")
    os.system("./class check.ini")
    test=pt.post_search(ell_E=10,ell_B=10,fid_root="output/check00",p_start=[r-5*r/10,8],p_end=[r+5*r/10,10],p_step=[r/10/5,0.1],verbose=False)#,ps_exist=True)
    test.draw_2D("result_24_03_06/middle/10/post_r_"+str(r))
    print(test.best_fit)
    best_fit_10.append(test.best_fit)
    #os.system("rm -rf output/chi*dat")
    test=pt.post_search(ell_E=2002,ell_B=10,fid_root="output/check00",p_start=[r-5*r/10,8],p_end=[r+5*r/10,10],p_step=[r/10/5,0.1],verbose=False,ps_exist=True)
    #test=pt.post_sigma(ell=10,fid_root="output/check00",p_value=best_fit_before[i],p_sigma=[0.00003,0.2],steps=4,ranges=6,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_03_06/middle/10_2002/post_r_"+str(r))
    #test.get_sigma(root="result_24_02_08/small/post"+str(i))
    print(test.best_fit)
    #print(test.p_sigma)
    best_fit_10_2002.append(test.best_fit)
    #os.system("rm -rf output/chi*dat")
    test=pt.post_search(ell_E=2002,ell_B=2002,fid_root="output/check00",p_start=[r-5*r/10,8],p_end=[r+5*r/10,10],p_step=[r/10/5,0.1],verbose=False,ps_exist=True)
    test.draw_2D("result_24_03_06/middle/2002/post_r_"+str(r))
    #sigmas.append(test.p_sigma)
    print(test.best_fit)
    best_fit_2002.append(test.best_fit)
    os.system("rm -rf output/ch*dat")

np.save('result_24_03_06/middle/10/best_fit.npy',np.array(best_fit_10))
np.save('result_24_03_06/middle/10_2002/best_fit.npy',np.array(best_fit_10_2002))
np.save('result_24_03_06/middle/2002/best_fit.npy',np.array(best_fit_2002))
#np.save('result_24_02_13/large/sigmas.npy',np.array(sigmas))