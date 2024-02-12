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
best_fit_before=np.load("result_24_02_08/middle/best_fit.npy")

points=get_points_from_npy(redshifts,xes)

best_fit=[]
sigmas=[]
for i in range(len(points)):
    points[i].run()
    #test=pt.post_search(ell=10,fid_root="output/check00",p_start=[0.0001,8],p_end=[0.0016,12],p_step=[0.00005,0.2],verbose=False)
    test=pt.post_sigma(ell=10,fid_root="output/check00",p_value=best_fit_before[i],p_sigma=[0.00003,0.2],steps=4,ranges=6,verbose=False)#,ps_exsit=True)
    test.draw_2D("result_24_02_08/small/post"+str(i))
    test.get_sigma(root="result_24_02_08/small/post"+str(i))
    print(test.best_fit)
    print(test.p_sigma)
    best_fit.append(test.best_fit)
    sigmas.append(test.p_sigma)
    os.system("rm -rf output/ch*dat")

np.save('result_24_02_08/small/best_fit.npy',np.array(best_fit))
np.save('result_24_02_08/small/sigmas.npy',np.array(sigmas))