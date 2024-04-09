print("=====Kalkulator=====")

angka1 = float(input("Masukkan angka pertama : "))
angka2 = float(input("Masukkan angka kedua : "))
operator = input("Pilih operatornya(+,-,x,/) : ")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari penjumlahan {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari pengurangan {angka1} - {angka2} = {hasil}")
elif operator == "x":
    hasil = angka1 * angka2
    print(f"Hasil dari perkalian {angka1} x {angka2} = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil dari pembagian {angka1} / {angka2} = {hasil}")
else:
    print("ente kadang kadang ente")
