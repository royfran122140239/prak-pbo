class hewan :
    def __init__ (self,nama,jenis_kelamin):
        self.nama = nama
        self.jenis_keamin = jenis_kelamin

    def bersuara (self):
        pass
    def makan(self):
        pass
    
class kucing(hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)

    def bersuara(self):
        print(f"sucing {self.nama} bersuara : Meong!")

    def makan(self):
        print(f"kucing {self.nama} sedang makan : ikan")

class anjing(hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)

    def bersuara(self):
        print(f"Anjing {self.nama} bersuara : guk guk!!")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan : tulang")


hewan1 = kucing("Kiki","Betina")
hewan2 = anjing("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()

hewan2.bersuara()
hewan2.makan()