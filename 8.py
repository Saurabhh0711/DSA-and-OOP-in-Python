n = int(input())
a = list(map(int,input().split()))
max = -1
b = 0
for i in range(n):
    if a[i]>max:
        max = a[i]
        b = i
print("The biggest number is",max)
print("The position is",b)

