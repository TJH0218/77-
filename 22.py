a = int(input("輸入查詢組數N為："))

c =[]
for i in range(a):
    c.append(input("帳號、密碼：").split())
    
for j in range(a):
    if c[j][0] == "123":
        if c[j][1] == "456":
            print("9000")
        else:
            print("error")
    elif c[j][0] == "456":
        if c[j][1] == "789":
            print("5000")
        else:
            print("error")
    elif c[j][0] == "789":
        if c[j][1] == "888":
            print("6000")
        else:
            print("error")
    elif c[j][0] == "336":
        if c[j][1] == "558":
            print("10000")
        else:
            print("error")
    elif c[j][0] == "775":
        if c[j][1] == "666":
            print("12000")
        else:
            print("error")
    elif c[j][0] == "566":
        if c[j][1] == "221":
            print("7000")
        else:
            print("error")
    else:
        print("error")
