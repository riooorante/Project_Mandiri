# List untuk angka ke Huruf
List_A = ["Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh"] 

# Kamus untuk huruf Ke Angka
Dic_B = {"Satu" : 1 ,"Dua" : 2,"Tiga" : 3, "Empat" : 4, "Lima" : 5, "Enam" : 6, "Tujuh" : 7, "Delapan" : 8,"Sembilan" : 9, "sepuluh" : 10}

while True:
    print("\n> Silahkan Memilih : \n 1. Angka Ke Huruf. \n 2. Huruf Ke Angka. \n 0. Untuk mengakhiri.")
    y = int(input("> Pilihan Anda (1/2/0) : "))

    while y == 1:
        if True:
            O = int(input("> Masukkan Angka (0 < X < 11) : "))
            if O > 0 and O < 11: 
                print("> Hasil Konversi > ", List_A[O - 1])
                y += 2
            else:
                print("> Angka Tidak Dapat Diproses!")
                
        if y == 3:
            T = input("> Ketik Y untuk mengulang proses : ")
            if T == "Y" :
                y -= 2
            else:
                False 

    while y == 2:
        if True:
            P = input("> Masukkan Angka (Satu - Sepuluh) : ") ; P = P.title()
            if P in Dic_B: 
                print("> Hasil Konversi > ", Dic_B.get(P))
                y += 2
            else:
                print("> Tidak ditemukan!")
                
        if y == 4:
            T = input("> Ketik Y untuk mengulang proses : ")
            if T == "Y" :
                y -= 2
            else:
                False
            
    if y == 0:
        print("> Program Berakhir....")
        break
    else:
        print("> Error")
        

    
    
