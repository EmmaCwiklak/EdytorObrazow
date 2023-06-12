"""
Transformaca pomiędzy przestrzeniami barw,
Negatyw,
Po binaryzacji:
	Erozja (dla sąsiedztwa ośmiospójnego i czterospójnego)
	Otwarcia i Domknięcia
Jeden wybrany filtr (proszę o rozsądne korzystanie, zamiana wszystkich pikseli na czarne lub białe będzie przesadą),
Wyrównanie histogramu,
Kompresja,
Wygładzanie przez uśrednianie;

Wymagania ogólne:
Klasowość, hermetyzacja i kreatywna obsługa błędów. Dodać dziedziczenie.
Kod czysty, czytelny, pisany w języku polskim (przynajmniej metody i funkcje, zmienne wybaczę).
Optymalizacja kodu - nie powtarzać zbędnie kodu, lepiej zrobić funkcję itd.
"""

import PIL

class EdytorObrazow:
    def __init__(self, sciezka):
        try:
            self.zdjecie=PIL.Image.open(sciezka)
        except IOError: #IOError wynik nieprawidłowej nazwy pliku lub lokalizacji
            print("Nie można otworzyć tego pliku")
            return

    def transformacja(self):
        pass

    def negatyw(self):
        pass

    def erozja(self,sasiedztwo):
        pass

    def otwarcie(self):
        pass

    def zamkniecie(self):
        pass

    def binaryzacja(self):
        print("Wybierz co zrobić po binaryzacji: ")
        print("1. Erozja")
        print("2. Otwarcie")
        print("3. Domknięcie")

        wybor = input("Twoja opcja: ")
        if wybor == '1':
            sasiedztwo = input("Wybierz sąsiedztwo (4 lub 8): ")
            self.zdjecie = self.erozja(sasiedztwo)
        elif wybor == '2':
            self.zdjecie = self.otwarcie()
        elif wybor == '3':
            self.zdjecie = self.zamkniecie()

    def filtr(self):
        pass

    def wyrownanie_histogramu(self):
        pass

