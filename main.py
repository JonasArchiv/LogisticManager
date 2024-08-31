import json
import os


class Inventory:
    def __init__(self, dateiname='inventar.json'):
        self.dateiname = dateiname
        self.lade_inventar()

    def lade_inventar(self):
        if os.path.exists(self.dateiname):
            with open(self.dateiname, 'r') as datei:
                self.inventar = json.load(datei)
        else:
            self.inventar = {
                "kategorien": {},
                "lagerorte": {},
                "lieferanten": {},
                "kunden": {}
            }

    def speichere_inventar(self):
        with open(self.dateiname, 'w') as datei:
            json.dump(self.inventar, datei, indent=4, ensure_ascii=False)

    def fuege_kategorie_hinzu(self, kategorie):
        if kategorie not in self.inventar["kategorien"]:
            self.inventar["kategorien"][kategorie] = {}
            print(f"Kategorie '{kategorie}' hinzugefügt.")
        else:
            print(f"Kategorie '{kategorie}' gibt's schon.")

    def fuege_lagerort_hinzu(self, lagerort):
        if lagerort not in self.inventar["lagerorte"]:
            self.inventar["lagerorte"][lagerort] = {}
            print(f"Lagerort '{lagerort}' hinzugefügt.")
        else:
            print(f"Lagerort '{lagerort}' gibt's schon.")

    def fuege_lieferant_hinzu(self, lieferant):
        if lieferant not in self.inventar["lieferanten"]:
            self.inventar["lieferanten"][lieferant] = []
            print(f"Lieferant '{lieferant}' hinzugefügt.")
        else:
            print(f"Lieferant '{lieferant}' gibt's schon.")

    def fuege_kunde_hinzu(self, kunde):
        if kunde not in self.inventar["kunden"]:
            self.inventar["kunden"][kunde] = []
            print(f"Kunde '{kunde}' hinzugefügt.")
        else:
            print(f"Kunde '{kunde}' gibt's schon.")

    def fuege_artikel_hinzu(self, kategorie, lagerort, name, menge, lieferant):
        if kategorie not in self.inventar["kategorien"]:
            print(f"Kategorie '{kategorie}' gibt's nicht.")
            return
        if lagerort not in self.inventar["lagerorte"]:
            print(f"Lagerort '{lagerort}' gibt's nicht.")
            return
        if lieferant not in self.inventar["lieferanten"]:
            print(f"Lieferant '{lieferant}' gibt's nicht.")
            return

        if lagerort not in self.inventar["kategorien"][kategorie]:
            self.inventar["kategorien"][kategorie][lagerort] = {}

        if name in self.inventar["kategorien"][kategorie][lagerort]:
            self.inventar["kategorien"][kategorie][lagerort][name] += menge
        else:
            self.inventar["kategorien"][kategorie][lagerort][name] = menge

        self.inventar["lieferanten"][lieferant].append(name)
        print(f"{menge} {name}(s) hinzugefügt in {kategorie} bei {lagerort} von {lieferant}.")
        self.speichere_inventar()

    def entferne_artikel(self, kategorie, lagerort, name, menge):
        if kategorie not in self.inventar["kategorien"]:
            print(f"Kategorie '{kategorie}' gibt's nicht.")
            return
        if lagerort not in self.inventar["kategorien"][kategorie]:
            print(f"Lagerort '{lagerort}' gibt's nicht.")
            return

        if name in self.inventar["kategorien"][kategorie][lagerort]:
            if self.inventar["kategorien"][kategorie][lagerort][name] >= menge:
                self.inventar["kategorien"][kategorie][lagerort][name] -= menge
                if self.inventar["kategorien"][kategorie][lagerort][name] == 0:
                    del self.inventar["kategorien"][kategorie][lagerort][name]
                    if not self.inventar["kategorien"][kategorie][lagerort]:
                        del self.inventar["kategorien"][kategorie][lagerort]
                print(f"{menge} {name}(s) entfernt aus {kategorie} bei {lagerort}.")
            else:
                print(f"Nicht genug {name} in {kategorie} bei {lagerort}.")
        else:
            print(f"{name} nicht gefunden in {kategorie} bei {lagerort}.")
        self.speichere_inventar()

    def wareneingang(self, kategorie, lagerort, name, menge, lieferant):
        self.fuege_artikel_hinzu(kategorie, lagerort, name, menge, lieferant)

    def warenausgang(self, kategorie, lagerort, name, menge, kunde):
        if kategorie not in self.inventar["kategorien"]:
            print(f"Kategorie '{kategorie}' gibt's nicht.")
            return
        if lagerort not in self.inventar["kategorien"][kategorie]:
            print(f"Lagerort '{lagerort}' gibt's nicht.")
            return
        if kunde not in self.inventar["kunden"]:
            print(f"Kunde '{kunde}' gibt's nicht.")
            return

        if name in self.inventar["kategorien"][kategorie][lagerort]:
            if self.inventar["kategorien"][kategorie][lagerort][name] >= menge:
                self.inventar["kategorien"][kategorie][lagerort][name] -= menge
                if self.inventar["kategorien"][kategorie][lagerort][name] == 0:
                    del self.inventar["kategorien"][kategorie][lagerort][name]
                    if not self.inventar["kategorien"][kategorie][lagerort]:
                        del self.inventar["kategorien"][kategorie][lagerort]
                self.inventar["kunden"][kunde].append(name)
                print(f"{menge} {name}(s) an {kunde} ausgegeben aus {kategorie} bei {lagerort}.")
            else:
                print(f"Nicht genug {name} in {kategorie} bei {lagerort}.")
        else:
            print(f"{name} nicht gefunden in {kategorie} bei {lagerort}.")
        self.speichere_inventar()

