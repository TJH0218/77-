a = input("請輸入一整數序列：").split()
a1 = list(map(int,a))
b = set(a1)
for i in b:
    if a1.count(i)>=len(a1)/2:
        print("過半元素為：",i)
        break
    else:
        print("過半元素為：","NO")
        break