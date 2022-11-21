import datetime
from tabulate import tabulate
while True:
    x = datetime.datetime.now() 
    _fase = "Start"
    while _fase =="Start":
        _Keterangan = input("Keterangan : ")
        _pengeluaran = input("Pengeluaran : ")
        with open('data.txt', "a") as catat:
            _data = [[x.strftime("%x").ljust(22), _Keterangan.ljust(47), _pengeluaran.ljust(16)]] 
            catat.write(tabulate(_data,tablefmt="grid"))
        _fase = "Stop"
    print("Terima kasih...")
    break

        

    

    
