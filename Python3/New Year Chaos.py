# https://www.hackerrank.com/challenges/new-year-chaos

def solve(queue):
    bribe = [0]*len(queue)
    complete =  False
    while not complete:
        complete = True
        for i in range(len(queue)-1):
            if queue[i] > queue[i+1]:
                if bribe[queue[i] - 1] > 1:
                    return "Too chaotic"
                bribe[queue[i] - 1] += 1
                swap(i, i+1, queue)
                complete = False
    output = 0
    for i in bribe:
        output += i
    return output

def swap(x, y, array):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp



T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    print(solve(q))
