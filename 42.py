a = int(input("輸入a值:"))
b = int(input("輸入b值:"))
c = int(input("輸入c值:"))
p = (b*b)-(4*a*c)
x1 = (-b+ p**0.5)/(2*a)
x2 = (-b- p**0.5)/(2*a)
if p<0:
    print(0)
elif p==0:
    print(x1)
else:
    print(x1)
    print(x2)
