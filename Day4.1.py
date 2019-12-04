def has_double(num):
  digits = [char for char in str(num)]
  last = digits[0]
  same = False
  for digit in digits[1:]:
    if digit == last:
      same = True
    last = digit
  return same
def no_dec(num):
  digits = [char for char in str(num)]
  last = digits[0]
  lower = True
  for digit in digits[1:]:
    if (int(digit) < int(last)):
      lower = False
    last = digit
  return lower

lower = 171309
upper = 643603
correct = 0

for num in range(lower, upper):
  if(has_double(num) and no_dec(num)):
    correct += 1
print(correct)
