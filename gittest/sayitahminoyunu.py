import random

secilen_sayi = random.randint(1, 100)
tahmin_sayisi = 0

print("Sayı Tahmin Oyunu'na Hoşgeldiniz!")
print("1 ile 100 arasında bir sayı seçildi. Tahmininizi girin.\n")

while True:
    tahmin = int(input("Tahmininizi girin: "))
    tahmin_sayisi += 1

    if tahmin < secilen_sayi:
        print("Daha büyük bir sayı girin.")
    elif tahmin > secilen_sayi:
        print("Daha küçük bir sayı girin.")
    else:
        print(f"Tebrikler! {secilen_sayi} sayısını {tahmin_sayisi} tahminde doğru bildiniz!")
        break

