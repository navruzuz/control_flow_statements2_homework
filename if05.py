n=float(input("n ni kiriting::"))
x1=n%10
x2=(n%100)//10
x3=(n%1000)//100
x4=(n%10000)//1000
x5=n//10000
max=x1
if max<x3:
    max=x3
if max<x4:
    max=x4
if max<x5:
    max=x5
print(x1,x2,x3,x4,x5,max)
