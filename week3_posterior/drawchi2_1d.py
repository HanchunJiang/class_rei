import numpy as np
import matplotlib.pyplot as plt

#=========input==============#
chi2_EE=np.load("chi21_EE.npy")
chi2_BB=np.load("chi21_BB.npy")

r_start=0.01
r_end=0.26
r_step=0.01

#=======functions============#
def posterior(chi2):
    #post=np.zeros((chi2.shape[0],chi2.shape[1]))
    post=np.zeros(len(chi2))
    for i in range(len(chi2)):
        post[i]=np.exp(-0.5*chi2[i])
    print(post)
    return post

plt.plot(np.arange(r_start,r_end,r_step),chi2_BB[0])
plt.show()

#====standard deviation=========#
print(np.std(chi2_BB[0]))

