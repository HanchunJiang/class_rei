import posterior as pt
import powerspectrum as ps
import numpy as np
import os

print("p_value=0.001 and 0.01")

#best_fit_10=[]
best_fit_10_2002=[]
best_fit_2002=[]
sigmas_10=[]
sigmas_10_2002=[]
sigmas_2002=[]

#best_fit_before_10=np.load("result_24_03_06/middle/10/best_fit.npy")
best_fit_before_10_2002=np.load("result_24_03_06/middle/10_2002/best_fit.npy")
best_fit_before_2002=np.load("result_24_03_06/middle/2002/best_fit.npy")

i=0
for r in [0.001,0.01]:
    ps.write_ps("check",["r","z_reio"],[r,8.5],"reio_mine")
    os.system("./class check.ini")

    #这一部分不用重跑了
    '''
    test=pt.post_sigma(ell_E=10,ell_B=10,fid_root="output/check00",p_value=best_fit_before_10[i],p_sigma=[best_fit_before_10[i][0]/10/2,best_fit_before_10[i][1]/10/10],steps=5,ranges=7,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_03_06/small/10/post_r_"+str(r))
    test.get_sigma(root="result_24_03_06/small/10/post_r_"+str(r))
    best_fit_10.append(test.best_fit)
    sigmas_10.append(test.p_sigma)
    print(test.best_fit)
    print(test.p_sigma)
    os.system("rm -rf output/chi*dat")
    '''

    test=pt.post_sigma(ell_E=2002,ell_B=10,fid_root="output/check00",p_value=best_fit_before_10_2002[i],p_sigma=[best_fit_before_10_2002[i][0]/10/2,0.04],steps=5,ranges=7,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_03_06/small/10_2002/post_r_"+str(r))
    test.get_sigma(root="result_24_03_06/small/10_2002/post_r_"+str(r))
    best_fit_10_2002.append(test.best_fit)
    sigmas_10_2002.append(test.p_sigma)
    print(test.best_fit)
    print(test.p_sigma)
    os.system("rm -rf output/chi*dat")

    p_sigma_temp=[best_fit_before_2002[i][0]/10/2,0.04]
    if r==0.001:
        p_sigma_temp=[best_fit_before_2002[i][0]/10/2/2,0.04]
    test=pt.post_sigma(ell_E=2002,ell_B=2002,fid_root="output/check00",p_value=best_fit_before_2002[i],p_sigma=p_sigma_temp,steps=5,ranges=7,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_03_06/small/2002/post_r_"+str(r))
    test.get_sigma(root="result_24_03_06/small/2002/post_r_"+str(r))
    best_fit_2002.append(test.best_fit)
    sigmas_2002.append(test.p_sigma)
    print(test.best_fit)
    print(test.p_sigma)
    os.system("rm -rf output/ch*dat")

    i+=1

#np.save('result_24_03_06/small/10/best_fit.npy',np.array(best_fit_10))
np.save('result_24_03_06/small/10_2002/best_fit.npy',np.array(best_fit_10_2002))
np.save('result_24_03_06/small/2002/best_fit.npy',np.array(best_fit_2002))

#np.save('result_24_03_06/small/10/sigmas.npy',np.array(sigmas_10))
np.save('result_24_03_06/small/10_2002/sigmas.npy',np.array(sigmas_10_2002))
np.save('result_24_03_06/small/2002/sigmas.npy',np.array(sigmas_2002))