n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
max = sum
for i in range (n):
    sum = sum + a[i] - b[i]
    if max < sum:
        max = sum
print(max)