harga = int(input (""))
if harga == 1:
   tarif = 3500
elif harga == 2:
   tarif = 5500
elif harga == 3:
   tarif = 7500
else:
   print("null")
print ("Tarif parkir {} jam adalah : Rp{}" .format(harga, tarif))