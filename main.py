import csv
import os

csv_filename = 'Barang.csv'

# clearscreen untuk membersihkan layar dengan key cls = clearscreen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan menu program
def show_menu():

    clear_screen()
#   Baris kode untuk jumlah total data
    Barang = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
        row_count = sum(1 for row in Barang)

    print("|============================================|")
    print("|====== APLIKASI STOK BARANG TOKO YMART ======|")
    print("|============= MENU DATA BARANG ==============|")
    print("          # Info Total Barang : ", row_count)
    print("|=============================================|")
    print("[1] Lihat Daftar Data Barang                  |")
    print("|---------------------------------------------|")
    print("[2] Tambahkan Data Barang                     |")
    print("|---------------------------------------------|")
    print("[3] Edit Data Barang                          |")
    print("|---------------------------------------------|")
    print("[4] Hapus Data Barang                         |")
    print("|---------------------------------------------|")
    print("[5] Cari Data Barang                          |")
    print("|---------------------------------------------|")
    print("[6] Halaman Credit                            |")
    print("|---------------------------------------------|")
    print("[0] Exit                                      |")
    print("|=============================================|")
    pilihd_menu =input("\nPilih Menu => ")

    # Percabangan untuk menentukan pilihan menu
    if (pilihd_menu == "1"):
        show_barang()
    elif (pilihd_menu == "2"):
        tambahd_barang()
    elif (pilihd_menu == "3"):
        editd_barang()
    elif (pilihd_menu == "4"):
        hapusd_barang()()
    elif (pilihd_menu == "5"):
        cari_barang()
    elif (pilihd_menu == "6"):
        hal_credit()
    elif (pilihd_menu == "0"):
        exit("Anda keluar dari Aplikasi")
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


# fungsi kembali ke menu isinya memanggil fungsi show menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


#  menampilkan barang
def show_barang():
    clear_screen()
    Barang = []
    # buka file CSV dengan mode R / Baca
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    row_count = sum(1 for row in Barang)

    print("-" * 54)
    print("\t\t\tDaftar Stok Barang Toko Ymart")
    print("-" * 55)

    print("|\t Kode \t|\t  NAMA  \t|\t harga \t|\t QTY \t |")
    print("-" * 55)

    # Looping untuk mengeluarkan datanya
    for data in Barang:
        print(f"|\t{data['Kode']} \t| {data['NAMA']} \t| Rp.{data['HARGA']} \t|\t {data['QTY']} \t |")
        print("-" * 55)
        print("\tTotal Data => ", row_count)
        print("-" * 55)

    back_to_menu()


#  tambah barang
def tambahd_barang():
    clear_screen()
    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['Kode', 'NAMA', 'harga', 'QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("="*54)
        print("|------------------ Tambah Barang --------------------|")
        print("="*55)

        Kode = input("Kode Barang   : ")
        nama = input("Nama Barang   : ")
        harga = input("Harga Barang  : ")
        QTY = input("Jumlah Barang : ")

        print("="*55)

        writer.writerow({'Kode': Kode, 'NAMA': nama, 'harga': harga, 'QTY': QTY})

    back_to_menu()


def cari_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    kode = input("Cari berdasrakan kode> ")

    data_found = []

    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            data_found = Barang[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"NAMA: {data_found['NAMA']}")
        print(f"HARGA: Rp.{data_found['HARGA']}")
        print(f"QTY :{data_found['QTY']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()

def editd_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)

    print("-" * 54)
    print("\t\t\tDaftar Stok Barang Toko Ymart")
    print("-" * 55)

    print("kode \t NAMA \t\t Harga \t\t QTY")
    print("-" * 55)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \tRp.{data['HARGA']} \t{data['QTY']}")

    print("-" * 54)
    print("Total Data :",row_count)
    print("-" * 55)
    kode = input("Pilih Kode Barang : ")
    nama = input("Nama Baru         : ")
    harga = input("Harga Baru        : ")
    QTY = input("Jumlah Baru       : ")

    # mencari Barang dan mengubah datanya dengan data yang baru
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang[indeks]['NAMA'] = nama
            Barang[indeks]['HARGA'] = harga
            Barang[indeks]['QTY'] = QTY
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA','QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY']})

    back_to_menu()



def cari_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    kode = input("Cari berdasrakan kode> ")

    data_found = []

    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            data_found = Barang[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("\tDATA BARANG DITEMUKAN\t ")
        print(f"\tNAMA         : {data_found['NAMA']}")
        print(f"\tHARGA        : Rp.{data_found['HARGA']}")
        print(f"\tQTY          : {data_found['QTY']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()


def hapusd_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("kode \t NAMA \t\t harga \t QTY")
    print("-" * 55)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t {data['HARGA']} \t {data['QTY']}")

    print("-"*50)
    kode = input("Hapus Barang dengan KODE : ")

    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang.remove(Barang[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA', 'QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY']})

    print("Data sudah terhapus")

    back_to_menu()

def hal_credit():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    print("=" * 103,"|")
    print("\t\t\t\t\t\t\t\t\tHak Cipta dan Penjelasan Aplikasi                                    |")
    print("-"*104,"|")
    print(" Tentang Aplikasi   : Aplikasi ini merupakan aplikasi tentang melihat stok barang yang ada di toko Ymart |")
    print("-"*104,"|")
    print(" Pembuat Aplikasi   : Muhammad Yusuf                                                                     |\n"
          " NIM                : 10121230                                                                           |\n"
          " Kelas              : IF-6                                                                               |")
    print("-"*104,"|")
    print(" Menu Yang Tersedia  1.Data untuk kita melihat stok barang yang ada di toko Ymart.                       |\n"
          "                     2.Data Untuk Menambahkan barang di toko Ymart.                                      |\n"
          "                     3.Edit data stok barang yang sudah ada di toko Ymart.                               |\n"
          "                     4.Hapus data stok barang yang sudah ada di toko Ymart.                              |\n"
          "                     5.Cari data stok barang yang sudah ada di toko Ymart.                               |\n"
          "                     6.Halaman Credit.                                                                   |")
    print("="*104,"|")

    back_to_menu()


show_menu()



