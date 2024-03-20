Valuta_Koder = {
    'USD': 0.095,
    'GBP': 0.075,
    'JPY': 14.07,
    'AUD': 0.14,
    'CAD': 0.13,
    'CHF': 0.084,
    'CNY': 0.68,
    'INR': 7.89,
    'SGD': 0.13,
    'NZD': 0.15,
    'HKD': 0.74,
    'SEK': 0.98,
    'NOK': 1.00,
    'KRW': 125.34,
    'TRY': 3.05,
    'ZAR': 1.78,
    'BRL': 0.47,
    'RUB': 8.72,
    'MXN': 1.60,
    'PLN': 0.37,
    'THB': 3.40,
    'DKK': 0.65,
    'MYR': 0.45,
    'IDR': 1482.08,
    'TWD': 3.00,
    'SAR': 0.36,
    'AED': 0.35,
    'ARS': 80.60,
    'CLP': 91.47,
    'COP': 371.41,
    'CZK': 2.20,
    'HUF': 34.69,
    'ILS': 0.35,
    'PHP': 5.27,
    'QAR': 0.35,
    'VND': 2346.17,
    'PEN': 0.35,
    'KWD': 0.029,
    'EGP': 4.64,
    'PKR': 26.59
}

Valuta_Navn = [
    ('USD', 'United States Dollar'),
    ('GBP', 'British Pound Sterling'),
    ('JPY', 'Japanese Yen'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CHF', 'Swiss Franc'),
    ('CNY', 'Chinese Yuan'),
    ('INR', 'Indian Rupee'),
    ('SGD', 'Singapore Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('SEK', 'Swedish Krona'),
    ('NOK', 'Norwegian Krone'),
    ('KRW', 'South Korean Won'),
    ('TRY', 'Turkish Lira'),
    ('ZAR', 'South African Rand'),
    ('BRL', 'Brazilian Real'),
    ('RUB', 'Russian Ruble'),
    ('MXN', 'Mexican Peso'),
    ('PLN', 'Polish Zloty'),
    ('THB', 'Thai Baht'),
    ('DKK', 'Danish Krone'),
    ('MYR', 'Malaysian Ringgit'),
    ('IDR', 'Indonesian Rupiah'),
    ('TWD', 'New Taiwan Dollar'),
    ('SAR', 'Saudi Riyal'),
    ('AED', 'United Arab Emirates Dirham'),
    ('ARS', 'Argentine Peso'),
    ('CLP', 'Chilean Peso'),
    ('COP', 'Colombian Peso'),
    ('CZK', 'Czech Koruna'),
    ('HUF', 'Hungarian Forint'),
    ('ILS', 'Israeli New Shekel'),
    ('PHP', 'Philippine Peso'),
    ('QAR', 'Qatari Riyal'),
    ('VND', 'Vietnamese Dong'),
    ('PEN', 'Peruvian Nuevo Sol'),
    ('KWD', 'Kuwaiti Dinar'),
    ('EGP', 'Egyptian Pound'),
    ('PKR', 'Pakistani Rupee')
]

# intro for kalkulator
print("Velkommen til min valutakalkulator:")
print("Skriv inn summen som skal bli konvertert fra nok: ")
A = float(input(""))

for valutakode, valutanavn in Valuta_Navn:
    print(f"{valutakode}: {valutanavn}")
print("Tilgjengelige valutakoder:")


print("Vennligst skriv inn valutakode som skal bli konvertert")
B = input("").upper()  # Konverterer til store bokstaver for å matche nøklene i valutakodene

# Sjekker om valutakoden finnes i listen
if B not in Valuta_Koder:
    print("Ugyldig valutakode.")
    exit()

Result = A * Valuta_Koder[B]  # Konverterer beløpet fra input A til input B

print(f"{A}NOK tilsvarer {round(Result, 3)} {B}")