def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x] [x] for x in range(len(arr))])
    d2 = sum([arr[y] [n - 1 - y] for y in range(len(arr))])
    return abs(d1-d2)

A = [[1, 4, 5], 
    [-5, 8, 9],
    [3, 5, 6]]
n = 3
print("A", A)

# for x in range(len(A)):
#   print(A[x][x])

for y in range(len(A)):
  print(A[n-1-y][y])