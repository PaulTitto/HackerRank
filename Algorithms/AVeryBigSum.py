numbers = 1000000001, 1000000002, 1000000003, 1000000004, 1000000005

# print(sum(numbers))
def int_list(numbers):
  summ = 0
  for i in numbers:
      summ += i

  print(summ)

int_list(numbers)


def aVeryBigSum(ar):
    # Write your code here
    summ = 0
    for i in ar:
        summ += i
    return summ