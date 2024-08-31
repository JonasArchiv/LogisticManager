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

