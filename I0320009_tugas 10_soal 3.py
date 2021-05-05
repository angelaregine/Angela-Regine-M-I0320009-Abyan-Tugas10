print ("Program Biodata Diri")
print ("====================")

# Ambil input dari user
nama = input("Nama: ")
ttl = input("Tempat, tanggal lahir: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks
teks = "Nama: {}\nTempat, tanggal lahir: {}\nUmur: {}\nAlamat: {}".format(nama, ttl, umur, alamat)

# buka file untuk ditulis
file_bio = open("biodata.txt", "a")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()