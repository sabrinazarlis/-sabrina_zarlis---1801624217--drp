from datetime import datetime

print('=== Aplikasi Manajemen Aktivitas ===')

aktivitas = input('Masukkan aktivitas: ')
aktivitas = aktivitas.lower()

if aktivitas == 'sarapan':

    print('Menu tersedia: telur, ikan, nugget, roti, mie, susu, martabak, bubur, nasi goreng')

    menu = input('Masukkan menu sarapan: ')
    menu = menu.lower()

    if menu == 'telur' or menu == 'ikan' or menu == 'nugget':
        print('Bahan tersedia, silakan dimasak terlebih dahulu')
        print('Jangan lupa sarapan agar lebih semangat!')

    elif menu == 'roti' or menu == 'mie' or menu == 'martabak':
        print('Menu dapat langsung disajikan')
    
    elif menu == 'bubur' or menu == 'nasi goreng' or menu == 'susu':
        print('menu sangat enak')
        print('semangat menjalani hari')

    else:
        print('Bahan tidak tersedia, silakan membeli terlebih dahulu')

elif aktivitas == 'kerja':

    waktu_sekarang = datetime.now()

    jam = waktu_sekarang.hour
    menit = waktu_sekarang.minute

    print('Waktu sekarang:', jam, ':', menit)

    if jam > 8 or (jam == 8 and menit > 0):
        print('Anda terlambat masuk kerja')

    else:
        print('Anda belum terlambat masuk kerja')
        print('Semangat bekerja hari ini!')

else:
    print('Aktivitas tidak tersedia')