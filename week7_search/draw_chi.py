import numpy as np
import matplotlib.pyplot as plt
import sys

chi2=np.load("week7_search/chi21_Wishert.npy")

try:
    p1_start=float(sys.argv[1])
    p1_end=float(sys.argv[2])
    p1_step=float(sys.argv[3])
    p1_name=sys.argv[4]
    p2_start=float(sys.argv[5])
    p2_end=float(sys.argv[6])
    p2_step=float(sys.argv[7])
    p2_name=sys.argv[8]

except Exception as e:
    print("Input Error:", e)

ranges=8
steps=5

min_i=0
min_j=0
min_chi=1e6

for i in range(chi2.shape[0]):
    for j in range(chi2.shape[1]):
        if chi2[i,j]<min_chi:
            min_chi=chi2[i,j]
            min_i=i
            min_j=j

print(np.arange(p1_start,p1_end,p1_step)[min_i])
print(np.arange(p2_start,p2_end,p2_step)[min_j])

fig = plt.figure()
ay=fig.add_subplot()
X,Y = np.meshgrid(np.arange(float(p2_start),float(p2_end),float(p2_step)),np.arange(float(p1_start),float(p1_end),float(p1_step)))
contour=ay.contourf(X,Y,chi2)#,colors=['blue','lightsteelblue','white'])
ay.set_xlabel(p2_name)
ay.set_ylabel(p1_name)
fig.colorbar(contour)
plt.savefig("week7_search/chi_2D.jpg")
plt.show()
