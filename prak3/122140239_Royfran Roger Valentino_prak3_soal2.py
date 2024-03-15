class dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        dagangan.jumlah_barang += 1
        dagangan.list_barang.append((self.__nama,self.__stok,self.__harga))

    def __del__(self):
        dagangan.jumlah_barang -= 1
        dagangan.list_barang.remove((self.__nama,self.__stok,self.__harga))

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for i, barang in enumerate(cls.list_barang, start=1):
            print(f"{i}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")

dagangan1 = dagangan("Galon Aqua 19L", 32, 17000)
dagangan2 = dagangan("Gas LPG 5 kg", 22, 88000)
dagangan3 =dagangan("Beras Ramos 5 kg", 13, 68000)
dagangan.lihat_barang()
print("\nGalon Aqua 19L dihapus dari toko!\n")
del dagangan1
dagangan.lihat_barang()
print("\nGas LPG 5 kg dihapus dari toko!\n")
del dagangan2
print("Beras Ramos 5 kg dihapus dari toko!")
del dagangan3