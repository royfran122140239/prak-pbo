class BilanganGanjil:
    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper

    def JumlahBilanganGanjil (self):
        if self.lower < 0 or self.upper < 0:
            return "Batas bawah dan atas yang di masukan tidak boleh di bawah nol"
        JumlahGanjil = 0
        for i in range(self.lower,self.upper + 1):
            if i % 2 != 0:
             JumlahGanjil += 1
        return JumlahGanjil
lower = int(input("Masukan batas bawah : "))
upper = int(input("Masukan batas atas : "))

bilanganganjil = BilanganGanjil(lower,upper)

JumlahGanjil = bilanganganjil.JumlahBilanganGanjil()

print("jumlah bilangan ganjil dalam rentang tersebut adalah : ",JumlahGanjil)