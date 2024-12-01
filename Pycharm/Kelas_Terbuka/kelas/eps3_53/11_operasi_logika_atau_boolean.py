# Operasi logika atau boolean

# not, or, and, xor

# NOT
print("===NOT===")
a = False
c = not a

print('data a = ', a)
print('data c = ', c)

# OR (Jika salah satu trus, maka hasilnya akan true)
print("===OR===")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)

# AND (Jika salah satu false, maka hasilnya akan false)
print("===AND===")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)

# XOR (akan True jika salah satu True)
print("===XOR===")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)
