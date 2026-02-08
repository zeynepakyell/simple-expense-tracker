def gider_ekle(miktar, kategori):
    with open("harcamalar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{miktar},{kategori}\n")
    print("Gider başarıyla kaydedildi!")

def giderleri_goster():
    print("\n--- Harcama Listesi ---")
    toplam = 0
    try:
        with open("harcamalar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                miktar, kategori = satir.strip().split(",")
                print(f"Kategori: {kategori} - Miktar: {miktar} TL")
                toplam += float(miktar)
        print(f"-----------------------\nToplam Harcama: {toplam} TL")
    except FileNotFoundError:
        print("Henüz kaydedilmiş bir harcama yok.")

def ana_menu():
    while True:
        print("\n--- Gider Takip Sistemi ---")
        print("1. Gider Ekle")
        print("2. Giderleri Listele")
        print("3. Çıkış")
        secim = input("Seçiminiz (1/2/3): ")
        if secim == "1":
            miktar = input("Harcama miktarı: ")
            kategori = input("Harcama kategorisi: ")
            gider_ekle(miktar, kategori)
        elif secim == "2":
            giderleri_goster()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    ana_menu()