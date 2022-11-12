data ={"usr" : "", "pass" : "03112"}
buku = {"MA1" : "MEMASAK IKAN", "MA2": "BELAJAR TERBANG", "MA3" : "RAEHAN BAIK?", "MA4" : "KUDAPAN SEHAT", "MA5" : "KALKULUS JILID 1", "MA6" : "PERJALANAN KARIR SAMBO"}
buku_tetap = {"MA1" : "MEMASAK IKAN", "MA2": "BELAJAR TERBANG", "MA3" : "RAEHAN BAIK?", "MA4" : "KUDAPAN SEHAT", "MA5" : "KALKULUS JILID 1", "MA6" : "PERJALANAN KARIR SAMBO"}
q = 0 ; KERANJANG = {}
while q == 0:
    x = input("Username : ") ; data["usr"] = x
    y = input(f"Password (default : {data['pass']}): ") ; print("=" * 80)
    while y == data["pass"] and x == data["usr"]:
        print("0. Exit\n1. Pinjam Buku\n2. Kembalikan buku\n3. Tambah Judul Buku") ; print("=" * 80)
        opsi = int(input("Pilih: ")) ; print("=" * 80)
        if opsi == 0:
            print(f"Terima Kasih {data['usr']}") ; print("=" * 80)
            q = 1 ; break
        elif opsi == 1:
            if len(KERANJANG) >= 3:
                print("Tidak Boleh Pinjam Buku!") ; print("=" * 80)
            else:
                for key,value in buku.items():
                    print(f"{key} : {value}")
                print("=" * 80)
                key = input("Key : ")
                if key in buku: 
                    print(f"Judul : {buku[key]}\nAutor : MARIO VALERIAN RANTE TA'DUNG\nLama Pinjam: 7H") ;  print("=" * 80)
                    KERANJANG[key] = buku_tetap[key]
                    del buku[key]
                else: print("Buku tidak ditemukan atau sedang dipinjam!") ; print("=" * 80)
        elif opsi == 2:
            if len(KERANJANG) == 0:
                print("Keranjang anda kosong, silahkan meminjam buku terlebih dahulu!") ; print("=" * 80)
            else:
                print("Daftar buku yang dipinjam : ")
                for key,value in KERANJANG.items(): print(f"{key} : {value}")
                print("=" * 80) ; key = input("Key : ") ; print("=" * 80) ; del KERANJANG[key] ; buku[key] = buku_tetap[key]
        elif opsi == 3:
            kode, nama = input("Kode buku : ") , input("Judul Buku : ")
            buku[kode] = nama ; buku_tetap[kode] = nama ; print("=" * 80)
        else:
            print("Opsi tidak ditemukan!\n") ; print("=" * 80)
    else: print("Password salah!") ; print("=" * 80)

        
        
