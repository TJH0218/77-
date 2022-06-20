a = int(input("小明身上有幾元："))
b = int(input("販賣機有幾種飲料："))

c = []
s = 0
for i in range(b):
    c.append(int(input("飲料價錢：")))
    if c[i]<=a:
        s+=1
    else:
        s+=0
        
print(s)    