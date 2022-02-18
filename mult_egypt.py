def mult_egypt(a,b):
    x = a
    y = b
    z = 0
    while x!= 0:
        if x % 2 == 1:
            z = z+y
        x = x//2
        y = y+y
    print(z)



a=int(input())
b=int(input())
mult_egypt(a,b)