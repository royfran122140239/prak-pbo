class Lingkaran:
    pi = 3.14
    def __init__(self,jarijari):
        self.jarijari = jarijari

    def luas(self):
        return self.jarijari**2 * Lingkaran.pi
    
    def keliling(self):
        return self.jarijari * 2 * Lingkaran.pi

jarijari = float(input("Jari-jari : "))

if jarijari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    lingkaran = Lingkaran(jarijari)
    print(f"Luas : {lingkaran.luas()}")
    print(f"Keliling : {lingkaran.keliling()}")