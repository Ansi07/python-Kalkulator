import time

# Funksjonen som får teksten til å gå samtidig som du leser
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

# Velkomstmelding
slow_print("Velkommen til min kalkulator")

# Leser det første tallet
slow_print("Skriv inn det første tallet")
A = float(input(""))

# Meny for operasjoner
while True:
    slow_print("Velg mellom:")
    slow_print("1: + (plusse)")
    slow_print("2: / (Dele)")
    slow_print("3: * (Gange)")
    slow_print("4: - (Minus)")

    # Leser operatøren
    C = input("")

    # Sjekker om operatøren er gyldig
    if C in ('1', '+', '2', '/', '3', '*', '4', '-'):
        break  
    else:
        print("Ugyldig inndata, vennligst prøv på nytt")

# Leser det andre tallet
slow_print("skriv inn det andre tallet")
B = float(input(""))

# Utfører den valgte operasjonen
if C == '1' or C == '+':
    result = A + B
    slow_print(f"Svaret er {round(result, 3)}")
    
if C == '2' or C == '/':
    result = A / B
    slow_print(f"Svaret er {round(result, 3)}")

if C == '3' or C == '*':
    result = A * B
    slow_print(f"Svaret er {round(result, 3)}")

if C == '4' or C == '-':
    result = A - B
    slow_print(f"Svaret er {round(result, 3)}")
