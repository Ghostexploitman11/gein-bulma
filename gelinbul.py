import random
import time
import sys


isim = input("İsminizi giriniz: ")


dosya_yolu = "/root/Desktop/gelin bulma/gelinisimi.txt"


with open(dosya_yolu, 'r', encoding='utf-8') as file:
    isimler = file.readlines()


isimler = [isim.strip() for isim in isimler]


rastgele_isim = random.choice(isimler)

print(isim + " " + "bey için gelin aranıyor", end="", flush=True)


for _ in range(30):
    print(".", end="", flush=True)
    time.sleep(1)  # 1 saniye bekle


print("\n" + isim + " " + "bey  için gelin bulundu: " + rastgele_isim)
