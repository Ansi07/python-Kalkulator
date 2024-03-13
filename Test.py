import requests
valuta_land = {
    "USD": "Amerikanske dollar",
    "EUR": "Euro",
    "GBP": "Britiske pund",
    "JPY": "Japanske yen",
    "AUD": "Australske dollar",
    "CAD": "Kanadiske dollar",
    "CHF": "Sveitsiske franc",
    "CNY": "Kinesiske yuan",
    "INR": "Indiske rupier",
    "SGD": "Singaporske dollar",
    "NZD": "Newzealandske dollar",
    "HKD": "Hong Kong-dollar",
    "SEK": "Svenske kroner",
    "NOK": "Norske kroner",
    "KRW": "Sørkoreanske won",
    "TRY": "Tyrkiske lira",
    "ZAR": "Sørafrikanske rand",
    "BRL": "Brasilianske real",
    "RUB": "Russiske rubler",
    "MXN": "Mexicanske peso",
    "PLN": "Polske zloty",
    "THB": "Thailandske baht",
    "DKK": "Danske kroner",
    "MYR": "Malaysiske ringgit",
    "IDR": "Indonesiske rupier",
    "TWD": "Ny taiwanske dollar",
    "SAR": "Saudi Riyal",
    "AED": "Emirati Dirham",
    "ARS": "Argentinske peso",
    "CLP": "Chilenske peso",
    "COP": "Colombianske peso",
    "CZK": "Tsjekkiske koruna",
    "HUF": "Ungarske forint",
    "ILS": "Israelske nye shekel",
    "PHP": "Filippinske peso",
    "QAR": "Qatarske riyal",
    "VND": "Vietnamesiske dong",
    "PEN": "Peruvianske sol",
    "KWD": "Kuwaitiske dinar",
    "EGP": "Egyptiske pund"
}

for valutakode, land in valuta_land.items():
    print(f"{valutakode} - {land}\n")


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount


print("Velkommen til valutakalkulatoren!")
amount = float(input("Skriv inn beløpet du vil konvertere: "))
base_currency = input("Skriv inn valutakoden for den opprinnelige valutaen (f.eks. USD): ").upper()
for valutakode, land in valuta_land.items():
    print(f"{valutakode} - {land}\n")
target_currency = input("Skriv inn valutakoden for den målvalutaen (f.eks. EUR): ").upper()
converted_amount = convert_currency(amount, base_currency, target_currency)
print(f"{amount} {base_currency} tilsvarer {converted_amount} {target_currency}")
    
