from builtins import int, print, range, input

numero = int(input("Digite o numero que deseja fatorar "))

if numero > 0:
    FATORIAL = 1
    for item in range(1, numero +1):
        fatorial = fatorial * item
        print(item)
    print(fatorial)
else:
    print("que que se ta digitando ai burro")