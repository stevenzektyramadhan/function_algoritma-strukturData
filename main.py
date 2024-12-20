
def title(nama):
    print(f"hello {nama}, selamat pagi")
  
  
title("steven")

# fungsi aritmatika
def segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas
    
    
def persegi(sisi):
    luas = sisi**2 # karena luas persegi = sisi x sisi, itu sama saja dengan sisi^2
    return luas
    
def vol_persegi(sisi):
    volume = sisi**3
    return volume

def vol_lingkaran(jari, tinggi):
    if jari % 7 == 0:
        volume = 22/7 * jari**2 *tinggi
    else:
        volume = 3.14 * jari**2 * tinggi
        
    return volume

luas = vol_persegi(5)
print(luas)


# Mencari faktor bilangan



