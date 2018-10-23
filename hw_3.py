#functions and modules
#Yijia Zhao
import math
import random

def is_divisible(m,n):
    return(m%n==0)

print(is_divisible(6,3))

def not_equal(a,b):
    if (a==b):
        return(False)
    else:
        return(True)

print(not_equal(1,2))

radians = (90.0 / 360.0) * 2 * math.pi
print (math.sin(radians))

def multadd(a,b,c):
    return(a*b+c)

print(multadd(2,4,3))
print(multadd(math.cos(math.pi/4),1/2,math.sin(math.pi/4)))
print((multadd(2,math.log(12)/math.log(7),math.ceil(276/19))))

def rand_divis_3():
    a = random.randint(0,100)
    print(a)
    return(a%3==0)

print(rand_divis_3())
