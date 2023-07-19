def main(a,b):
    max=a
    if max<b:
        max=b
    if a==b:
        return 0
    else:
        return max
print(main(3,3))