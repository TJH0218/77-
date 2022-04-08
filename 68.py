x1 = input("請輸入第一組數字:")
x2 = input("請輸入第二組數字:")
a=0
b=0

for i in x1:
    for j in x2 :
        if x1.index(i)==x2.index(j) and i==j:
            a+=1
        elif i==j :
            b+=1

if a == 4:
    print(a,"A",b,"B","全對")
else:
    print(a,"A",b,"B","加油")
