from datetime import datetime

# ################################# 10 ############################################
# Display product
product = [
    [1, "Celana Jeans       L         Pria        Navy", 300000],
    [2, "Celana Formal      L         Pria        Hitam", 400000],
    [3, "Celana Formal      XL        Pria        Navy", 500000],
    [4, "Celana Jogger      XL        Pria        Navy", 200000],
    [5, "Celana Skinny      L         Pria        Cream", 300000],
    [6, "Celana Chinos      S         Pria        Maroon", 100000],
    [7, "Celana Chinos      M         Pria        Hitam", 150000],
    [8, "Celana Chinos      L         Pria        Navy", 200000],
    [9, "Celana Boot Cut    M         Pria        Maroon", 250000],
    [10, "Celana Cargo       L         Pria        Hitam", 350000],
    [11, "Celana Cargo       XL        Pria        Grey", 375000],
    [12, "Celana Drawstring  L         Pria        Maroon", 100000],
    [13, "Celana Jeans       XL       Wanita       Navy", 300000],
    [14, "Celana Palazzo     M        Wanita       Hitam", 200000],
    [15, "Celana Palazzo     L        Wanita       Lilac", 225000],
    [16, "Celana Leggings    M        Wanita       Hitam", 100000],
    [17, "Celana Leggings    S        Wanita       Grey", 125000],
    [18, "Celana Kulot       XL       Wanita       Maroon", 250000],
    [19, "Celana Cargo       L        Wanita       Hitam", 225000],
    [20, "Celana Jogger      S        Wanita       Hitam", 300000],
    [21, "Kemeja Denim       L         Pria        Navy", 400000],
    [22, "Kaos Polos         XL        Pria        Putih", 200000],
    [23, "Kemeja Rugby       L         Pria        Cream", 300000],
    [24, "Kaos Polo          M         Pria        Navy", 200000],
    [25, "Kemeja Flanel      XL        Pria        Navy", 250000],
    [26, "Jaket Denim        L         Pria        Hitam", 500000],
    [27, "Sweater            L         Pria        Army", 400000],
    [28, "Kemeja Denim       S         Pria        Navy", 400000],
    [29, "Tunik              L        Wanita       Cream", 250000],
    [30, "Blouse             L        Wanita       Army", 200000],
    [31, "Gamis              XL       Wanita       Navy", 500000],
    [32, "Bolero             M        Wanita       Maroon", 325000],
    [33, "Blazer             L        Wanita       Navy", 450000],
    [34, "Drees              XL       Wanita       Putih", 550000],
    [35, "Cardigan           L        Wanita       Hitam", 100000],
    [36, "Sweater            XL       Wanita       Cream", 200000],
    [37, "Rompi              M        Wanita       Hitam", 100000],
    [38, "Hoodie             L        Wanita       Pink", 200000],
    [39, "Kaftan             XL       Wanita       Navy", 250000],
    [40, "Jumpsuit           L        Wanita       Hitam", 150000],
]
    ################################################# 10 #################################################

# # Fungsi-fungsi
def sambutan():
    print("-----------------  SELAMAT DATANG DI TOKO BUSANAKU  ------------------")
    print("")


def display():
    print("ID\t  Product\t  Size\t  Pria/Wanita\t Warna\t    Harga")
    for i in product:
        print("{0}\t{1}\t Rp {2}".format(i[0], i[1], i[2]))
    

def order(*order):
    print("\n\n")
    print("======================================================================")
    print("-----------------  Selamat datang di Toko BusanaKU  ------------------")
    print("======================================================================")
    print("Tanggal Order    :   {}".format(str(datetime.now())))
    print("Nama Pembeli     :   {}".format(nama_pembeli))
    print("Product id       :   {}".format(pilihan))
    print("Nama Product     :   {}".format(item[1]))
    print("Cara Bayar       :   {}".format(bayar))
    print("Jumlah           :   {}".format(jumlah))
    print("Harga Satuan     :   Rp {}".format(item[2]))
    print("Total Belanja    :   Rp {}".format(total))
    print("Diskon Cash      :   Rp {}".format(diskon))
    #print("Admin           :   Rp {}".format(admin))
    print("Total Akhir      :   Rp {}".format(total_akhir))
    print("======================================================================")


def order1(*order1):
    print("\n\n")
    print("======================================================================")
    print("-----------------  Selamat datang di Toko BusanaKU  ------------------")
    print("======================================================================")
    print("Tanggal Order    :   {}".format(str(datetime.now())))
    print("Nama Pembeli     :   {}".format(nama_pembeli))
    print("Product id       :   {}".format(pilihan))
    print("Nama Product     :   {}".format(item[1]))
    print("Cara Bayar       :   {}".format(bayar))
    print("Kredit           :   {} bln".format(kredit))    
    print("Jumlah           :   {}".format(jumlah))
    print("Harga Satuan     :   Rp {}".format(item[2]))
    print("Total Belanja    :   Rp {}".format(total))
    print("Dp               :   Rp {}".format(dp))
    print("Bunga            :   Rp {}".format(bunga))
    print("Admin            :   Rp {}".format(admin_kredit))
    print("Total Akhir      :   Rp {}".format(total_akhir))
    print("----------------------------------------------------------------------")
    print("Tagihan/Bln      :   Rp {} * {}".format(tagihan, kredit))
    print("----------------------------------------------------------------------")
    print("------------- Terima Kasih Sudah Berbelanja di Toko Kami -------------\n")

def bayar1(*bayar1):
    print("----------------------------------------------------------------------")
    print("Total di bayar   :   Rp {}".format(pembayaran))
    print("Total pembelian  :   Rp {}".format(total_akhir))
    print("Kembali          :   Rp {}\n".format(sesudah))
    print("------------- Terima Kasih Sudah Berbelanja di Toko Kami -------------\n")

sambutan()
display()

print("----------------------------------------------------------------------")
print("")
# #
admin = 0
admin_kredit = 10000
total_akhir = 0
diskon = 0
kredit = 0
dp = 100000
# #
pilihan = int(input("Masukkan ID yang ingin di beli 1 sd 40     :   "))
# #
for item in product:
    if item[0] == pilihan:
        # #
        nama_pembeli = input("Masukkan Nama Pembeli                      :   ")
        # #
        jumlah = int(input("Masukkan jumlah yang di beli               :   "))
        ################################################# 20 #################################################
        bayar = input("Masukkan cara Bayar Cash / Kredit          :   ")
        if (bayar == "Kredit") or (bayar == "kredit") or (bayar == "KREDIT") or (bayar == "1"):
            # #
            kredit = int(input("Angsuran 6/12 Bln                          :   "))
            # #
            if kredit == 6:
                total = jumlah * item[2]
                bunga = int(total * 0.05)
                total_akhir = int(total + bunga + admin_kredit)
                tagihan = int(total_akhir/6)
                # #
                order1(item, nama_pembeli, bunga, admin_kredit, total,
                        total_akhir, tagihan, dp)
                # #
            elif kredit == 12:
                total = jumlah * item[2]
                bunga = int(total * 0.10)
                total_akhir = int(total + bunga + admin_kredit)
                tagihan = int(total_akhir/12)
                # #
                order1(item, nama_pembeli, bunga, admin_kredit, total,
                        total_akhir, tagihan, dp)
            elif (kredit != 6) or (kredit != 12):
                print(" --------- Tidak Ada Tenor Tersebut --------- ")
                break
            else:
                [True]

        ################################################# 20 #################################################
        ################################################# 30 #################################################
        elif (bayar == "Cash") or (bayar == "cash") or (bayar == "CASH") or (bayar == "2"):
            tagihan = 0
            bunga = 0
            total = jumlah * item[2]
            diskon = int(total * 0.10)
            total_akhir = total - diskon + admin
            # #
            if (pilihan > 35):
                diskon = 0
                total_akhir = total + admin
            else:
                [True]
            # #
            order(item, nama_pembeli, diskon, total,
                    total_akhir) # admin
            # #
            pembayaran = int(input("Bayar            :   Rp "))
            sesudah = pembayaran- total_akhir
            # #
            bayar1(pembayaran, total_akhir, sesudah)
    ################################################# 30 #################################################
    ################################################# 40 #################################################
    elif pilihan == 0 or pilihan >= 41:
        print("Tidak ada pilihan tersebut")
        break
    else:
        [True]
    ################################################# 40 #################################################
