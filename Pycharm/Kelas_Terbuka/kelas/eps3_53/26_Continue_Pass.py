angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")  # aksi 1

    if angka == 3:
        print("Nice!")
        continue  # akan membuat loop meloncat ke step selanjutnya

    print("wasaapp!")  # aksi 2

print("Cukup??!")
