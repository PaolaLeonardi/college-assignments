#O código cria uma lista de números, altera alguns valores, exibe os elementos na tela e realiza operações matemáticas como soma, multiplicação e divisão. 
#Depois, cria outra lista e utiliza estruturas de repetição (while e for) para multiplicar cada número dessa lista por 2 e mostrar os resultados.

n = [5,7,12,2,9,21]
n [1] = 17 #Indíce 1
n [3] = 22 #Indíce 3
n [2] = 1 #Indíce 2
n [4] = 29 #Indíce 4
print (n [0])
print (n [1])
print (n [2])
print (n [3])
print (n [4])
print (n [5])

soma = n[5] + n[4]
sub = n[3] + n[1]
multi = n[0] * n[5]
div = n[3] / n[2]

print ("As operações ficaram:")
print (soma, sub, multi, div)

#Agora multiplicamos estes por 2:
numero=[10,7,2,15]
i = 0

while i < 4:
    print(numero[i]*2)
    i+= 1

for i in range(len(numero)):
    print(numero[i] * 2

#Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:
#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
#(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
#A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
#(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
#d) Mostre na tela cada valor do vetor A, um em cada linha.

A = ([1, 0, 5, -2, -5, 7])
soma = A[0]+A[1]+A[2]
print (soma)
A [4] = 100
print (A)

#Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

Valor1 = (int(input("Diga um valor inteiro")))
Valor2 = (int(input("Diga outro valor inteiro")))
Valor3 = (int(input("Diga mais um valor inteiro")))
Valor4 = (int(input("Diga mais outro valor inteiro")))
Valor5 = (int(input("Diga o penúltimo valor inteiro")))
Valor6 = (int(input("Diga o último valor inteiro")))

Valores = [Valor1, Valor2, Valor3, Valor4, Valor5, Valor6]
print (Valores)
