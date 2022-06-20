import math
a = input("輸入月租費形式及通話時間：").split(",")
b = map(int,a)
c = list(b)

if a[0]=="186":
    s=0.09*c[1]
    if s>=186*2:
        print("通話費為：",math.ceil(s*0.8))
    elif s>=186:
        print("通話費為：",math.ceil(s*0.9))
    else:
        print("通話費為：",186)
elif a[0]=="386":
    s=0.08*c[1]
    if s>=386*2:
        print("通話費為：",math.ceil(s*0.7))
    elif s>=386:
        print("通話費為：",math.ceil(s*0.8))
    else:
        print("通話費為：",386)
elif a[0]=="586":
    s=0.07*a[1]
    if s>=586*2:
        print("通話費為：",math.ceil(s*0.6))
    elif s>=586:
        print("通話費為：",math.ceil(s*0.7))
    else:
        print("通話費為：",586)
else:
    s=0.06*a[1]
    if s>=986*2:
        print("通話費為：",math.ceil(s*0.5))
    elif s>=986:
        print("通話費為：",math.ceil(s*0.6))
    else:
        print("通話費為：",986)      