"""
Obrazy możemy zapisać jako pliki graficzne, lecz edycja nadal będzie odbywać się na "oryginale" aż do zakończenia działania programu.
Przy zapisywaniu możemy wybrać nazwę pliku.
Po edycji możemy podejrzeć obraz.

Klasowość, hermetyzacja i kreatywna obsługa błędów. Dodać dziedziczenie.
Kod czysty, czytelny, pisany w języku polskim (przynajmniej metody i funkcje, zmienne wybaczę).
Optymalizacja kodu - nie powtarzać zbędnie kodu, lepiej zrobić funkcję itd.
"""

from PIL import Image, ImageOps, ImageFilter

class EdytorObrazow:
    def __init__(self, sciezka):
        try:
            self.zdjecie=Image.open(sciezka)
        except IOError: #IOError wynik nieprawidłowej nazwy pliku lub lokalizacji
            print("Nie można otworzyć tego pliku")
            return

    def transformacja(self):
        transformed_zdjecie = self.zdjecie.convert('L')  # Konwersja do skali szarości
        return transformed_zdjecie

    def negatyw(self):
        zmienione = ImageOps.invert(self.zdjecie)
        return zmienione

    def erozja(self, sasiedztwo):
        if sasiedztwo == '4':  # Czterospójne sąsiedztwo
            po_erozji = self.zdjecie.filter(ImageFilter.MinFilter(3))
        elif sasiedztwo == '8':  # Ośmiospójne sąsiedztwo
            po_erozji = self.zdjecie.filter(ImageFilter.MinFilter(9))
        else:
            print("Nieprawidłowe sąsiedztwo")
            return None
        return po_erozji

    def otwarcie(self):
        otwarte = self.zdjecie.filter(ImageFilter.MinFilter(3))
        otwarte = otwarte.filter(ImageFilter.MaxFilter(3))
        return otwarte

    def domkniecie(self):
        domkniete = self.zdjecie.filter(ImageFilter.MaxFilter(3))
        domkniete = domkniete.filter(ImageFilter.MinFilter(3))
        return domkniete

    def binaryzacja(self):
        binary = self.zdjecie.convert('1')  # Konwersja do obrazu binarnego (czarno-białego)
        return binary

    def filtr(self):
        edge = self.zdjecie.filter(ImageFilter.FIND_EDGES)
        return edge

    def wyrownanie_histogramu(self):
        histogram = ImageOps.equalize(self.zdjecie)
        return histogram

    def kompresja(self):
        skompresowane = self.zdjecie.convert('P', palette=Image.ADAPTIVE, colors=64)
        return skompresowane

    def wygladzanie(self):
        pass

    def zapisz_obraz(self,nazwa_pliku):
        self.zdjecie.save(nazwa_pliku)
        print("Obraz został zapisany jako", nazwa_pliku)
        pass

    def wyswietl(self):
        self.zdjecie.show()

def main():
    sciezka_zdjecia = input("Podaj ścieżkę do pliku obrazu: ")
    Edycja = EdytorObrazow(sciezka_zdjecia)

    while True:
        print("\nWYBIERZ CO MA ZROBIĆ KONSOLA ARTYSTKA")
        print("1. Transformacja pomiędzy przestrzeniami barw")
        print("2. Negatyw")
        print("3. Binaryzacja")
        print("4. Filtr")
        print("5. Wyrównanie histogramu")
        print("6. Kompresja")
        print("7. Wygładzanie przez uśrednianie")
        print("8. Zapisz obraz")
        print("9. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            Edycja.zdjecie = Edycja.transformacja()
        elif wybor == '2':
            Edycja.zdjecie = Edycja.negatyw()
        elif wybor == '3':
            Edycja.zdjecie = Edycja.binaryzacja()
            print("Wybierz co zrobić po binaryzacji: ")
            print("1. Erozja")
            print("2. Otwarcie")
            print("3. Domknięcie")

            wybor = input("Twoja opcja: ")
            if wybor == '1':
                sasiedztwo = input("Wybierz sąsiedztwo (4 lub 8): ")
                Edycja.zdjecie = Edycja.erozja(sasiedztwo)
            elif wybor == '2':
                Edycja.zdjecie = Edycja.otwarcie()
            elif wybor == '3':
                Edycja.zdjecie = Edycja.domkniecie()

        elif wybor == '4':
            Edycja.zdjecie = Edycja.filtr()
        elif wybor == '5':
            Edycja.zdjecie = Edycja.wyrownanie_histogramu()
        elif wybor == '6':
            Edycja.zdjecie = Edycja.kompresja()
        elif wybor == '7':
            Edycja.zdjecie = Edycja.wygladzanie()
        elif wybor == '8':
            nazwa = input("Podaj nazwę przerobionego obrazu: ")
            Edycja.zapisz_obraz(nazwa)
        elif wybor == '9':
            break
        else:
            print("Nieprawidlowy wybór. Wybierz coś z menu")
        Edycja.wyswietl()

if __name__ == "__main__":
    main()
