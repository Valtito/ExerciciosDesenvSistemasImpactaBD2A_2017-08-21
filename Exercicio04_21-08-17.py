"""
Valter Gonçalves dos Santos RA 1110951
Marcos Vinícius Zamboni RA 1700108

Exercício 4:
Crie um programa para criar um arquivo com um conteúdo qualquer,
depois crie um segundo arquivo onde será lido o conteúdo do primeiro arquivo e copiado para o segundo.
"""

#variavel de linhas
linhas = 10

#criando arquivo
f = open('arquivo01.txt', 'w')

#criando conteudo
for i in range(linhas):
	f.write('Esta e a linha %i de %i do primeiro arquivo\n' % ((i+1), linhas))

#fecha o arquivo
f.close()




#abre o(s) arquivo(s)
f = open('arquivo01.txt', 'r')
f2 = open('arquivo02.txt', 'w')
i = 0

for linha in f:
	f2.write('Esta e a linha %i de %i do segundo arquivo arquivo: %s' % ((i+1), linhas, linha))
	i = i + 1

f.close()
f2.close()
