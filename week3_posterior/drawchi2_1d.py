import numpy as np
import matplotlib.pyplot as plt

#=========input==============#
#chi2_EE=np.load("chi21_EE.npy")
chi2_BB=np.load("chi21_BB.npy")

r_start=0.07
r_end=0.13
r_step=0.000001

#=======functions============#
def posterior(chi2):
    #post=np.zeros((chi2.shape[0],chi2.shape[1]))
    post=np.zeros(len(chi2))
    for i in range(len(chi2)):
        post[i]=np.exp(-0.5*chi2[i])
    print(post)
    return post

#plt.plot(np.arange(r_start,r_end,r_step),posterior(chi2_BB[0]))
#plt.show()

#==========sigma=============#
post_BB=posterior(chi2_BB[0])
sum=0
for i in range(len(post_BB)):
    sum+=post_BB[i]

print(sum)
N=1/sum
print(N)

plt.plot(np.arange(r_start,r_end,r_step),N*post_BB)
plt.xlabel("r")
plt.ylabel("P(r)")
plt.show()
sigma2=0
R=np.arange(r_start,r_end,r_step)
for i in range(len(post_BB)):
    sigma2+=r_step*(R[i]-0.1)**2*post_BB[i]*N

print(np.sqrt(sigma2))


