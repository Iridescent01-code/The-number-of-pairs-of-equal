a = list(map(int, input().split()))
z = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            z += 1

print(z)