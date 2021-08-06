# coding: latin-1
from math import pi

#Fun��o � um trecho de c�digo que tem um nome e pode receber informa��es externas para fazer seu trabalho.
#Opcionalmente, uma fun��o pode retornar um valor
#Uma fun��o pode ser chamada v�rias vezes mas � definida apenas uma
#Python ja vem com algumas fun��es imbutidas

def imc(peso, altura):
    """
        Fun��o que calcula o �ndice de Massa Corp�rea (IMC)
    """
    #Trechos com aspas triplas s�o coment�rios especiais no python para documentar uma fun��o.
    return peso / (altura ** 2)


p = float(input("Informe seu peso: "))
a = float(input("Informe a altura: "))

print(imc(p,a))


def area_forma(base, altura, forma = "R"):
    """
        Fun��o que calcula a �rea de uma das seguintes formas geom�tricas:
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
