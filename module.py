from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(judul):
    lebar = 90

    print("\n" + "=" * lebar)
    print(judul.center(lebar))
    print("=" * lebar)

class Pasien:
    def __init__(self, id, nama, usia, keluhan):
        self.id = id
        self.nama = nama
        self.usia = usia
        self.keluhan = keluhan
        self.waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"ID: {self.id} Nama: {self.nama} Usia : {self.usia} Keluhan: {self.keluhan} Waktu: {self.waktu}"
    
    def tampilkan_detail(self):
        print(f"ID      : {self.id}")
        print(f"Nama    : {self.nama}")
        print(f"Usia    : {self.usia}")
        print(f"Keluhan : {self.keluhan}")
        print(f"Waktu   : {self.waktu}")


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
        header("PILIH KELUHAN PASIEN")

        for i, keluhan in enumerate(self.KELUHAN, start=1):
            print(f"{i}. {keluhan}")

        print("=" * 90)

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

        header("PASIEN DILAYANI")
        pasien.tampilkan_detail()
        print("=" * 90)

    def cari_pasien(self, id):
        for pasien in self.antrean:
            if pasien.id == id:
                header("PASIEN DITEMUKAN")

                pasien.tampilkan_detail()
                print("=" * 90)
                return

        print("Pasien tidak ditemukan.")

    def hitung_pasien(self):
        print("\n" + "=" * 90)
        print(f"Total pasien dalam antrean: {len(self.antrean)}")
        print("=" * 90)