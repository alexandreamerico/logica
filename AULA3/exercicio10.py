palavra = str(input("Digite uma palavra: "))

invertida = palavra [::-1]

if palavra == invertida:
    print("é um palíndromo")
else:
    print("não é um palíndromo")