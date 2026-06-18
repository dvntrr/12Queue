from module import SistemAntreanGigi

def main():
    sistem = SistemAntreanGigi()

    while True:
        print("\n===== SISTEM ANTREAN KLINIK GIGI =====")
        print("1. Tambah Pasien")
        print("2. Lihat Antrean")
        print("3. Layani Pasien")
        print("4. Cari Pasien")
        print("5. Hitung Pasien")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama Pasien: ")

            try:
                usia = int(input("Usia: "))
            except ValueError:
                print("Usia harus berupa angka.")
                continue

            keluhan = sistem.pilih_keluhan()

            sistem.tambah_pasien(nama, usia, keluhan)
            print("Pasien berhasil ditambahkan!")

        elif pilihan == "2":
            sistem.lihat_antrean()

        elif pilihan == "3":
            sistem.layani_pasien()

        elif pilihan == "4":
            try:
                id = int(input("Masukkan ID Pasien: "))
                sistem.cari_pasien(id)
            except ValueError:
                print("ID harus berupa angka.")

        elif pilihan == "5":
            sistem.hitung_pasien()

        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem ini.")
            break

        else:
            print("Pilihan menu tidak valid.")


if __name__ == "__main__":
    main()