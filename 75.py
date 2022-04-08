s = 0
while s>=0:
    a = input("請輸入事項(若以無事項，請輸入end):")
    s+=1
    if a=="end":
        break
    else:
        print(s,".",a)
    