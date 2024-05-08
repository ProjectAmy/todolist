# Membuat to-do list dengan fitur CRUD

import os

class todo:

    def __init__(self, tugas):
        self.tugas = tugas
        self.tugas_baru = None
        self.nomor_hapus = None
        self.nomor_rubah = None
        self.dihapus = None
        self.load()

    def tampil(self):

        if self.tugas: # ngecek ada isinya apa ndak
            print("Berikut adalah daftar tugas anda :\n")
            for nomor, item in enumerate(self.tugas, start = 1):
                print(f"{nomor}. {item}")
        else:
            print("\nBelum ada tugas hari ini.\nPilih opsi 2 untuk menambahkan tugas\n")

        print("")
    def tambah(self):

        while True:
            self.tugas_baru = input("\nKetikan tugas baru.\nKetik (dah) untuk mengakhiri : ")

            if self.tugas_baru.lower() == "dah": # cek udah selesai
                print("Siap!\n")
                self.tampil()
                break

            if self.tugas_baru:
                self.tugas.append(self.tugas_baru)
                self.save()

    def hapus(self):

        if not self.tugas:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru")
            return

        print("")
        self.tampil()
        print("00 - Batal menghapus\n")

        while True:
            try:
                self.nomor_hapus = int(input("Tugas nomor berapa yang ingin dihapus? "))
                if self.nomor_hapus == '00':
                    break
                break
            except ValueError:
                print("Salah input! Masukan bilangan bulat!")
        print("")

        if 1 <= self.nomor_hapus <= len(self.tugas):
            self.dihapus = self.tugas.pop(self.nomor_hapus - 1)
            self.save()
            print(f"Tugas : {self.dihapus}\nBerhasil dihapus dari daftar\n")

        if self.tugas:
            self.tampil()
        else:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru\n")
            return

    def rubah(self):

        if not self.tugas:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru")
            return

        self.tampil()
        print("00 - Batal merubah\n")
        while True:
            try:
                self.nomor_rubah = int(input("Tugas nomor berapa yang ingin dirubah? ")) - 1
                if self.nomor_rubah == '00':
                    break
                break
            except ValueError:
                print("Salah input! Masukan bilangan bulat!")

        if 0 <= self.nomor_rubah < len(self.tugas):
            self.tugas_baru = input("\nKetikan tugas baru : ")
            self.tugas[self.nomor_rubah] = self.tugas_baru
            self.save()
            print(f"Tugas No : {self.nomor_rubah + 1}\nBerhasil dirubah\n")

        if self.tugas:
            self.tampil()
        else:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru\n")
            return

    def save(self): #save kedalam file todo.txt

        with open("todo.txt", "w") as file:
            for baris in self.tugas:
                file.write(baris + "\n")

    def load(self): # ngeload todo.txt

        if os.path.exists("todo.txt"):
            with open("todo.txt", "r") as file:
                for baris in file:
                    self.tugas.append(baris.strip())
        return self.tugas
