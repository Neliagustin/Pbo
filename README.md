# 1. Impor kelas yang diperlukan
class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NPM:", self.npm)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            mahasiswa.tampilkan_info()


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
# 2. Buat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# 4. Buat objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa("Neli Agustin", "G1A022048", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_1)

# 5. Tampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()
print(" ")
# 6. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
