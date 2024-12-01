# # Membuat gabungan area rentang dari angka
#
# # ++++++++3-------10+++++++++
#
# inputUser = float(input("Masukan angka yang bernilai kurang dari 3 atau lebih dari 10 : "))
#
# # ++++++3------
# isKurangDari = (inputUser < 3)
# print("Kurang dari 3 =", isKurangDari)
#
# # -------10+++++++
# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 =", isLebihDari)
#
# # +++++++++3-------10++++++++++
# isCorrect = isKurangDari or isLebihDari
# print("Angka yang anda masukan :", isCorrect)
#
# print("\n", 30 * "=", "\n")
# # --------3++++++++10-----------
# inputUser = float(input("Masukan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))
#
# # ---------3++++++++
# isLebihDari = (inputUser > 3)
# print("Lebih dari 3 = ", isLebihDari)
#
# # ++++++++++10------
# isKurangDari = (inputUser < 10)
# print("Kurang dari 10 = ", isKurangDari)
#
# # --------3++++++++10-----------
# isCorrect = isLebihDari and isKurangDari
# print("angka yang anda masukan :", isCorrect)
#
# print("\n", 30 * "=", "Latihan", "\n")
#
inputUser = float(input("Masukan angka : "))

# Latihan 1
angka1 = (inputUser >= 0) and (inputUser <= 5)
print("angka yang anda masukan >= 0 dan <= 5 =", angka1)

angka2 = (inputUser >= 8) and (inputUser <= 11)
print("angka yang anda masukan >= 8 dan <= 11 =", angka2)

hasil = angka1 and angka2
print("Jawab", hasil)

inputUser = float(input("Masukan angka : "))
# Latihan 2
angka3 = (inputUser <= 0) or (inputUser <= 11)
print("angka <= 0 atau <= 11 = ", angka3)
angka4 = (inputUser >= 0) or (inputUser >= 8)
print("angka >= 0 atau <= 11 = ", angka4)
