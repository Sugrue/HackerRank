def solve(grid, pattern):
    for r in range(len(grid)-(len(pattern)-1)):
        for c in range(len(grid[0])-(len(pattern[0])-1)):
            if grid[r][c] == pattern[0][0]:
                pr = 0
                pc = 0
            
                while grid[r+pr][c+pc] == pattern[pr][pc]:
                    #print("PATTERN: " + str(pr) + "," + str(pc) + " = " + pattern[pr][pc])
                    #print("GRID: " + str(r+pr) + "," + str(c+pc) + " = " + grid[r+pr][c+pc] + "\n")
                    if pr == len(pattern)-1 and pc > 0 and \
                                    pc == len(pattern[0]) -1 and pc > 0:
                        #print("~~~~~YES~~~~~")
                        return "YES"
                    if pc == len(pattern[0])-1 and pc > 0:
                        #print("--Next Row--")
                        pr += 1
                    pc = (pc + 1) % len(pattern[0])
    return "NO"


output = ""
for t in range(int(input())):
    grid = []
    pattern = []
    for i in range(int(input().split()[0])):
        grid.append(list(input()))
    for i in range(int(input().split()[0])):
        pattern.append(list(input()))
    output += solve(grid, pattern) + "\n"

print(output)