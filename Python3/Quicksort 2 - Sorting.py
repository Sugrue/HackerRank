def quick_sort(left):
    if not len(left) > 1: return left
    pivot = left.pop()
    right = []
    equal = []
    output = ""
    i = 0
    while i < len(left):
        if left[i] == pivot: equal.append(left.pop(i))
        elif left[i] > pivot: right.append(left.pop(i))
        else: i += 1
    left = quick_sort(left)
    right = quick_sort(right)
    for item in left + equal + [pivot] + right: output += " " + str(item)
    print(output.strip())
    return left + equal + [pivot] + right
input()
array = []
output = ""
for item in input().split(): array.append(int(item))
quick_sort(array)