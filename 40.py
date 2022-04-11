n = int(input("輸入整數n:"))

for i in range(1,n,2):
    print(end="    ")
    print(i)
for k in range(1,n+1,2):
    print(k,end="")
for k in range(n-2,0,-2):
    print(k,end="")
print()
for j in range(n-2,0,-2):
    print(end="    ")
    print(j)
