# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:28:45 2025

@author: Sueda
"""

#Yaşı girilen kişi çocuk mu yetişkin mi
yas=input("Yaşınızı giriniz:")
yas2=int(yas)
if yas2>18:
    print("Yetişkinsiniz.")
elif yas2<18:
    print("Çocuksunuz.")
else:
    print("18 yaşındasınız.")
    
#Girilen sayı tek mi çift mi
sayi=input("Bir sayı giriniz:")
sayi1=int(sayi)
if sayi1%2==0:
    print(f"{sayi1} çift bir sayıdır.")
else:
    print(f"{sayi1} tek bir sayıdır.")
     
#Girilen pozitif mi negatif mi yoksa sıfır mı
sayi=int(input("Bir sayı giriniz:"))
if sayi>0:
    print(f"{sayi1} pozitif bir sayıdır.")
elif sayi<0:
    print(f"{sayi1} negatif bir sayıdır.")
else:
    print("Sayı sıfırdır.")
    

teksayilar=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(teksayilar[0:6])
print(teksayilar[1:6])
print(teksayilar[2:6])
print(teksayilar[3:6]) 
    
#harf değiştirme
ornek=["K","O","D"]
print(ornek)
ornek[2]="T"
print(ornek)
print(len(ornek))

#in, içinde olup olmadığını kontrol ediyor
renkler=["mavi","yeşil","kırmızı","beyaz"]
print("mavi" in renkler)

renkler=["mavi","yeşil","kırmızı","beyaz"]
if "beyaz" in renkler:
    print("beyaz var")
else:
    print("beyaz yok")
    
#sonuna ekleme
renkler=["mavi","yeşil","kırmızı","beyaz"]
renkler.append("sarı")
print(renkler)
print(len(renkler))

#birleştirme
renkler=["mavi","yeşil","kırmızı","beyaz"]
mobilyalar=["koltuk","yatak","beşik"]
renkler.extend(mobilyalar)
print(renkler)

#istediğinin önüne ekleme
renkler=["mavi","yeşil","kırmızı","beyaz"]
renkler.insert(3, "şeftali")
print(renkler)
    
#kaldırma
renkler=["mavi","yeşil","kırmızı","beyaz"]
renkler.remove("yeşil")
print(renkler)

#istediğin elemanı silme
renkler=["mavi","yeşil","kırmızı","beyaz"]
renkler.pop(2)
print(renkler)
    
#listeyi boşaltıyor
renkler=["mavi","yeşil","kırmızı","beyaz"]
renkler.clear()
print(renkler)

renkler=["mavi","yeşil","kırmızı","mavi","beyaz"]
renkler.count("mavi")
print(renkler)
