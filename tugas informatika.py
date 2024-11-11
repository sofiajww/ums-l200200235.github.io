class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_terbayar = False
        self.absensi = 0
        self.tugas = []
        self.uts = None
        self.uas = None
        self.nilai_akhir = None

    def bayar_spp(self):
        print(f"{self.nama} telah membayar SPP.")
        self.spp_terbayar = True

    def hadir_kuliah(self):
        if self.spp_terbayar:
            print(f"{self.nama} hadir dalam perkuliahan.")
            self.absensi += 1
        else:
            print(f"{self.nama} belum membayar SPP, tidak dapat mengikuti kuliah.")

    def kerjakan_tugas(self, nilai_tugas):
        if self.spp_terbayar:
            print(f"{self.nama} mengerjakan tugas dan mendapatkan nilai {nilai_tugas}.")
            self.tugas.append(nilai_tugas)
        else:
            print(f"{self.nama} belum membayar SPP, tidak dapat mengerjakan tugas.")

    def ikut_uts(self, nilai):
        if self.spp_terbayar:
            print(f"{self.nama} mengikuti UTS dan mendapatkan nilai {nilai}.")
            self.uts = nilai
        else:
            print(f"{self.nama} belum membayar SPP, tidak dapat mengikuti UTS.")

    def ikut_uas(self, nilai):
        if self.spp_terbayar:
            print(f"{self.nama} mengikuti UAS dan mendapatkan nilai {nilai}.")
            self.uas = nilai
        else:
            print(f"{self.nama} belum membayar SPP, tidak dapat mengikuti UAS.")

    def hitung_nilai_akhir(self):
        if self.uts is not None and self.uas is not None and self.tugas:
            rata_tugas = sum(self.tugas) / len(self.tugas)
            self.nilai_akhir = (0.3 * rata_tugas) + (0.3 * self.uts) + (0.4 * self.uas)
            print(f"Nilai akhir {self.nama} adalah: {self.nilai_akhir:.2f}")
        else:
            print(f"{self.nama} belum menyelesaikan semua komponen penilaian.")

    def status_kelulusan(self):
        if self.nilai_akhir is not None:
            if self.nilai_akhir >= 60:
                print(f"{self.nama} dinyatakan lulus dengan nilai akhir {self.nilai_akhir:.2f}.")
            else:
                print(f"{self.nama} dinyatakan tidak lulus dengan nilai akhir {self.nilai_akhir:.2f}.")
        else:
            print("Nilai akhir belum dihitung.")


# Simulasi proses mengikuti kuliah
mahasiswa1 = Mahasiswa("Sofi", "L200220235")

# Langkah-langkah simulasi
mahasiswa1.bayar_spp()
mahasiswa1.hadir_kuliah()
mahasiswa1.kerjakan_tugas(85)
mahasiswa1.kerjakan_tugas(90)
mahasiswa1.hadir_kuliah()
mahasiswa1.ikut_uts(78)
mahasiswa1.ikut_uas(88)
mahasiswa1.hitung_nilai_akhir()
mahasiswa1.status_kelulusan()
