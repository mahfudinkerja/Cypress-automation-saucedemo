# Looping dri list

print('\n#for loop')
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"number : {number}")

members = ['gompar', 'bella', 'cella', 'rindha', 'ghavi']

for member in members:
    print(f"member : {member}")

print('\n#loop dan range')
numbers = [6, 7, 8, 9, 10]
length = len(numbers)

for i in range(length):
    print(f"number = {numbers[i]}")

print('\n#while loop')
numbers = [11, 12, 13, 14, 15]
length = len(numbers)
i = 0

while i < length:
    print(f"number = {numbers[i]}")
    i += 1

print('\n#List comprehension')
data = ['gompar', 'rindha', 'putri', 2, 3, 4, 5]

[print(f"data = {i}") for i in data]

numbers = [11, 12, 13, 14, 15]
angka_kuadrat = [i ** 2 for i in numbers]
print(f"angka kuadrat = {angka_kuadrat}")

print('\n#Enumerate')  # dapet index dan data nya
data_list = ['gompar', 'rindha', 'putri', 2, 3, 4, 5]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
