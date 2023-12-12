import numpy as np
import matplotlib.pyplot as plt

#=========input==============#
p_start=float(input("p_start "))
p_end=float(input("p_end "))
p_step=float(input("p_step "))
p_name=input("p_name ")

chi2_BB=np.load("chi21_BB_"+p_name+".npy")

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

plt.plot(np.arange(p_start,p_end,p_step),N*post_BB)
plt.xlabel(p_name)
plt.ylabel("P("+p_name+")")
plt.savefig(p_name+"_chi2.jpg")
plt.show()
plt.cla()

plt.plot(np.arange(p_start,p_end,p_step),chi2_BB[0])
plt.xlabel(p_name)
plt.ylabel(r"$\chi^2$")
plt.savefig(p_name+"_chi2.jpg")
plt.show()
sigma2=0
R=np.arange(p_start,p_end,p_step)
for i in range(len(post_BB)):
    sigma2+=p_step*(R[i]-0.1)**2*post_BB[i]*N

print(np.sqrt(sigma2))


