# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:58:33 2025

@author: Sueda
"""

#iki sınav sonucu ve bir performans notu bulunan öğrencinin başarılı olup olmadığını hesaplama
sinav1=int(input("1. Sınav notu:"))
sinav2=int(input("2. Sınav notu:"))
performans=int(input("Performans notu:"))

ortalama=(sinav1+sinav2+performans)/3

if ortalama>=50:
    print("Başarılı.")
else:
    print("Başarısız.")
    
    
#üç iç açısı girilen geometrik şekil üçgen mi değil mi
aci1=int(input("Birinci açıyı giriniz:"))
aci2=int(input("İkinci açıyı giriniz:"))
aci3=int(input("Üçüncü açıyı giriniz:"))

toplamaci=aci1+aci2+aci3

if toplamaci==180:
    print("Bu bir üçgendir.")
else:
    print("Bu bir üçgen değildir.")
    
    
#20kg'dan fazla bagaj ağrılığı olanların ödemesi gereken ek ücretin hesaplanması
bagaj_agirligi=int(input("Bagaj ağırlığını giriniz:"))

if bagaj_agirligi<=20:
    print("Ek ücret ödemenize gerek yok.")
else:
    ek_agirlik=int(bagaj_agirligi-20)
    ek_ucret=ek_agirlik*10
    print(f"Fazla bagaj için {ek_ucret} TL ödemelisiniz.")
    
    