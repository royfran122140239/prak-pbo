class Manusia:
  def __init__(self, nama, usia):
    self.nama = nama
    self.usia = usia
    print(f"Data Manusia yang bernama {self.nama} berumur {self.usia} tahun sudah ditambahkan.")

  def __del__(self):
    print(f"Data Manusia yang bernama {self.nama} berumur {self.usia} tahun sudah dihapus.")

  def berbicara_decorator(func):
    def wrapper(self, *args, **kwargs):
      print(f"{self.nama} {self.usia} tahun berkata: ", end="")
      return func(self, *args, **kwargs)
    return wrapper

  @berbicara_decorator
  def berbicara(self, kalimat):
    return kalimat

manusia1 = Manusia("Mahmud", 97)

manusia1.berbicara("Hallo semuanya!")

del manusia1