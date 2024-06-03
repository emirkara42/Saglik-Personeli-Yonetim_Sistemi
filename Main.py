from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

def dataframe_olustur(personel_listesi, doktor_listesi, hemsire_listesi, hasta_listesi):
    data = {
        'personel_no': [],
        'ad': [],
        'soyad': [],
        'departman': [],
        'maas': [],
        'uzmanlik': [],
        'deneyim_yili': [],
        'hastane': [],
        'calisma_saati': [],
        'sertifika': [],
        'hasta_no': [],
        'dogum_tarihi': [],
        'hastalik': [],
        'tedavi': []
    }

    for personel in personel_listesi:
        data['personel_no'].append(personel.get_personel_no())
        data['ad'].append(personel.get_ad())
        data['soyad'].append(personel.get_soyad())
        data['departman'].append(personel.get_departman())
        data['maas'].append(personel.get_maas())
        data['uzmanlik'].append(None)
        data['deneyim_yili'].append(None)
        data['hastane'].append(None)
        data['calisma_saati'].append(None)
        data['sertifika'].append(None)
        data['hasta_no'].append(None)
        data['dogum_tarihi'].append(None)
        data['hastalik'].append(None)
        data['tedavi'].append(None)

    for doktor in doktor_listesi:
        data['personel_no'].append(doktor.get_personel_no())
        data['ad'].append(doktor.get_ad())
        data['soyad'].append(doktor.get_soyad())
        data['departman'].append(doktor.get_departman())
        data['maas'].append(doktor.get_maas())
        data['uzmanlik'].append(doktor.get_uzmanlik())
        data['deneyim_yili'].append(doktor.get_deneyim_yili())
        data['hastane'].append(doktor.get_hastane())
        data['calisma_saati'].append(None)
        data['sertifika'].append(None)
        data['hasta_no'].append(None)
        data['dogum_tarihi'].append(None)
        data['hastalik'].append(None)
        data['tedavi'].append(None)

    for hemsire in hemsire_listesi:
        data['personel_no'].append(hemsire.get_personel_no())
        data['ad'].append(hemsire.get_ad())
        data['soyad'].append(hemsire.get_soyad())
        data['departman'].append(hemsire.get_departman())
        data['maas'].append(hemsire.get_maas())
        data['uzmanlik'].append(None)
        data['deneyim_yili'].append(None)
        data['hastane'].append(hemsire.get_hastane())
        data['calisma_saati'].append(hemsire.get_calisma_saati())
        data['sertifika'].append(hemsire.get_sertifika())
        data['hasta_no'].append(None)
        data['dogum_tarihi'].append(None)
        data['hastalik'].append(None)
        data['tedavi'].append(None)

    for hasta in hasta_listesi:
        data['personel_no'].append(None)
        data['ad'].append(hasta.get_ad())
        data['soyad'].append(hasta.get_soyad())
        data['departman'].append(None)
        data['maas'].append(None)
        data['uzmanlik'].append(None)
        data['deneyim_yili'].append(None)
        data['hastane'].append(None)
        data['calisma_saati'].append(None)
        data['sertifika'].append(None)
        data['hasta_no'].append(hasta.get_hasta_no())
        data['dogum_tarihi'].append(hasta.get_dogum_tarihi())
        data['hastalik'].append(hasta.get_hastalik())
        data['tedavi'].append(hasta.get_tedavi())

    df = pd.DataFrame(data)
    return df

def dataframe_islemleri(df):
    #Bos olan degisken degerleri icin 0 atama.
    df.fillna(0, inplace=True)

    #Uzmanlik sutununa gore gruplama ve .size() ile bunların adedi.
    doktor_sayilari = df.groupby('uzmanlik').size() 
    doktor_sayilari = doktor_sayilari[doktor_sayilari.index != 0] #0'a esit olmayanlardan yeni bir df
    print("\nDoktor Sayilari (Uzmanlik Alanina Göre):")

    print(doktor_sayilari)
    #df[df[...] > ...] kiyaslama yapilirken kullanilir ve shape[0] bunlarin satir sayisini dondurur.
    deneyimli_doktorlar = df[df['deneyim_yili'] > 5].shape[0]
    print(f"\n5 Yildan Fazla Deneyime Sahip Doktor Sayisi: {deneyimli_doktorlar}")

    #Hasta isimlerini alfabetik siralama.
    hasta_alfabetik = df[df['hasta_no'] != 0].sort_values(by='ad') #Hasta no 0 olmayan satirlari .sortvalues(by="ad") ile siralama. ascending= False olsa tersine siralar.
    print("\nHasta Adina Göre Alfabetik Siralanmis Liste:")
    print(hasta_alfabetik[['hasta_no', 'ad', 'soyad']]) #Yalnizca bu sütunları bastir.

    #Maasi 7000 den buyuk olan personel bastir.
    yuksek_maas_personel = df[df['maas'] > 7000]
    print("\nMaasi 7000 TL Üzerinde Olan Personel:")
    print(yuksek_maas_personel[['personel_no', 'ad', 'soyad', 'maas']]) #Yalnizca bu sütunları bastir.

    #pandas DateTime nenelerine dondurulen degerler Timestamp ile karsilastirilir --> True, False doner
    yeni_hastalar = df[pd.to_datetime(df['dogum_tarihi']) > pd.Timestamp('1990-01-01')]
    print("\n1990 ve Sonrasinda Doğan Hastalar:")
    print(yeni_hastalar[['hasta_no', 'ad', 'soyad', 'dogum_tarihi']])

    yeni_dataframe = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastane', 'hastalik', 'tedavi']]
    print("\nYeni DataFrame:")
    print(yeni_dataframe)

def main():
    personel_listesi = [
        Personel(1, "Emir", "Kara", "IT", 45000),
        Personel(2, "Ada", "Gok", "Ozluk", 50000)
    ]
    print(personel_listesi[0])
    print(personel_listesi[1])

    doktor_listesi = [
        Doktor(3, "İrem", "Kara", "Cerrahi", 90000, "Genel Cerrah", 10, "Çiğli Devlet Hastanesi"),
        Doktor(4, "Seçil", "Erdal", "Dahiliye", 80000, "İç Hastaliklari", 7, "Menemen Devlet Hastanesi"),
        Doktor(5, "Tarik", "Dincsoy", "Pediatri", 75000, "Çocuk Sağliği", 5, "Karşiyaka Devlet Hastanesi")
    ]
    print(doktor_listesi[0])
    print(doktor_listesi[1])
    print(doktor_listesi[2])
    
    hemsire_listesi = [
        Hemsire(6, "Gorkem", "Kiristioglu", "Acil", 75000, 40, "Yoğun Bakim", "Karşiyaka Devlet Hastanesi"),
        Hemsire(7, "Deniz", "Altun", "Kardiyoloji", 65000, 45, "Kardiyovasküler", "Çiğli Devlet Hastanesi"),
        Hemsire(8, "Berkan", "Ilbayli", "Nöroloji", 65000, 42, "Nörolojik Bakim", "Menemen Devlet Hastanesi")
    ]
    print(hemsire_listesi[0])
    print(hemsire_listesi[1])
    print(hemsire_listesi[2])

    hasta_listesi = [
        Hasta(9, "Yagmur", "Eren", "2002-02-02", "Migren", "İlaç Tedavisi"),
        Hasta(10, "Fatma", "Gok", "1965-05-05", "Diabet", "İnsülin Tedavisi"),
        Hasta(11, "Mehmed", "Cakirdiken", "1980-08-08", "Astim", "Solunum Tedavisi")
    ]
    print(hasta_listesi[0])
    print(hasta_listesi[1])
    print(hasta_listesi[2])

    df = dataframe_olustur(personel_listesi, doktor_listesi, hemsire_listesi, hasta_listesi)
    dataframe_islemleri(df)

if __name__ == "__main__":
    main()
