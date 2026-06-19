from datetime import datetime

class Pasien:
    def __init__(self, id, nama, usia, keluhan):
        self.id = id
        self.nama = nama
        self.usia = usia
        self.keluhan = keluhan
        self.waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"ID: {self.id:03d} | Nama: {self.nama} | Usia: {self.usia} | Keluhan: {self.keluhan} | Waktu: {self.waktu}"


class SistemAntreanGigi:
    KELUHAN = [
        "Sakit Gigi",
        "Gigi Berlubang",
        "Kontrol Behel",
        "Cabut Gigi",
        "Pembersihan Karang Gigi",
        "Lainnya"
    ]

    def __init__(self):
        self.antrean = []
        self.id_berikutnya = 1

    def pilih_keluhan(self):
        print("\n" + "=" * 40)
        print(" PILIH KELUHAN PASIEN ")
        print("=" * 40)

        for i, keluhan in enumerate(self.KELUHAN, start=1):
            print(f"{i}. {keluhan}")

        print("=" * 40)

        while True:
            try:
                pilihan = int(input("Pilih keluhan: "))

                if 1 <= pilihan <= len(self.KELUHAN):
                    if self.KELUHAN[pilihan - 1] == "Lainnya":
                        return input("Masukkan keluhan: ")

                    return self.KELUHAN[pilihan - 1]

                print("Pilihan tidak valid.")

            except ValueError:
                print("Silakan masukkan angka.")

    def tambah_pasien(self, nama, usia, keluhan):
        pasien = Pasien(self.id_berikutnya, nama, usia, keluhan)
        self.antrean.append(pasien)
        self.id_berikutnya += 1

    def lihat_antrean(self):
        print("\n" + "=" * 90)
        print(f"{'No':<5}{'ID':<5}{'Nama':<20}{'Usia':<10}{'Keluhan':<25}{'Waktu'}")
        print("=" * 90)

        for posisi, pasien in enumerate(self.antrean, start=1):
            print(
                f"{posisi:<5}"
                f"{pasien.id:<5}"
                f"{pasien.nama:<20}"
                f"{pasien.usia:<10}"
                f"{pasien.keluhan:<25}"
                f"{pasien.waktu}"
            )

        print("=" * 90)

    def layani_pasien(self):
        if not self.antrean:
            print("\nAntrean kosong.")
            return

        pasien = self.antrean.pop(0)

        print("\n===== SEDANG DILAYANI =====")
        print(pasien)

    def cari_pasien(self, id):
        for pasien in self.antrean:
            if pasien.id == id:
                print("\n===== PASIEN DITEMUKAN =====")
                print(pasien)
                return

        print("Pasien tidak ditemukan.")

    def hitung_pasien(self):
        print(f"\nTotal pasien dalam antrean: {len(self.antrean)}")