import random

kelimeler = ["meryem", "ceren", "bilgisayar", "telefon", "televizyon","kağıt","necati"]

gizli_kelime = random.choice(kelimeler)
tahmin_edilen_kelime = ["_"] * len(gizli_kelime)
yanlis_tahminler = []
can = 6

print("Kelime Tahmin Oyunu'na Hoşgeldiniz!")
print("Gizli kelime:", " ".join(tahmin_edilen_kelime))
print(f"{can} canınız var.\n")

while can > 0 and "_" in tahmin_edilen_kelime:
    tahmin = input("Bir harf tahmin edin: ").lower()

    if len(tahmin) != 1:
        print("Lütfen sadece bir harf girin!")
        continue

    if tahmin in tahmin_edilen_kelime or tahmin in yanlis_tahminler:
        print("Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin.")
        continue 

    if tahmin in gizli_kelime:
        for i, harf in enumerate(gizli_kelime):
            if harf == tahmin:
                tahmin_edilen_kelime[i] = tahmin
        print("Doğru tahmin!")
    else:
        yanlis_tahminler.append(tahmin)
        can -= 1
        print("Yanlış tahmin!")

    print("Gizli kelime:", " ".join(tahmin_edilen_kelime))
    print(f"Kalan can: {can}")
    print(f"Yanlış tahminler: {', '.join(yanlis_tahminler)}\n")

if "_" not in tahmin_edilen_kelime:
    print("Tebrikler! Kelimeyi doğru tahmin ettiniz:", gizli_kelime)
else:
    print("Maalesef, canınız bitti. Gizli kelime:", gizli_kelime)
