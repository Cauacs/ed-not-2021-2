# coding: latin-1

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
