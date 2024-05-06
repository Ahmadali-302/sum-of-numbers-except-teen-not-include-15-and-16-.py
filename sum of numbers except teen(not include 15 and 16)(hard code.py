def fix_teen(n):
  if 13 <= n <=14 or 16 <= n <=19:
    return 0
  return n
def no_teen_sum(a, b, c):
  sum =  fix_teen(a) + fix_teen(b) + fix_teen(c)
  return sum

print(no_teen_sum(3, 1, 2))