#Crie uma matriz de tamanho 3x3 e
#preencha-a com valores de 1 a 9.
#Imprima a matriz das três formas:
#1. print(matriz)
#2. utilizando um for.
#3. utilizando dois for’s.


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print (matriz)

for linha in matriz:
    print (linha)
#ou
for linha in range(3):
    print (matriz[linha])
#ou
for linha in range (3):
    for coluna in range (3):
        print (matriz[linha][coluna])

#Utilizando a mesma matriz da
#prática anterior, altere os valores
#nas seguintes posições:
#1. [0][0] para 20
#2. [1][2] para 15
#3. [2][1] para 19

matriz [0][0] = 20
matriz [1][2] = 15
matriz [2][1] = 19

for linha in range(3):
    print (matriz[linha])

#Faça as seguintes operações aritméticas com os valores de cada
#posição e armazene-as em variáveis:
#1. soma de [0][0] e [1][0]
#2. subtração de [2][2] e [2][1]
#3. multiplicação de [0][1] e [2][0]
#4. divisão de [1][2] e [0][2]
#Imprima todas as variáveis.

soma = matriz[0][0] + matriz [1][0]
sub = matriz [2][2] - matriz [2][1]
mult = matriz [0][1] * matriz [2][0]
div = matriz [1][2] / matriz [0][2]

print (soma, sub, mult, div)
