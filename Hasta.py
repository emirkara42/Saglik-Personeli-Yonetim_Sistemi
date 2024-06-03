class Hasta:

    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def get_hasta_no(self):
        return self.__hasta_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def get_tedavi(self):
        return self.__tedavi
    
    def set_hasta_no(self, yeni_hasta_no):
        self.__hasta_no = yeni_hasta_no

    def set_ad(self, yeni_ad):
        self.__ad = yeni_ad

    def set_soyad(self, yeni_soyad):
        self.__soyad = yeni_soyad

    def set_dogum_tarihi(self, yeni_dogum_tarihi):
        self.__dogum_tarihi = yeni_dogum_tarihi

    def set_hastalik(self, yeni_hastalik):
        self.__hastalik = yeni_hastalik

    def set_tedavi(self, yeni_tedavi):
        self.__tedavi = yeni_tedavi
    
    def tedavi_suresi_hesapla(self, hastalik):
        if hastalik == "Migren":
            return 5
        elif hastalik == "Diabet":
            return 7
        elif hastalik == "Astim":
            return 12
        else: 
            return None
        
    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Dogum Tarihi: {self.__dogum_tarihi}, Hastalik: {self.__hastalik}, Tedavi: {self.__tedavi}"
