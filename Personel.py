class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    def get_personel_no(self):
        return self.__personel_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_departman(self):
        return self.__departman

    def get_maas(self):
        return self.__maas
    
    def set_personel_no(self, yeni_personel_no):
        self.__personel_no = yeni_personel_no

    def set_ad(self, yeni_ad):
        self.__ad = yeni_ad

    def set_soyad(self, yeni_soyad):
        self.__soyad = yeni_soyad

    def set_departman(self, yeni_departman):
        self.__departman = yeni_departman

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas

    def __str__(self):
        return f"Personel No: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maaş: {self.__maas}"
