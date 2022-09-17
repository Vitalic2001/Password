num = int(input())
sum1 = 0
sum2 = 0
mar =[input().split() for _ in range(num)]
for i in range(num):
    for j in range(num):
        sum1 += int(mar[i][j])
        sum1 += int(mar[j][i])
        if mar[i].count(mar[j][i]) > 2:
            sum1 += 4444
            print(sum1)
        if i == j:
            sum2 += int(mar[i][j])
if sum1/(num*2) == sum2:
    print("YES")
else:
    print("NO")


