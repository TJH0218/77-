a = int(input("輸入第一行正整數為:"))
b = input("第二行中數列中的數字為:").split()
b1 = list(map(int,b))

s = 0
if a==len(b1):
    for i in range(0,a):
        if b1[i]==b1[i+1]