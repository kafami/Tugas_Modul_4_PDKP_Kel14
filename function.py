# Function return untuk melakukan cek stok
def cek_stok(stok, nama_barang):
    if nama_barang in stok:
        return stok[nama_barang]
    else:
        return 0

# Function non-return untuk menambahkan stok 
def tambah_stok(stok, nama_barang, jumlah):
    if nama_barang in stok:
        stok[nama_barang] += jumlah
    else:
        stok[nama_barang] = jumlah
    print("Berhasil menambahkan stok", nama_barang, "sebanyak", jumlah)

# Function non-return untuk menghapus stok 
def hapus_stok(stok, nama_barang, jumlah):
    if nama_barang in stok:
        if stok[nama_barang] >= jumlah:
            stok[nama_barang] -= jumlah
            print("Berhasil menghapus stok", nama_barang, "sebanyak", jumlah)
        else:
            print("Maaf, stok", nama_barang, "tidak mencukupi.")
    else:
        print("Maaf, stok", nama_barang, "tidak tersedia.")

function.py
