import time

#funksjonen som får teksten til å gå samtidig som du leser
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

slow_print("Velkommen til min kalkulator")
slow_print("Skriv inn det første tallet")
A = float(input(""))

slow_print("skriv inn det andre tallet")
B = float(input(""))


while True:
    slow_print("Velg mellom:")
    slow_print("1: + (plusse)")
    slow_print("2: / (Dele)")
    slow_print("3: * (Gange)")
    slow_print("4: - (Minus)")

    C = input("")

    if C in ('1', '+', '2', '/', '3', '*', '4', '-'):
        break  
    else:
        print("Ugyldig inndata, vennligst prøv på nytt")

if C == '1' or C == '+':
    result = A + B
    slow_print(f"Svaret er {result}")
    
if C == '2' or C == '/':
    result = A / B
    slow_print(f"Svaret er {round(result, 3)}")

if C == '3' or C == '*':
    result = A * B
    slow_print(f"Svaret er {result}")

if C == '4' or C == '-':
    result = A - B
    slow_print(f"Svaret er {round(result, 3)}")