# Import Modules
from prettytable import PrettyTable
import numpy as np
import math
from matplotlib import pyplot as plt

# Create Class
class RegresiLinearSederhana:

  def fit(self, x: list, y: list):
    """
    Menerapkan Variabel X (Independen) dan Variabel Y (Dependen) pada Instance Model Regresi Linear Sederhana
    yang Telah Dibuat Sebelumnya
    """

    # Membuat Beberapa Validasi
    assert len(x) > 1, "Jumlah Data Harus Lebih dari 1"
    assert len(y) > 1, "Jumlah Data Harus Lebih dari 1"

    # Melakukan Kalkulasi Terhadap Parameter dll.
    self.__x = np.array(x)
    self.__y = np.array(y)

    self.__b0 = round(((sum(self.__y) * sum(self.__x ** 2)) - (sum(self.__x) * sum(self.__x * self.__y))) / ((len(self.__x) * sum(self.__x ** 2)) - sum(self.__x) ** 2), 3)

    self.__b1 = round(((len(self.__x) * sum(self.__x * self.__y)) - (sum(self.__x) * sum(self.__y))) / (len(x) * sum(self.__x ** 2) - sum(self.__x) ** 2), 3)

    self.__r = round(((len(self.__x) * sum((self.__x * self.__y))) - (sum(self.__x) * sum(self.__y))) / math.sqrt(int(((len(self.__x) * sum(self.__x ** 2)) - (sum(self.__x)**2))) * int(((len(self.__x) * sum(self.__y ** 2)) - (sum(self.__y) ** 2)))), 3)

    self.__rsquare = round(self.__r ** 2, 3)

    self.__thitung = round((self.__r * math.sqrt(len(self.__x) - 2)) / (math.sqrt(1 - self.__rsquare)), 3)

    # Mengembalikan Nilai Dalam Bentuk Dictionary
    return {
      "b0" : self.__b0,
      "b1" : self.__b1,
      "R-square" : self.__rsquare,
      "t-hitung" : self.__thitung
    }

  # Menerapkan Getter pada Beberapa Property Agar Bisa Diakses Namun Tidak Bisa Diubah
  @property
  def x(self):
    return self.__x

  @property
  def y(self):
    return self.__y

  @property
  def b0(self):
    return self.__b0

  @property
  def b1(self):
    return self.__b1

  @property
  def r(self):
    return self.__r

  @property
  def rsquare(self):
    return self.__rsquare

  @property
  def thitung(self):
    return self.__thitung
  
  def tampilkan_hasil(self):
    """
    Menampilkan Hasil Estimasi dalam Bentuk yang Lebih Rapi.
    CATATAN : Harus Memanggil Method "fit" Terlebih Dahulu Sebelum Memanggil Method ini.
    """
    my_table = PrettyTable()
    my_table.field_names = ["Parameter", "Nilai", "t-hitung"]
    my_table.add_rows(
      [
        ["B0", self.__b0, "-"],
        ["B1", self.__b1, self.__thitung]
      ]
    )
    print("Hasil Analisis Regresi")
    print(my_table)
    print(f"R-Square yang didapatkan adalah sebesar {self.__rsquare}")

  def plot(self, ukuran=(12, 8), judul = "Plot Antara Variabel X dan Y", nama_x_axis = "X", nama_y_axis = "Y"):
    """
    Menampilkan Hasil Plot Pada Model yang Telah Dibuat
    """
    plt.figure(figsize=(ukuran))
    plt.plot(self.__x, self.__y, 'o')
    plt.plot(self.__x, self.__b0+self.__b1*self.__x)
    plt.title(judul)
    plt.xlabel(nama_x_axis)
    plt.ylabel(nama_y_axis)
    plt.show()

  def predict(self, x_baru: list):
    """
    Memprediksi Data yang Akan Datang Berdasarkan Model yang Telah Dibuat.
    """
    hasil_prediksi = []
    for i in x_baru:
      x = round((self.__b0 + self.__b1 * i), 3)
      hasil_prediksi.append(x)
    return hasil_prediksi

# Mencoba Class yang Telah Dibuat
x = [8, 9, 7, 6, 13, 7, 11, 12]
y = [35, 49, 27, 33, 60, 21, 45, 51]
x_baru = [24, 25, 76]

reglin = RegresiLinearSederhana()
reglin.fit(x, y)
reglin.tampilkan_hasil()
reglin.plot()
hasil_pred = reglin.predict(x_baru)
print(hasil_pred)