def fix_teen(n):
  if 13 <= n <=14 or 16 <= n <=19:
    return 0
  else:
    return n

def no_teen_sum():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  num3 = int(input("Enter the second number: "))

  sum_ = fix_teen(num1) + fix_teen(num2) + fix_teen(num3)
  return sum_

print(no_teen_sum())