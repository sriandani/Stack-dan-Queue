from collections import deque

antrian = deque()

while True:
    print("\n--- Simulasi Antrian Restoran ---")
    print("1. Tambah pelanggan ke antrian")
    print("2. Layani pelanggan")
    print("3. Tampilkan antrian")
    print("4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        nama = input("Masukkan nama pelanggan: ")
        antrian.append(nama)
        print(f"Pelanggan {nama} ditambahkan ke antrian.")
    
    elif pilihan == "2":
        if antrian:
            dilayani = antrian.popleft()  
            print(f"Pelanggan {dilayani} sedang dilayani.")
        else:
            print("Antrian kosong! Tidak ada pelanggan untuk dilayani.")
    
    elif pilihan == "3":
        if antrian:
            print("Antrian saat ini:", list(antrian))
        else:
            print("Antrian kosong.")
    
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    
    else:
        print("Opsi tidak valid!")
