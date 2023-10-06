palavra = "alexandre"
soma = 0
for letra in palavra:
    if letra not in "aeiouAEIOU":
        soma = soma + 1
print(soma)
