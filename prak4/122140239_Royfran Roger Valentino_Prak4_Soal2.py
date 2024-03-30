import math
class persegi:
    def __init__(self,sisi):
        self.sisi = sisi

    def hitungluas(self):
        return self.sisi ** 2
    
class lingkaran :
    def __init__ (self,jari_jari):
        self.jari_jari = jari_jari

    def hitungluas(self):
        return math.pi * self.jari_jari ** 2
    
Persegi = persegi(5)
Lingkaran = lingkaran(3)

print(f"luas persegi : {Persegi.hitungluas()}")
print(f"luas lingkaran : {Lingkaran.hitungluas()}")