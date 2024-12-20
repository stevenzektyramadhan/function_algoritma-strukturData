buku = ["atomic habit","filosofi teras","educated"]

def show_data():
    if len(buku) <= 0:
        print("belum ada data buku")
    else:
        for index  in range(len(buku)):
            print("[%d] %s" %(index, buku[index]))
            
def insert_buku():
    data = input("masukan judul buku: ")
    buku.append(data)
    print("data berhasil ditambkan")
    
def edit_data():
    show_data()
    index = int(input("inputkan id buku: "))
    if index > len(buku):
        print("id salah")
    else:
        judul_baru = input("judul baru")
        buku[index] = judul_baru
        print("yeyyy,,,buku berhasil di Update \n")
        
def delete_data():
    show_data()
    index = int(input("inputkan id buku "))
    if index > len(buku):
        print("id salah")
    else:
        buku.remove(buku[index])
        
def show_menu():
    while True:
        user = input("\n\n----- Menu -----\n1. Menampilkan data buku\n2. Edit data buku\n3. Hapus data buku\n4. Tambah buku\n Masukan pilihan anda: ")
        if int(user) == 1:
            print("Berikut ini data buku yang tersimpan: ")
            show_data()
        elif int(user) == 2 :
            edit_data()
        elif int(user) == 3 :
            delete_data()
        elif int(user) == 4:
            insert_buku()
        else:
            break
        

if __name__ == "__main__":
    show_menu() 