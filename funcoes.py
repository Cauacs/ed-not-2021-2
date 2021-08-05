# coding: latin-1

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
