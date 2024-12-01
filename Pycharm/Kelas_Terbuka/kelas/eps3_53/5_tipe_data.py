# Integer
data_integer = 10000
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# Float, data dengan koma
data_float = 10000.09
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# String, kumpulan karakter
data_string = "apiiii"
print("data : ",
      data_string)
print("- bertipe : ", type(data_string))

# Boolean, true / false
data_boolean = True
print("data : ", data_boolean)
print("- bertipe : ", type(data_boolean))

# Tipe data khusus

# bilangan kompleks
data_complex = complex(5, 7)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char

data_c_double = c_double(5.7)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))


