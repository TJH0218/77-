a = input("請選擇主餐及升級的套餐:")
b = input("是否升級成大杯飲料:")
c = input("是否換成大薯:")
s = 0
if "1" in a:
    s = s + 72
elif "2" in a:
    s = s + 62
elif "3" in a:
    s = s + 82
elif "4" in a:
    s = s + 44
elif "5" in a:
    s = s + 60

if "A" in a:
    s = s + 55
elif "B" in a:
    s = s + 68

if "是" in b:
    s = s + 7
else:
    s = s + 0

if "是" in c:
    s = s + 13
else:
    s = s + 0

print("總共為",s,"元")
