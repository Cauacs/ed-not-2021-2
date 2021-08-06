# coding: latin-1
from math import pi

#Função é um trecho de código que tem um nome e pode receber informações externas para fazer seu trabalho.
#Opcionalmente, uma função pode retornar um valor
#Uma função pode ser chamada várias vezes mas é definida apenas uma
#Python ja vem com algumas funções imbutidas

def imc(peso, altura):
    """
        Função que calcula o Índice de Massa Corpórea (IMC)
    """
    #Trechos com aspas triplas são comentários especiais no python para documentar uma função.
    return peso / (altura ** 2)


p = float(input("Informe seu peso: "))
a = float(input("Informe a altura: "))

print(imc(p,a))


def area_forma(base, altura, forma = "R"):
    """
        Função que calcula a área de uma das seguintes formas geométricas:
        retangulo, triangulo ou elipse
        Parametro forma:
        "R" == retangulo
        "T" == triangulo
        "E" == elipse
    """

    area = 0
    
    if forma == "R":
        area = base * altura
    elif forma == "T":
        area = base * altura / 2
    elif forma == "E":
        area = (base/2) * (altura * 2) * pi

    return area


print(f"Retangulo 7.5x11: {area_forma(7.5, 11)}")
