import locale

locale.setlocale(locale.LC_ALL, "de_DE")


def checkout_process():
    price = input("Gib den Preis ein: ")
    price = locale.atof(price)
    discount_in_percent = input("Rabatt in %: ")
    discount_in_percent = float(discount_in_percent)
    discount_in_euro = price / 100 * discount_in_percent
    new_price = round(price - discount_in_euro, 2)
    print("Preis mit", discount_in_percent, "% Rabatt ist", new_price)

    payment = input("Der Kunde zahlt: ")
    payment = locale.atof(payment)
    change = payment - new_price
    if change < 0:
        print("Das gezahlte Geld reicht nicht!")
    else:
        print("Gegeben:", payment, "Preis:", new_price)
        print("Wechselgeld:", locale.format_string("%.2f", change))
        return new_price


sales = 0

while True:
    sales += checkout_process()
    entry = input("Noch einmal (j/n)? ")
    if entry == "n":
        break

print("Der Umsatz beträgt:", round(sales, 2))
print("Das Programm wurde beendet.")
