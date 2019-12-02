filepath = 'input.txt'
with open(filepath) as fp:
   line = fp.readline()
   inputs = [int(x) for x in line.split(',')]
   noun = 0
   verb = 0
   position = 0
   opcode = inputs[position]
   for verb in range(0,99):
     for noun in range(0,99):
      inputs = [int(x) for x in line.split(',')]
      inputs[1] = noun
      inputs[2] = verb
      position = 0
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
      if inputs[0] == 19690720:
        print('Noun: ' + str(noun) + ' \nVerb: ' + str(verb))
