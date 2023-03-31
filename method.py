from function import *

class Toko:
    def __init__(self):
        self.stok = {}

    # Method non-return untuk menampilkan menu utama
    def menu(self):
        print("Selamat datang di Program Pengecekan Stok")
        print("Silahkan pilih menu:")
        print("1. Cek Stok")
        print("2. Tambah Stok")
        print("3. Hapus Stok")
        print("4. Keluar")

    # Method non-return untuk menjalankan program Toko
    def run(self):
        # Memanggil function menu untuk menampilkan menu utama
        self.menu()

        # Menggunakan loop untuk menampilkan menu utama dan meminta input dari user
        while True:
            pilihan = int(input("Silahkan pilih menu: "))
            if pilihan == 1:
                nama_barang = input("Masukkan nama stok: ")
                stok_barang = cek_stok(self.stok, nama_barang)
                if stok_barang > 0:
                    print("Stok", nama_barang, "saat ini adalah", stok_barang)
                else:
                    print(nama_barang, "tidak tersedia.")
            elif pilihan == 2:
                nama_barang = input("Masukkan nama stok: ")
                jumlah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
                tambah_stok(self.stok, nama_barang, jumlah)
            elif pilihan == 3:
                nama_barang = input("Masukkan nama stok: ")
                jumlah = int(input("Masukkan jumlah stok yang ingin dihapus: "))
                hapus_stok(self.stok, nama_barang, jumlah)
            elif pilihan == 4:
                print("Terima kasih telah menggunakan Program Pengecekan Stok")
                break
            else:
                print("Maaf, pilihan yang Anda masukkan tidak tersedia.")
