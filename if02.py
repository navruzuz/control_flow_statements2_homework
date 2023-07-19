def main(a,b,c):
    if a>=0 and a<=9 and a<b and a<c:
        print('a eng kichik raqam')
    if b>=0 and b<=9 and b<a and b<c:
        print('b eng kichik raqam')
    if c>=0 and c<=9 and c<a and c<b:
        print('c eng kichik raqam')
print(main(7,25,2))