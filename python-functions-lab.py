#Task 1

def sum_to (n):
  sum = 0
  for i in range(1,n+1):
    sum += i
  print(sum) 

sum_to(6)

#Task 2

def largest (list):
  largest = list[0]
  for num in list:
    if num > largest:
      largest = num
  print(largest)

largest([10,4,2,231,91,54])

#Task 3

def occurances (str1, str2):
  occurances = len(str1.split(str2)) - 1 
  print(occurances)

occurances('fleep floop', 'ee')

#Task 4

def product (*args):
  product = 1
  for arg in args:
    product *= arg
  print(product)

product(2, 5, 5)


