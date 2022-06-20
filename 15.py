a = input("輸入一個四位數字：")
b = []
for i in range(len(a)):
    s = (int(a[i])+7)%10
    b.append(s)
    
t1 = b[0]
b[0] = b[2]
b[2] = t1

t2 = b[1]
b[1] = b[3]
b[3] = t2

b1 = map(str,b)
c = str(''.join(b1))

print("輸出加密後的數字為：",c)