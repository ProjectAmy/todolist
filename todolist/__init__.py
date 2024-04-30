class todo:

    def __init__(self, tugas):
        self.tugas = tugas
        self.tugas_baru = None
        self.nomor_hapus = None
        self.dihapus = None

    def tampil(self):

        if self.tugas: # ngecek ada isinya apa ndak
            print("Berikut adalah daftar tugas anda :")
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

    def hapus(self):

        if not self.tugas:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru")
            return

        print("")
        self.tampil()
        self.nomor_hapus = int(input("Tugas nomor berapa yang ingin dihapus?"))
        print("")

        if 1 <= self.nomor_hapus <= len(self.tugas):
            self.dihapus = self.tugas.pop(self.nomor_hapus - 1)
            print(f"Tugas : {self.dihapus}\nBerhasil dihapus dari daftar\n")

        if self.tugas:
            self.tampil()
        else:
            print("Belum ada tugas.\nSilahkan pilih opsi 2 untuk menambahkan tugas baru\n")
            return
