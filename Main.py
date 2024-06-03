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

def dataframe_islemleri():
    pass

def main():
    personel_listesi = [
        Personel(123456789, "Emir", "Kara", "IT", 45000)
    ]

    doktor_listesi = [
        Doktor(213456789, "İrem", "Kara", "Cerrahi", 90000, "Genel Cerrah", 10, "Çiğli Devlet Hastanesi"),
        Doktor(312456789, "Seçil", "Erdal", "Dahiliye", 80000, "İç Hastaliklari", 7, "Menemen Devlet Hastanesi"),
        Doktor(412356789, "Tarik", "Dincsoy", "Pediatri", 75000, "Çocuk Sağliği", 5, "Karşiyaka Devlet Hastanesi")
    ]

    hemsire_listesi = [
        Hemsire(512346789, "Gorkem", "Kiristioglu", "Acil", 75000, 40, "Yoğun Bakim", "Karşiyaka Devlet Hastanesi"),
        Hemsire(612345789, "Deniz", "Altun", "Kardiyoloji", 65000, 45, "Kardiyovasküler", "Çiğli Devlet Hastanesi"),
        Hemsire(712345689, "Berkan", "Ilbayli", "Nöroloji", 65000, 42, "Nörolojik Bakim", "Menemen Devlet Hastanesi")
    ]

    hasta_listesi = [
        Hasta(812345679, "Yagmur", "Eren", "02-11-2002", "Migren", "İlaç Tedavisi"),
        Hasta(912345678, "Fatma", "Gok", "21-01-1965", "Diabet", "İnsülin Tedavisi"),
        Hasta(102345678, "Mehmed", "Cakirdiken", "30-05-2980", "Astim", "Solunum Tedavisi")
    ]

    df = dataframe_olustur(personel_listesi, doktor_listesi, hemsire_listesi, hasta_listesi)
    print(df)
    #dataframe_islemleri(df)

if __name__ == "__main__":
    main()
