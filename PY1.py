# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:56:29 2025

@author: Sueda
"""

#Çemberin alanını ve çevresini hesaplama
PI=3.14
r=input("Çemberin yarıçapı:")
r2=int(r)
alan=PI*r2**2
cevre=2*r2*PI
print("Alan",alan, "Çevre",cevre)


#Dikdörtgenin alanı ve çevresini hesaplama
uzunKenar=input("Uzun kenarı giriniz:")
kisaKenar=input("Kısa kenarı giriniz:")
uzunKenar2=int(uzunKenar)
kisaKenar2=int(kisaKenar)
#
alan=uzunKenar2*kisaKenar2
#
cevre=(2*uzunKenar2)+(2*kisaKenar2)
print("Alan",alan,"Çevre",cevre)


#Üçgenin çevresini ve alanını hesaplama
taban=input("Tabanını giriniz:")
birinciKenar=input("Birinci kenarı giriniz:")
ikinciKenar=input("İkinci kenarı giriniz:")
yukseklik=input("Yüksekliği giriniz:")
#
taban2=int(taban)
birinciKenar2=int(birinciKenar)
ikinciKenar2=int(ikinciKenar)
yukseklik2=int(yukseklik)
#
alan=(taban2*yukseklik2)/2
cevre=birinciKenar2+ikinciKenar2+taban2
print("Alan",alan,"Çevre",cevre)


#Dairenin çevresini ve alanını hesaplama
tercih=input("Dairenin alanını mı yoksa çevresini mi hesaplamak istiyorsunuz? Alan için 1, çevre için 2 giriniz.")
PI=3.14
r=input("Yarıçap:")
r2=int(r)
if tercih=="1":
    alan=PI*r2**2
    print("Dairenin alanı",alan)
else:
    cevre=2*r2*PI
    print("Dairenin çevresi",cevre)
    