import time

data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "nilai_akhir": nilai_akhir}
    print("Data berhasil ditambahkan!")
    time.sleep(1)

def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    if nim in data_mahasiswa:
        print("Data saat ini:", data_mahasiswa[nim])
        nama = input("Masukkan Nama baru: ")
        tugas = float(input("Masukkan Nilai Tugas baru: "))
        uts = float(input("Masukkan Nilai UTS baru: "))
        uas = float(input("Masukkan Nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "nilai_akhir": nilai_akhir}
        print("Data berhasil diubah!")
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)

def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)

def lihat_data():
    if data_mahasiswa:
        print("Daftar Nilai Mahasiswa")
        print("-----------------------------------------------------------------------------------------")
        print("| NO | NIM           | NAMA                 | TUGAS    | UTS      | UAS      | AKHIR    |")
        print("-----------------------------------------------------------------------------------------")
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:<2} | {nim:<13} | {data['nama']:<20} | {data['tugas']:<8.2f} | {data['uts']:<8.2f} | {data['uas']:<8.2f} | {data['nilai_akhir']:<8.2f} |")
            print("-----------------------------------------------------------------------------------------")
    else:
        print("Daftar Nilai Mahasiswa")
        print("-----------------------------------------------------------------------------------------")
        print("| NO | NIM           | NAMA                 | TUGAS    | UTS      | UAS      | AKHIR    |")
        print("-----------------------------------------------------------------------------------------")
        print("|                                    TIDAK ADA DATA                                     |")
        print("-----------------------------------------------------------------------------------------")
    time.sleep(1)

def cari_data():
    nim = input("Masukkan NIM mahasiswa yang dicari: ")
    if nim in data_mahasiswa:
        print("Data ditemukan:", data_mahasiswa[nim])
    else:
        print("Data tidak ditemukan.")
    time.sleep(1)

def menu():
    while True:
        pilihan = input("[ (T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar ]: ")

        if pilihan == 't':
            tambah_data()
        elif pilihan == 'u':
            ubah_data()
        elif pilihan == 'h':
            hapus_data()
        elif pilihan == 'l':
            lihat_data()
        elif pilihan == 'c':
            cari_data()
        elif pilihan == 'k':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        time.sleep(1)

if __name__ == "__main__":
    menu()
