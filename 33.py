a = []
a.append(int(input("國文：")))
a.append(int(input("英文：")))
a.append(int(input("微積分：")))
a.append(int(input("體育：")))
a.append(int(input("程式設計：")))
b = (a[0]+a[1]+a[2]+a[3]+a[4])/5

print("平均分數：",'%.2f'%b)

max = max(a[0],a[1],a[2],a[3],a[4])
min = min(a[0],a[1],a[2],a[3],a[4])

if max == a[0]:
    print("最高分科目：國文",max,"分")
elif max == a[1]:
    print("最高分科目：英文",max,"分")
elif max == a[2]:
    print("最高分科目：微積分",max,"分")
elif max == a[3]:
    print("最高分科目：體育",max,"分")
elif max == a[4]:
    print("最高分科目：程式設計",max,"分")

if min == a[0]:
    print("最高分科目：國文",min,"分")
elif min == a[1]:
    print("最高分科目：英文",min,"分")
elif min == a[2]:
    print("最高分科目：微積分",min,"分")
elif min == a[3]:
    print("最高分科目：體育",min,"分")
elif min == a[4]:
    print("最高分科目：程式設計",min,"分")
