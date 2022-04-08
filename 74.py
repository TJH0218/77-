a = ['red','blue','red','green']
b = input("依序輸入四個顏色:").split()
s = ""
if a == b:
    print("正確答案")
else:
    for i in range(4):
        if a[i]==b[i]:
            s+= "1"
        elif b[i] in a:
            s+= "2"
        else:
            s+= "3"
    print(s)
