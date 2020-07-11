coordinates = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(coordinates[2][1])
print(coordinates[1])

for row in coordinates:
    for col in row:
##        print(col)
        print(col, end= " ")
