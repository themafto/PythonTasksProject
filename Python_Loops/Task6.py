grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def modify_values(grid):
    for index in range(len(grid)):
        for j in range(len(grid[index])):
            if grid[index][j] % 2 == 0:
                grid[index][j] *= 2
            else:
                grid[index][j] = 0

modify_values(grid)
print(grid)


