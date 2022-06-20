a = int(input("n個地方："))
b = []

if 2<=a<=10:
    for i in range(a):
        b.append(int(input("距離幾公里：")))
    
for j in range(a):
    if b[j]%9==0 or b[j]%11==0:
        if 1<=b[j]<=1000:
            print("第",j+1,"個點",b[j])
