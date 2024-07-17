def parola_gucu_kontrol(parola):
    guc = 0
    if len(parola) >= 8:
        guc += 1
    if any(char.isdigit() for char in parola):
        guc += 1    
    if any(char.isupper() for char in parola):
        guc += 1  
    if any(char.islower() for char in parola):
        guc += 1
    ozel_karakterler = "!@#$%^&*()_+-=[]{};:,.<>?/~"
    if any(char in ozel_karakterler for char in parola):
        guc += 1
    return guc
parola = input("Parolanızı girin: ")
guc_degeri = parola_gucu_kontrol(parola)
if guc_degeri == 5:
    print("Parolanız çok güçlü!")
elif guc_degeri >= 3:
    print("Parolanız güçlü.")
elif guc_degeri >= 2:
    print("Parolanız orta derecede güçlü.")
elif guc_degeri >= 1:
    print("Parolanız zayıf.")
else:
    print("Parolanız çok zayıf! Daha güçlü bir parola belirleyin.")
