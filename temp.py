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

points=get_points_from_npy(redshifts,xes)

best_fit=[]
for i in range(len(points)):
    points[i].run()
    test=pt.post_search(ell=10,fid_root="output/check00",p_start=[0.0004,5],p_end=[0.0016,15],p_step=[0.0001,0.5],verbose=False)
    test.draw_2D("result_24_02_08/large/post"+str(i))
    print(test.best_fit)
    best_fit.append(test.best_fit)
    os.system("rm -rf output/ch*dat")

np.save('result_24_02_08/large/best_fit.npy',np.array(best_fit))