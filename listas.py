# coding: latin-1
# Criando uma lista

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#Percurso

for num in primos:
    print(num)

#Acrescentar um novo elemento no FIM da lista lista: append()


primos.append(31)
print(primos)


#Inserir um elemento em uma posição específica: insert()
#1 arg = posição da inserção
#2 arg = elemento a ser inserido

primos.insert(0, 1)
primos.insert(5,37)
print(primos)



#Retirar o último elemento da lista = pop()

ultimo = primos.pop()
print(f"ultimo: {ultimo}")
print(primos)

#Remover por valor = remove()

primos.remove(37)
print(primos)

#Removendo por posição = del

del primos[4]
print(primos)

#(Slicing) Fatiando uma lista
#Incluindo o primeiro arg e excluindo o ultimo

print(primos[0:7])

#Fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)
