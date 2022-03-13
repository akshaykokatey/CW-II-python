#Check no. is Perfect square or not
import math
n=int(input('Enter the number:'))
root=math.sqrt(n)
if int (root+0.5)**2==n:
    print('Number is perfect square')
else:
    print("Number is not perfect square")    