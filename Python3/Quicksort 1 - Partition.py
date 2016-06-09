# https://www.hackerrank.com/challenges/quicksort1

def quick_sort(left):
    if not len(left) > 1: return left
    pivot = left.pop(0)
    right = []
    equal = []
    i = 0
    while i < len(left):
        if left[i] == pivot: equal.append(left.pop(i))
        elif left[i] > pivot: right.append(left.pop(i))
        else: i += 1
    return left + equal + [pivot] + right
input()
array = []
output = ""
for item in input().split(): array.append(int(item))
for item in quick_sort(array): output += " " + str(item)
print(output)