# Latihan

# Kalculator
print(20 * "=")
print("Kalkulator sederhana")
print(20 * "=")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("Operator (+, -, x, /) = ")
angka_2 = float(input("Masukan angka 2 = "))

# Percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Masukin yang bener dong operator nya")

print(20*"=")
print("Program nya selesai")