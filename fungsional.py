def input_alas_dan_tinggi ():
    alas = float(input('Masukan Alas :'))
    Tinggi = float(input('Masukan Tinggi :'))

    return alas, tinggi


def hitung_luas (alas, Tinggi):
    return 0.5 * alas * Tinggi

print( hitung_luas(7, 10))