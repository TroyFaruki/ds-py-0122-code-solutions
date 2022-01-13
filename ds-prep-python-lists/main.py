ages = [29, 19, 17, 26, 32, 16, 21]
print(ages)
print(ages[4:5])
print(ages[-2:-1])
print(ages[3:6])
print(ages[:4])

if 17 in ages:
  print((ages))

if 42 in ages:
  print((ages))

ages[2] = 18
print(ages)

temp = ages[4]
ages[3] = ages[4]
temp = ages[3]
print("Instruction 15: ",ages)

ages.append(45)
ages.insert(0, 32)
ages.insert(5, 37)
print(ages)
ages.pop()
print(ages)
ages.pop(2)
print(ages)
