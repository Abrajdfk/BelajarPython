class Segitiga:

    def __int__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi


    def get_luas(self):
            return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(5, 10)
segitiga2 = Segitiga(19, 19)

print('luas segitiga 1 :', segitiga1.get_luas())