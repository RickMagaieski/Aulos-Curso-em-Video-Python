print("ºº" * 25)
print("Digite três números aleatórios e eu os analisarei! ")
print("ºº" * 25)
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O menor valor foi o número {menor}.")
print(f"O maior valor foi o número {maior}.")