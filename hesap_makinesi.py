x = float(input("Birinci sayıyı giriniz :"))
y = float(input("İkinci sayıyı giriniz :"))

islem = input("Yapmak istediğiniz işlemi giriniz ( +,-,*,/) : ").lower()
if islem == "+" :
    sonuc= x + y
    print(f"Sonuç:{sonuc}")
elif islem == "-" :
    sonuc = x - y
    print(f"Sonuç:{sonuc}")
elif islem == "*" :
    sonuc = x*y
    print(f"Sonuç:{sonuc}")
elif islem =="/" :
    if y != 0:
        sonuc = x/y
        print(f"Sonuç:{sonuc}")
    else:
        print("Bölme işlemi için ikinci sayı 0 olamaz")
else:
    print("Geçersiz işlem")

    
