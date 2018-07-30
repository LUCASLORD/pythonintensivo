filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())


print("===========================================================")
print("ler arquivo linha  a linha\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())


print("===========================================================")
print("ler arquivo para lista\n")
with open(filename) as file_object:
    lines = file_object.readlines() #armazena cada linha na lista lines

for line in lines:
    print(line.strip())

print("===========================================================")
print("passar para uma única string\n")
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


