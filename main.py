# aplikasi to-do list

import todolist

nama = input("Silahkan ketikan nama anda : ")
print("")
tugas = []
tugasku = todolist.todo(tugas)

if __name__ == '__main__':

    print(f"Selamat datang, {nama}!")
    print("Ini adalah aplikasi to-do list\n")

    while True:

        print("Menu to-do list : \n")
        print("1. Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. keluar aplikasi\n")

        opsi = input("Pilih 1 / 2 / 3 / 4 : ")

        if opsi == "1":
            tugasku.tampil()
        elif opsi == "2":
            tugasku.tambah()
        elif opsi == "3":
            tugasku.hapus()
        elif opsi == "4":
            print(f"Terima kasih, {nama}!")
            break
        else:
            print(f"Maaf kak, tidak ada pilihan [{opsi}]")
            print("Coba pilih dari 1 - 4")