class Mahasiswa:
  def __init__(self, nim, nama, angkatan, isMahasiswa=True):
    self.__nim = nim
    self.__nama = nama
    self.angkatan = angkatan
    self.isMahasiswa = isMahasiswa

  @property
  def nama(self):
    return self.__nama

  @nama.setter
  def nama(self, new_nama):
    self.__nama = new_nama

  @property
  def nim(self):
    return self.__nim

  @nim.setter
  def nim(self, new_nim):
    self.__nim = new_nim

  def hitung_ipk(self, nilai_sks, sks_tempuh):
    if sks_tempuh == 0:
      return 0
    return nilai_sks / sks_tempuh

  def cek_lulus(self, ips):
    if ips >= 2.75:
      return "Lulus"
    return "Tidak Lulus"

  def info_lengkap(self):
    print(f"""
    NIM: {self.nim}
    Nama: {self.nama}
    Angkatan: {self.angkatan}
    Status: {'Mahasiswa' if self.isMahasiswa else 'Bukan Mahasiswa'}
    """)

mahasiswa1 = Mahasiswa("123456789", "Mahmud", 2022)

mahasiswa1.nama = "Mahmud Santoso"

mahasiswa1.info_lengkap()

ipk_mahasiswa1 = mahasiswa1.hitung_ipk(3.8, 24)
print(f"IPK: {ipk_mahasiswa1}")

status_lulus_mahasiswa1 = mahasiswa1.cek_lulus(3.0)
print(f"Status Lulus: {status_lulus_mahasiswa1}")

mahasiswa2 = Mahasiswa("987654321", "Ani", 2022)

mahasiswa2.info_lengkap()