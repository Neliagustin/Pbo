'''class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NPM:", self.npm)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan:", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print(mahasiswa.nama, "-", mahasiswa.npm)


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


# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas

# Kelas Mahasiswa merepresentasikan data mahasiswa di universitas.
# Setiap objek Mahasiswa memiliki atribut nama, nim, dan jurusan.

# Kelas Jurusan merepresentasikan data jurusan di universitas.
# Setiap objek Jurusan memiliki atribut nama jurusan dan daftar mahasiswa.

# Kelas Universitas merepresentasikan data universitas.
# Setiap objek Universitas memiliki atribut nama universitas dan daftar jurusan.

# 2. Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# 4. Membuat objek Mahasiswa dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa1 = Mahasiswa("Neli Agustin", "G1A022048", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)

# 5. Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()'''


