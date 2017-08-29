"""
Valter Gonçalves dos Santos RA 1110951
Marcos Vinícius Zamboni RA 1700108

Exercício 3:
Crie um programa que leia um valor e a partir disso faça:
(1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
(2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
(3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.
"""

digitado = int(input("Digite um numero: "))

if digitado < 0:
    print("O modulo de %i eh %i" % (digitado, abs(digitado)))
elif digitado > 10:
    digitado2 = int(input("Digite um segundo numero: "))
    print("A diferença entre %i e %i eh %i" % (digitado, digitado2, (digitado - digitado2)))
else:
    print("O valor %i dividido por 5.0 eh %f" % (digitado, (digitado / 5.0)))
