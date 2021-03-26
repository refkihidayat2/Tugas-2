



def menu():
    print ("Selamat datang!")
    print ("---MENU---")
    print ("1, Daftar Kontak")
    print ("2, Tambah Kontak")
    print ("3, Keluar")

nama = []
notelpon = []

def Tambah():
    while True:
        A = str(input("Masukkan nama :"))
        B = int(input("Masukkan No Telepon :"))
        nama.append(A)
        notelpon.append(B)
        break


menu()
pil = int(input("Masukkan pilihan : "))
while pil != 0:
    if pil == 1:
        for a in nama:
            print("Nama:", a)
        for b in notelpon:
            print("No telpon:", b)
        continue

    elif pil == 2:
        Tambah()
        print ("Kontak berhasil ditambahkan")

    elif pil == 3:
        print("Program selesai, sampai jumpa!")
        break

    else:
        print("Menu tidak tersedia")

    print()
    menu()
    pil = int(input("Masukkan pilihan : "))




