"""
Valter Gonçalves dos Santos RA 1110951
Marcos Vinícius Zamboni RA 1700108

Exercício 2:
Faça um programa que solicite ao usuário números e os armazene em um vetor de 20 posições.
Crie uma função que recebe o vetor preenchido e substitua todas as ocorrências de valores negativos por zero, as ocorrências de
valores menores do que 10 por 1 e as demais ocorrências por 2.
"""

def trata(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
        elif lista[i] < 10:
            lista[i] = 1
        else:
            lista[i] = 2
    return lista

listaoriginal = []
lista = []
itens = 20

for i in range(itens):
    digitado = int(input("Digite o %iº numero: " % (i + 1)))
    lista += [digitado]
    listaoriginal += [digitado]

trata(lista)

for i in range(itens):
    print("O numero %i foi alterado para %i" % (listaoriginal[i], lista[i]+0))



