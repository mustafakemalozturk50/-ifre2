import random

harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Karakter uzunluğunu giriniz:"))
sifre = ""

for i in range (uzunluk):
    eklenecek_harf = random.choice(harfler)
    sifre = sifre + eklenecek_harf
print(sifre)
