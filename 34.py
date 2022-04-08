a = int(input("輸入一正整數:"))

if a%2==0 and a%11==0 and a%5!=0 and a%7!=0:
    print(a,"為新公倍數? : Yes")
else:
    print(a,"為新公倍數? : No")
