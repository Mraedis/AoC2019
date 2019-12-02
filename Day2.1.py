filepath = 'input.txt'
with open(filepath) as fp:
   line = fp.readline()
   inputs = [int(x) for x in line.split(',')]
   position = 0
   operator = ['+', '*']
   opcode = inputs[position]
   while opcode != 99:
    pos1 = inputs[position+1]
    pos2 = inputs[position+2]
    targ = inputs[position+3]
    if opcode == 1:
      inputs[targ] = inputs[pos1] + inputs[pos2]
    elif opcode == 2:
      inputs[targ] = inputs[pos1] * inputs[pos2]
    else:
      print('Program halted early')
      break
    position += 4
    opcode = inputs[position]
print(inputs)
