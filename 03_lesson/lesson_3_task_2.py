from smartphone import Smartphone

catalog = [
    Smartphone("Realme", "GT 8 Pro", "+79181846297"),
    Smartphone("Nokia", "3310", "+78005553535"),
    Smartphone("iQOO", "15 Ultra", "+79524876235"),
    Smartphone("Samsung", "Galaxy S26", "+79884258936"),
    Smartphone("Apple", "iPhone 17 Pro Max", "+79203146512")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
