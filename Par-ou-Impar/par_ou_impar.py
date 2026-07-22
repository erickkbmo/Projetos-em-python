def par_ou_impar(number):
    if number % 2 == 0:
        return "par"
    return "impar"


num = input("Digite um ou mais números separados por espaço: ").split()

par = 0
impar = 0
maior_num = int(num[0])
menor_num = int(num[0])

for number in num:
    number = int(number)
    saida = par_ou_impar(number)

    if saida == "par":
        par += 1
    else:
        impar += 1

    if number > maior_num:
        maior_num = number

    if number < menor_num:
        menor_num = number
    print(f"O número {number} é {saida}")


print(f"\nO número total de pares são {par}")
print(f"O númrero total de ímpares são {impar}")
print(f"O maior número é {maior_num}")
print(f"O menor número é {menor_num}")
