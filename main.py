from module import SistemAntreanGigi, clear, header

def main():
    sistem = SistemAntreanGigi()

    while True:
        clear()
        header("SISTEM ANTREAN KLINIK GIGI")
        print("1. Tambah Pasien")
        print("2. Lihat Antrean")
        print("3. Layani Pasien")
        print("4. Cari Pasien")
        print("5. Hitung Pasien")
        print("6. Keluar")
        print("=" * 90)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            header("TAMBAH PASIEN BARU")

            nama = input("Nama Pasien: ")

            while True:
                try:
                    usia = int(input("Usia: "))

                    if usia <= 0:
                        print("Usia harus lebih dari 0.")
                        continue

                    break

                except ValueError:
                    print("Usia harus berupa angka.")

            keluhan = sistem.pilih_keluhan()

            sistem.tambah_pasien(nama, usia, keluhan)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":
            sistem.lihat_antrean()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "3":
            sistem.layani_pasien()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "4":
            try:
                id = int(input("Masukkan ID Pasien: "))
                sistem.cari_pasien(id)
            except ValueError:
                print("ID harus berupa angka.")
                continue
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "5":
            sistem.hitung_pasien()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem ini.")
            break

        else:
            print("Pilihan menu tidak valid.")
            input("\nTekan Enter untuk kembali...")


if __name__ == "__main__":
    main()