import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


a= cv.imread("/Users/kaival/Desktop/Dispplay decoder/pixil-frame-0.png")
binary_list=[]

plt.imshow(a)
plt.show()

#encryption

for i in range(28):
    for j in range(28):
        for k in range(3): 
            bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)]))
            #print(bin8(a[i][j][k]))
            binary_list.append(bin8(a[i][j][k]))


binary_list=pd.DataFrame(binary_list)
binary_list=binary_list.values.reshape(28,28,3)
values_list=[]

binary_list=binary_list.reshape(56,42)
print(binary_list)
oi_list=[]

for i in binary_list:
    for j in i:
        for k in j:
            oi_list.append(k)

oi_list=np.array(oi_list,dtype=int)
oi_list=oi_list.reshape(147,128)
print(oi_list)
plt.imshow(oi_list,cmap="Greys")
plt.show()




#decryption

back_list=oi_list
back_list=back_list.reshape(2352,8)

final_list=[]
jj=""
for i in back_list:
    for j in range(8):
        jj=jj+(str(i[j]))
    
    final_list.append(int(jj,2))
    jj=""

final_list=pd.DataFrame(final_list)
final_list=final_list.values.reshape(28,28,3)
print(final_list)
plt.imshow(final_list)
plt.show()