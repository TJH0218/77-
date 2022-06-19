a = input("輸入值為:").split(",")
# a1 = [int(item) for item in a]
max = sorted(a,reverse=True)
min = sorted(a,reverse=False)

b = [str(integer) for integer in max]
c = [str(integer) for integer in min]

b1 = "".join(b)
c1 = "".join(c)


print("最大值數列與最小值數列差值為:",int(b1)-int(c1))

