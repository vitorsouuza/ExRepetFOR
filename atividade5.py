import time

inspares = 0

for i in range(5,101):
    if i %7 ==0 and i %5 != 0:
     inspares += 1

     print(i)
print(' a quantidade é : ',inspares)



