import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def factors(n):    
    val = math.ceil(math.sqrt(n))
    val2 = int(n/val)
    while val2 * val != float(n):
        val -= 1
        val2 = int(n/val)
    return val, val2

a= cv.imread("/Users/kaival/Desktop/Dispplay decoder/download (2).jpeg")
binary_list=[]
print(a.shape)
a_shape=a.shape

image_height=a_shape[0]
image_width=a_shape[1]
image_dimension=a_shape[2]


plt.imshow(a)
plt.show()

#encryption

for i in range(image_height):
    for j in range(image_width):
        for k in range(image_dimension): 
            bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)]))
            #print(bin8(a[i][j][k]))
            binary_list.append(bin8(a[i][j][k]))


binary_list=pd.DataFrame(binary_list)
binary_list=binary_list.values.reshape(image_height,image_width,image_dimension)
values_list=[]

print(binary_list.shape)
f_1,f_2=factors(image_height*image_width*image_dimension)

print(f_1,f_2)
binary_list=binary_list.reshape(f_1,f_2)
oi_list=[]

for i in binary_list:
    for j in i:
        for k in j:
            oi_list.append(k)

oi_list=np.array(oi_list,dtype=int)
print(oi_list.shape)

enc_shape=oi_list.shape[0]
enc_f_1,enc_f_2=factors(enc_shape)

print(enc_f_1,enc_f_2)
oi_list=oi_list.reshape(enc_f_1,enc_f_2)
print(oi_list)
plt.imshow(oi_list,cmap="Greys")
plt.show()



#decryption

back_list=oi_list
a_1=oi_list.shape[0]
a_2=oi_list.shape[1]

back_list=back_list.reshape(int((a_1*a_2)/8),8)

final_list=[]
jj=""
for i in back_list:
    for j in range(8):
        jj=jj+(str(i[j]))
    
    final_list.append(int(jj,2))
    jj=""

final_list=pd.DataFrame(final_list)
print(final_list.shape)
b_1=final_list.shape[0]
f_dec_1,f_dec_2=factors(b_1/3)
print(b_1)
print(f_dec_1,f_dec_2)
final_list=final_list.values.reshape(f_dec_1,f_dec_2,3)
print(final_list)
plt.imshow(final_list)
plt.show()





