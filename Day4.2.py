def has_double(num):
  digits = [char for char in str(num)]
  last = digits[0]
  last2 = digits[1]
  dubs = last == last2
  trips = False
  hasdubs = False
  for digit in digits[2:]:
    if digit == last2:
      trips = dubs
      dubs = True
    else:
      if dubs and not trips:
        hasdubs = True
    dubs = digit == last2
    last = last2
    last2 = digit
  return hasdubs or dubs and not trips
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
