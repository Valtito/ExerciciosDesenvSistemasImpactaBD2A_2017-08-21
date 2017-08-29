"""
Valter Gonçalves dos Santos RA 1110951
Marcos Vinícius Zamboni RA 1700108

Exercício 5:
Crie um programa para criar um arquivo com um conteúdo qualquer,
depois crie um segundo arquivo onde será lido o conteúdo do primeiro arquivo e copiado para o segundo.
"""

#variavel de linhas
linhas = 10

#criando arquivo
f = open('arquivo03.txt', 'w')

f.write('ACME Inc.   Uso do espaço em disco pelos usuários\n')
f.write('--------------------------------------------------\n')
f.write('Nr. Usuário     Espaço utilizado     % do uso\n')
f.write('1   alexandre          434,99 MB       16,85%\n')
f.write('2   anderson          1187,99 MB       46,02%\n')
f.write('3   antonio            117,73 MB        4,56%\n')
f.write('4   carlos              87,03 MB        3,37%\n')
f.write('5   cesar                0,94 MB        0,04%\n')
f.write('6   rosemary           752,88 MB       29,16%\n')
f.write('Espaço total ocupado:  2581,57 MB\n')
f.write('Espaço médio ocupado:   430,26 MB\n')


#fecha o arquivo
f.close()
