a = input("輸入五張牌：").split()

for i in range(0,5):
    if a[i] == "A":
        a[i]="1"
    elif a[i] == "J":
        a[i]="11"
    elif a[i] == "Q":
        a[i]="12"
    elif a[i] == "K":
        a[i]="13"
    
b = [int(i) for i in a]
c = b[0]+b[1]+b[2]+b[3]+b[4]
print(c)
