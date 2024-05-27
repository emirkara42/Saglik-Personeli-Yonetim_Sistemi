from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        personel1 = Personel(1, "Ali", "Veli", "IT", 5000)
        print(personel1)

        doktor1 = Doktor(2, "Ayşe", "Yılmaz", "Cerrahi", 10000, "Genel Cerrah", 10, "XYZ Hastanesi")
        doktor2 = Doktor(3, "Fatma", "Demir", "Dahiliye", 9500, "İç Hastalıkları", 7, "ABC Hastanesi")
        doktor3 = Doktor(4, "Mehmet", "Çelik", "Pediatri", 9000, "Çocuk Sağlığı", 5, "DEF Hastanesi")
        print(doktor1)
        print(doktor2)
        print(doktor3)

        hemsire1 = Hemsire(5, "Selin", "Kaya", "Acil", 6000, 40, "Yoğun Bakım", "XYZ Hastanesi")
        hemsire2 = Hemsire(6, "Can", "Yılmaz", "Kardiyoloji", 6500, 45, "Kardiyovasküler", "ABC Hastanesi")
        hemsire3 = Hemsire(7, "Ezgi", "Gül", "Nöroloji", 6200, 42, "Nörolojik Bakım", "DEF Hastanesi")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        hasta1 = Hasta(8, "Zeynep", "Taş", "1990-05-12", "Migren", "İlaç Tedavisi")
        hasta2 = Hasta(9, "Ahmet", "Kara", "1985-07-23", "Diabet", "İnsülin Tedavisi")
        hasta3 = Hasta(10, "Ece", "Aydın", "2000-02-14", "Astım", "Solunum Tedavisi")
        print(hasta1)
        print(hasta2)
        print(hasta3)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
