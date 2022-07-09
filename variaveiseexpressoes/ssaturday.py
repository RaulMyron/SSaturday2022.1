#nome idade e altura
nome, idade, altura = input().split()
idade = int(idade)
altura = float(altura)

nome2, idade2, altura2 = input().split()
idade2 = int(idade2)
altura2 = float(altura2)

nome3, idade3, altura3 = input().split()
idade3 = int(idade3)
altura3 = float(altura3)

print(nome, nome2, nome3)

media_idades = (idade+idade2+idade3)/3
media_alturas = (altura+altura2+altura3)/3

print('Média das idades', media_idades)
print(f'Média das alturas: {media_alturas:.2f}')