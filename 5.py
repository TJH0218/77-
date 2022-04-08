m = int(input("請輸入M:"))
t = n = 1
while n<m:
    n *= t
    t += 1
print("超過M為",m,"的最小階乘N值為:",t-1)
