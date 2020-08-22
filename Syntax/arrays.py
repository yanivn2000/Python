cars = ["bmw", "volvo", "opel", "ford"]
print(cars)
print(f"cars[0] {cars[0]}")
print(f"cars[-1] {cars[-1]}")
print(f"cars[0:2] {cars[0:2]}")
print(f"cars[1:-1] {cars[1:-1]}")
print(f"cars[:-1] {cars[:-1]}")
print(f"cars[1:] {cars[1:]}")


#find max year
years = [1976, 2001, 2009, 1987, 1966]
max = years[0]
for year in years:
    if year > max:
        max = year
print(f"The max year is {max}")

#matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for item in row:
        print(item)
