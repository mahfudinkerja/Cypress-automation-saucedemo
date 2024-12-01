data = 'ini adalah string'
print(data)
print(type(data))

'''
    1. menggunakan single quote '..'
    2. menggunakan double quote ".."
'''

print("'Hallo, Apakabar?'")
print('"Hallo, Apakabar?"')
print("ini adalah haru jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string

print('mari sholat jum\'at')
print('g\'day, ins\'t it?')

# backslash
print("C:\\user\\mapud")

# tab
print("ucup\tmapud, jajan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.")
print("baris pertama.\rbaris kedua.")
print("baris pertama.\r\nbaris kedua.")

#  3. String literal dan raw string

# salah
print("c:\new folder")

print(10 * "=")

# menggununakan raw string
print(r'c:\new folder ')

# multiline literal sring
print('''
Nama: Ucup
kelas :  3 SD
''')

# multiline literal sring RAW
print(r'''
Nama: Ucup
kelas :  3 SD\newID
website: www.ucup.com
''')
