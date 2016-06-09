# https://www.hackerrank.com/challenges/larrys-array

def solve(array):
    for i in range(len(array)):
        if array[i] > array[i+1]:
            for t in range(-2,1):
                temp = array
                for a in range(3):
                    if (i+t) > (len(array)-1) or (i+t) < 0:
                        continue
                    temp = rotate(temp,i+t)
                    if is_sorted(temp):
                        return "YES"
            return "NO"

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
def rotate(arr, i):
    if i + 2 < len(arr):
        a = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = arr[i+2]
        arr[i+2] = a
    #print("RETURN: " + str(arr))
    return arr

def solve_try2(array):
    larger = 0
    for i in range(len(array)):
        for t in range(i, len(array)):
            if int(array[i]) > int(array[t]):
                larger += 1

    if (larger % 2) == 0:
        return "YES"
    return "NO"




output = ""
for i in range(int(input())):
    input()
    output += str(solve_try2(input().split())) + '\n'
print(output)
