#Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.

"""
Část 1
V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). 
Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektu. 
Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. 
S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, 
kde ICO nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). 
S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd. Text, který API vrátí, 
převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). Získané informace vypiš na obrazovku.

Například pro IČO 22834958 by tvůj program měl vypsat následující text.

Czechitas z.ú.
Krakovská 583/9, Nové Město, 110 00 Praha 1
"""

import json
import requests

ico = input("Zadejte IČO subjektu, o kterém chcete získat informace (IČO zadávejte bez mezer): ")

while len(ico) != 8:            #program odchytí, pokud uživatel nezadá osmimístný řetězec
    print("Vlož osmimístné číslo IČO")
    ico = input("Zadejte IČO subjektu, o kterém chcete získat informace (IČO zadávejte bez mezer): ")

url_input = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
#url_ico = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"  elegantnější řešení, jak vložit IČO do odkazu
#url_input = url_ico[:-3] + ico

response = requests.get(url_input)
data = response.json()

with open("actual_ICO.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])
