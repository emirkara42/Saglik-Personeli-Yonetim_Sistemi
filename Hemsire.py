from Personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane
    
    def set_calisma_saati(self, yeni_calisma_saati):
        self.__calisma_saati = yeni_calisma_saati

    def set_sertifika(self, yeni_sertifika):
        self.__sertifika = yeni_sertifika

    def set_hastane(self, yeni_hastane):
        self.__hastane = yeni_hastane

    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (1 + 40 / 100)
        self.set_maas(yeni_maas)

    def __str__(self):
        return f"{super().__str__()}, Çalisma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
