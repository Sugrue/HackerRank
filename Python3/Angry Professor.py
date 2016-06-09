# https://www.hackerrank.com/challenges/angry-professor

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    ontime = 0
    for t in a:
        if t <= 0:
            ontime += 1
    if ontime >= k:
        print("NO")
        continue
    print("YES")