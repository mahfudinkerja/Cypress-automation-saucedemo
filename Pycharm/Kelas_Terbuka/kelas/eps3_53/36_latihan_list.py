# list_buku = []
#
# while True:
#     print("\nMasukan data buku")
#     judul = input("Judul buku\t: ")
#     penulis = input("Nama penulis\t: ")
#
#     buku_baru = [judul, penulis]
#     list_buku.append(buku_baru)
#
#     print("\n\n", "=" * 20, "Data buku" * 20)
#     for index, buku in enumerate(list_buku):
#         print(f"{index + 1} | {buku[0]}\t| {buku[1]}")
#
#     print("\n\n", "=" * 30)
#     isLanjut = input("Lanjut ga gaes ? ( y / n ) : ")
#
#     if isLanjut == "n":
#         break
#
# print("Program Selesai")
book_lists = []
while True:
    print("Please Input Book\'s data ^^")
    title = input('Input Book\'s Title : ')
    writer = input('Input Book\'s Writer : ')

    the_books = [title, writer]
    book_lists.append(the_books)

    print("\n\n Data buku ")
    for index, book in enumerate(book_lists):
        print(f"No.{index + 1}  | {book[0]}\t | {book[1]}")

    isContinue = input("Continue ? (y / n) : ")
    if isContinue == 'n':
        break

print("Program finish ><")
