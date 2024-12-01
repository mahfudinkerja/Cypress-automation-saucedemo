# latihan loop membuat segitiga

sisi = int(input("Masukan angka sisi : "))

# 1. menggunakan for
print("=" * 20, "Start For", "=" * 20)
count = 1  # dummy variable
for i in range(sisi):
    print("*" * count)
    count += 1
print("=" * 20, "Finish For", '=' * 20)

# 2. Menggunakan while

print("=" * 20, "Start While", "=" * 20)
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

print("=" * 20, "End While", '=' * 20)

print("=" * 20, "Start Bilangan Ganjil", "=" * 20)
count = 1
while True:
    if count % 2:
        # print jika ganjil
        print('*' * count)
        count += 1
    else:
        # akan kembali loop jika ganjil
        count += 1
        continue
    # akan break jika count > dari sisi
    if count > sisi:
        break

print("=" * 20, "ENd Bilangan Ganjil", '=' * 20)

print("=" * 20, "Start Bilangan Ganjil", "=" * 20)
count = 1
spasi = int(sisi / 2)

while True:
    if count % 2:
        print(" " * spasi, "+" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("=" * 20, "ENd Bilangan Ganjil", '=' * 20)
