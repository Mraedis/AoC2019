filepath = 'fuels.txt'
fuelsum = 0
with open(filepath) as fp:
   line = fp.readline()
   while line:
     fuelsum += int(line) // 3 - 2
     line = fp.readline()
print(fuelsum)
