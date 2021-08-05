# coding: latin-1

frutas = ["laranja", "maca", "uva", "pera", "mamao", "abacate", "amora"]

print(frutas[2])

frutas[3] = "melao"

print(frutas)

print(len(frutas))

print("----------------------")


#Diferentes modos de iterar sobre uma lista

for fruta in frutas:
    print(fruta)

for i in range(len(frutas)):
    print(f"{frutas[i]} est� na posicao{i}")

#Ordem invertida
#1 argumento � determinado por len(frutas) -1
#2 argumento n�o conta o ultimo numero ent�o ele para em 0
#3 argumento -1 para a itera��o ser decrescente


for j in range(len(frutas) -1, -1, -1):
    print(frutas[j])
print("________________________________________")

frutas.sort()
print(frutas)
