# def main(a,b,c):
    
    # if a>b and a>c:

    #     print('a raqami eng katta')
    # if b>a and b>c:
    #     print('b raqami eng katta')
    # if c>a and c>b:
    #     print('c raqami eng katta')
    # if a>=0 and a<=9 and a<b and a<c:
    #     print('a eng kichik raqam')
    # if b>=0 and b<=9 and b<a and b<c:
    #     print('b eng kichik raqam')
    # if c>=0 and c<=9 and c<a and c<b:
    #     print('c eng kichik raqam')
a=float(input("a ni kiriting::"))
b=float(input("b ni kiriting::"))
c=float(input("c ni kiriting::"))
max=a
if   max<b :
    max=b
if max<c:
    max=c
# return max
min=a
if  min>b :
    min=b
if min>c:
    min=c
# return min
print(max,min,(max+min)/2)
