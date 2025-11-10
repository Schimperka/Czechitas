"""Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. 
Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, bytové a komerční prostory. 
Výše daně se odvíjí od několika faktorů, např. typu nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd."""
import math
from abc import ABC, abstractmethod

#V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. 
# Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

#Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. 
# Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).

#bonus - Uprav třídu Property na abstraktní třídu. Tato třída totiž nereprezentuje žádnou konkrétní nemovitost, nemovitost totiž musí být pozemek nebo stavba.

class Property(ABC):
    def __init__(self, locality: Locality):
        self.locality = locality
    @abstractmethod
    def calculate_tax(self):
        pass

#Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
# Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). 
# Dále přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math).
# Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. 
# U atributu estate_type následující hodnoty a koeficienty:

"""
- land (zemědělský pozemek) má koeficient 0.85.
- building site (stavební pozemek) má koeficient 9.
- forrest (les) má koeficient 0.35,
- garden (zahrada) má koeficient 2. 
"""

class Estate(Property):
    def __init__(self, locality: Locality, estate_type, area):
        self.estate_type = estate_type
        self.area = area
        super().__init__(locality)
    def calculate_tax(self):
        if self.estate_type == "land":
            coeff = 0.85
        elif self.estate_type == "building site":
            coeff = 9
        elif self.estate_type == "forrest":
            coeff = 0.35
        elif self.estate_type == "garden":
            coeff = 2

        property_tax = self.area * coeff * self.locality.locality_coefficient
        return math.ceil(property_tax)
    
#Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. 
# Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, 
# zda se jedná o nemovitost používanou k podnikání). Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. 
# Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. 
# Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        property_tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            property_tax = property_tax * 2
        return math.ceil(property_tax)

#Vyzkoušej svůj program pomocí následujících nemovitostí:

"""
- Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
- Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
- Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. 
Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
"""

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

objekt_1 = Estate(manetin, "land", 900)
objekt_2 = Residence(manetin, 120, False)
objekt_3 = Residence(brno, 90, True)

print(objekt_1.calculate_tax())
print(objekt_2.calculate_tax())
print(objekt_3.calculate_tax())
