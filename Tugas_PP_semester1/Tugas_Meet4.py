print("=" * 150)
print("\t\t\t\t\t\t\t\tKALKULATOR")
# Input
print("=" * 150)
bilangan_1 = int(input("Masukkan bilangan X: "))
bilangan_2 = int(input("Masukkan bilangan y: "))
print("=" * 150)
# Function 
def tambah(o,t):
    print(" %d + %d = %d" % (bilangan_1, bilangan_2, o + t))
    print("=" * 150)

def kali(o,t):
    print(" %d * %d = %d" % (bilangan_1, bilangan_2, o * t))
    print("=" * 150)

def bagi(i,o,t):
    if i == 1:
        print(" %d : %d = %5.2f" % (bilangan_1, bilangan_2, o / t))
        print("=" * 150)
    else:
        print(" %d : %d = %5.2f" % (bilangan_2, bilangan_1, t / o))
        print("=" * 150)

def akar(i,o,t):
    if i == 1:
        print(" %d akar %d = %5.2f" % (bilangan_1, bilangan_2, o ** (1 / t)))
        print("=" * 150)
    else:
        print(" %d akar %d = %5.2f" % (bilangan_2, bilangan_1, t ** (1 / o)))
        print("=" * 150)
        
def pangkat(i,o,t):
    if i == 1:
        print(" %d pangkat %d = %d" % (bilangan_1, bilangan_2,  o ** t))
        print("=" * 150)
    else:
        print(" %d pangkat %d = %d" % (bilangan_2, bilangan_1,  t ** o))
        print("=" * 150)

def kurang(i,o,t):
    if i == 1:
        print("%d - %d = %d" % (bilangan_1, bilangan_2, o - t))
        print("=" * 150)      
    else:
        print("%d - %d = %d" % (bilangan_2, bilangan_1, t - o))
        print("=" * 150)        

def operasi(x):
    if x == 2:
        print("1. X - Y \n2. Y - X")
        kurang_pil = int(input("> "))
        kurang(kurang_pil, bilangan_1, bilangan_2)
    if x == 1:
        tambah(bilangan_1,bilangan_2)
    if x == 3:
        kali(bilangan_1,bilangan_2)
    if x == 4:
        print("1. X : Y \n2. Y : X")
        bagi_Pil = int(input("> "))
        bagi(bagi_Pil,bilangan_1,bilangan_2)
    if x == 5:
        print("1. X akar Y \n2. Y akar X")
        akar_Pil = int(input("> "))
        akar(akar_Pil, bilangan_1, bilangan_2)
    if x == 6:
        print("1. X akar Y \n2. Y akar X")
        pangkat_Pil = int(input("> "))
        pangkat(pangkat_Pil, bilangan_1, bilangan_2)
# Perulangan 
while True:
    # Pilihan
    print("0]. [ Exit] \n1]. [ Tambah] \n2]. [ Kurang] \n3]. [ kali] \n4]. [ Bagi] \n5]. [ Akar] \n6]. [ Pangkat]")
    print("=" * 150)
    operasi_ = int(input("Pilih Operasi: "))
    print("=" * 150)
    operasi(operasi_)
    if operasi_ == 0:
        print("Thank you!")
        print("=" * 150)
        break
    if operasi_ < 0 or 6 < operasi_: 
        print("Operasi tidak ditemukan")
        print("=" * 150)

    


