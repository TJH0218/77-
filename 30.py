ans = input("輸入答案:")
q = input("輸入4位數字:")
a=0
b=0
if q == "0000":
    print(" ")
else:
    for i in q:
        for j in ans :
            if q.index(i)==ans.index(j) and i==j:
                a+=1
            elif i==j :
                b+=1
    print(a,"A",b,"B")
