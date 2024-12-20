def cari_faktor(n):
    hasil = []
    for i in range(1, n+1):
        if n % i == 0 :
            hasil.append(i)
        print(hasil)

cari_faktor(12)