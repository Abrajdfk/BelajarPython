def salam():
    print("hello Muhammad Firmansyah")

salam()


def luas_persegi(sisi):
    luas = sisi * sisi
    return  luas
 #pemanggilan fungsi
print("luas persegi : %d" % luas_persegi(6))

# membuat variable global
nama = "Python"
versi = "1.0.0"

def help():
    # ini variable lokal
    nama = "C#"
    versi = "1.0.2"
    # mengakses variabel lokal
    print(" nama: %s" % nama)
    print("versi: %s" % versi)

# mengakses variable global
print(" nama: %s" % nama)
print("versi: %s" % versi)

# memanggil fungsi help()
help()

