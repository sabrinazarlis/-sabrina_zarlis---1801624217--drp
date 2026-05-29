user = input("Siapa nama Anda? ")

print(f"\n.1 Papan Catur Milik {user}")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("🟦", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n.2 ☘️  Daftar Aktivitas {user} ☘️")

daftar_aktivitas = []

jumlah_aktivitas = int(input("Berapa banyak aktivitas yang ingin Anda tambahkan (angka)? "))

for i in range(jumlah_aktivitas):
    print(f"\nAktivitas ke-{i+1}")

    nama_aktivitas = input("Nama aktivitas: ")
    waktu_aktivitas = input("Waktu aktivitas (jam): ")
    tempat_aktivitas = input("Tempat aktivitas: ")
    kategori = input("Kategori aktivitas: ")
    status = input("Status (Selesai/Belum Selesai): ")

    aktivitas = {
        "aktivitas": nama_aktivitas,
        "waktu": waktu_aktivitas,
        "tempat": tempat_aktivitas,
        "kategori": kategori,
        "status": status
    }

    daftar_aktivitas.append(aktivitas)

print("\n" + "=" * 50)
print(f"\n ☘️  Daftar Aktivitas {user} ☘️")
print("=" * 50)

selesai = 0

for i in range(len(daftar_aktivitas)):
    print(f"\nAKTIVITAS {i+1}")
    print(f"🌸 Nama Aktivitas : {daftar_aktivitas[i]['aktivitas']}")
    print(f"🌸 Waktu          : {daftar_aktivitas[i]['waktu']}")
    print(f"🌸 Tempat         : {daftar_aktivitas[i]['tempat']}")
    print(f"🌸 Kategori       : {daftar_aktivitas[i]['kategori']}")
    print(f"🌸 Status         : {daftar_aktivitas[i]['status']}")

    if daftar_aktivitas[i]['status'].lower() == "selesai":
        selesai += 1

print("\n" + "=" * 50)
print(f"\n ☘️  Ringkasan Aktivitas {user} ☘️")
print("=" * 50)
print(f"Total aktivitas        : {len(daftar_aktivitas)}")
print(f"Aktivitas selesai      : {selesai}")
print(f"Aktivitas belum selesai: {len(daftar_aktivitas) - selesai}")

if len(daftar_aktivitas) > 0:
    persentase = (selesai / len(daftar_aktivitas)) * 100
else:
    persentase = 0

print(f"Persentase selesai     : {persentase:.1f}%")

print(f"\n☘️  Kesimpulan Aktivitas {user} ☘️ ")

if persentase == 100:
    print("✨ Semua aktivitas telah selesai!")
elif persentase >= 50:
    print("🧸 Sebagian besar aktivitas telah selesai :).")
else:
    print("💪 Masih banyak aktivitas yang perlu diselesaikan.")