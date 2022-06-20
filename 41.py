a = int(input("搭了幾次電梯："))
n = 1
s = 0

if 1<=a<=10:
    for i in range(a):
        b = int(input("樓層："))
        if b>n:
            s = s + (b-n)*20
        else:
            s = s + (n-b)*10
        n = b

print(s,"元")