def menu():
    print ("Selamat datang!")
    print ("---MENU---")
    print ("1, Daftar Kontak")
    print ("2, Tambah Kontak")
    print ("3, Keluar")


def Tambah():
    A = str(input("Masukkan nama :"))
    B = int(input("Masukkan No Telepon :"))
    print ("Nama :", A)
    print ("No Telepon :", B)


menu()
pil = int(input("Masukkan pilihan : "))
while pil != 0:
    if pil == 1:
        Tambah()
    
    elif pil == 3:
        print("Program selesai, sampai jumpa!")
    
    print()
    menu()
    pil = int(input("Masukkan pilihan : "))



