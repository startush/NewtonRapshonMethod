from sympy import*
import numpy as np
import matplotlib.pyplot as plt 
x=Symbol('x')
f=x**3-x*2-5
# this is sympy expression
f_prime = f.diff(x)
f=lambdify(x,f)
f_prime=lambdify(x,f_prime)
# f_prime(2)
x=input("enter the value of x:" )
n = input("enter the required correct decimal place:")
x=float(x)
n=int(n)
# newton Rapshon 
# number of iteration untill we get correct decimal place 
condition = True
i=1
while condition:
    g=str(x)
    x_n = x-(f(x)/(f_prime(x)))
    print("i=",i,"x=",x,"f(x)=",f(x))
    m = str(x_n)
#     if up to 3 decimal  place we are getting correct value
    if m[0:n+2]==g[0:n+2]:
        condition=False
    else:
        condition = True
        x=x_n
        i=i+1
x=str(x)
s=x[0:n+2]
print("Required root is", s)
m=np.linspace(-3,3,100)
y=f(m)
plt.plot(m,y)
