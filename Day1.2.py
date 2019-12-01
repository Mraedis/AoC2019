filepath = 'fuels.txt'
fuelsum = 0
with open(filepath) as fp:
   line = fp.readline()
   while line:
     dfuel = int(line)
     while dfuel > 0:
       dfuel = dfuel // 3 - 2
       if(dfuel > 0):
         fuelsum += dfuel
     line = fp.readline()
print(fuelsum)
