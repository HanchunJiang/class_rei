import posterior as pt
import powerspectrum as ps
import random_num as rn
import numpy as np
import os

def get_points_from_npy(redshifts,xes,file_name="check.ini",root="output/check",p_name=["r"],p_value=[0.001]):
    points=[]
    for i in range(len(redshifts)):
        obj=rn.random_num(True,redshifts[i],xes[i],file_name=file_name,root=root,p_name=p_name,p_value=p_value)
        points.append(obj)
    return points

redshifts=np.load("week8_random/totalz.npy")
xes=np.load("week8_random/totalxe.npy")
#best_fit_before=np.load("result_24_02_08/middle/best_fit.npy")

points=get_points_from_npy(redshifts,xes,p_value=[0.01])
print("p_value=0.01")

best_fit_10=[]
best_fit_10_2002=[]
best_fit_2002=[]
#sigmas=[]
for i in range(len(points)):
    points[i].run()
    test=pt.post_search(ell_E=10,ell_B=10,fid_root="output/check00",p_start=[0.003,7],p_end=[0.011,11.5],p_step=[0.0005,0.2],verbose=False)#,ps_exist=True)
    test.draw_2D("result_24_02_15/middle/10/post"+str(i))
    print(test.best_fit)
    best_fit_10.append(test.best_fit)
    os.system("rm -rf output/chi*dat")
    test=pt.post_search(ell_E=2002,ell_B=10,fid_root="output/check00",p_start=[0.007,6.5],p_end=[0.016,10],p_step=[0.0005,0.2],verbose=False)#,ps_exist=True)
    #test=pt.post_sigma(ell=10,fid_root="output/check00",p_value=best_fit_before[i],p_sigma=[0.00003,0.2],steps=4,ranges=6,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_02_15/middle/10_2002/post"+str(i))
    #test.get_sigma(root="result_24_02_08/small/post"+str(i))
    print(test.best_fit)
    #print(test.p_sigma)
    best_fit_10_2002.append(test.best_fit)
    #os.system("rm -rf output/chi*dat")
    test=pt.post_search(ell_E=2002,ell_B=2002,fid_root="output/check00",p_start=[0.007,6.5],p_end=[0.016,10],p_step=[0.0005,0.2],verbose=False,ps_exist=True)
    test.draw_2D("result_24_02_15/middle/2002/post"+str(i))
    #sigmas.append(test.p_sigma)
    print(test.best_fit)
    best_fit_2002.append(test.best_fit)
    os.system("rm -rf output/ch*dat")

np.save('result_24_02_15/middle/10/best_fit.npy',np.array(best_fit_10))
np.save('result_24_02_15/middle/10_2002/best_fit.npy',np.array(best_fit_10_2002))
np.save('result_24_02_15/middle/2002/best_fit.npy',np.array(best_fit_2002))
#np.save('result_24_02_13/large/sigmas.npy',np.array(sigmas))