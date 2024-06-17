import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""numero_01 = int(input("Insira o primeiro número: "))
numero_02 = int(input("Insira o segundo número: "))
resultado = numero_01 + numero_02
print(resultado)
"""
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""numero_01 = int(input("Insira um número: "))
resto_divisao = numero_01 % 5
print(resto_divisao)"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

"""numero_01 = int(input("Insira o primeiro número: "))
numero_02 = int(input("Insira o segundo número: "))
multiplicacao = numero_01 * numero_02
print(multiplicacao)
"""
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

"""numero_01 = int(input("Insira um número: "))
quadrado_do_numero = numero_01 ** 2 
print(quadrado_do_numero)"""

"""numero_01 = int(input("Insira um número: "))
quadrado_do_numero = pow(numero_01, 2)
print(quadrado_do_numero)"""

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

"""numero_01 = float(input("Insira o primeiro número: "))
numero_02 = float(input("Insira o segundo número: "))
soma = numero_01 + numero_02
print(soma)"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

"""numero_01 = float(input("Insira o primeiro número: "))
numero_02 = float(input("Insira o segundo número: "))
soma = numero_01 + numero_02
media = soma / 2

lista_numero = []
numero_01 = float(input("Insira o primeiro número: "))
lista_numero.append(numero_01)

numero_02 = float(input("Insira o primeiro número: "))
lista_numero.append(numero_02)

soma = sum(lista_numero)

media = soma / len(lista_numero)

print(f"A Média dos números é: {media}" )"""



# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

"""raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
print(f"{area_do_circulo:.2f}")
"""
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

"""texto = str(input('Escreva algo: '))
texto = texto.upper()
print(texto)"""

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

"""nome = str(input('Digite seu nome completo: '))
nome = nome.lower()
print(nome)"""

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

"""frase = str(input('Digite uma frase: '))
frase = frase.strip()
print(frase)"""

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

"""data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")"""

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

"""texto_1 = str(input('Digite uma palavra: '))
texto_2 = str(input('Digite outra palavra: '))
concatenado = texto_1 + texto_2
print(concatenado)"""


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.



# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.



# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

"""numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
resultado_igual = numero1 == numero2
print(resultado_igual)"""

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

"""numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
resultado_igual = numero1 != numero2
print(resultado_igual)"""

# #### try-except e if TESTE DE INTEGRAÇÃO

try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir um numero inteiro: "))
    resultado = numero_01 // numero_02
    print(resultado)
except ZeroDivisionError:
    print("integer division or modulo by zero")
except KeyboardInterrupt:
    print("Acho que voce nao quis inserir um numero")
# 21: Conversor de Temperatura

# 22: Verificador de Palíndromo

# 23: Calculadora Simples

# 24: Classificador de Números

# 25: Conversão de Tipo com Validação