# O código cria uma lista de números, altera alguns valores, exibe os elementos na tela e realiza operações matemáticas como soma, multiplicação e divisão. 
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

numero=[10,7,2,15]
i = 0

while i < 4:
    print(numero[i]*2)
    i+= 1

for i in range(len(numero)):
    print(numero[i] * 2

#1 Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:
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

#2 Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

Valor1 = (int(input("Diga um valor inteiro")))
Valor2 = (int(input("Diga outro valor inteiro")))
Valor3 = (int(input("Diga mais um valor inteiro")))
Valor4 = (int(input("Diga mais outro valor inteiro")))
Valor5 = (int(input("Diga o penúltimo valor inteiro")))
Valor6 = (int(input("Diga o último valor inteiro")))

Valores = [Valor1, Valor2, Valor3, Valor4, Valor5, Valor6]
print (Valores)

# //////////////

#3 Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
#componentes deste vetor, armazenando o resultado em outro vetor.
# Os conjuntos tem 10 elementos cada. Imprimir os conjuntos.

numeros = []
quadrados = []

for i in range(10):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

for numero in numeros:
    quadrados.append(numero ** 2)

print("\nVetor original:")
print(numeros)

print("\nVetor com os quadrados:")
print(quadrados)

#4 Faça um programa que leia um vetor de 8 posicoes e,
#em seguida, leia tambem dois valores X e Y quaisquer correspondentes a duas posicoes no vetor.
# Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posicoes X e Y.

vetor = []

for i in range(8):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

x = int(input("Digite a posição X: "))
y = int(input("Digite a posição Y: "))

soma = vetor[x] + vetor[y]

print("A soma dos valores é:", soma)

#5 Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.

vetor = []
pares = 0

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

    if valor % 2 == 0:
        pares += 1

print("Quantidade de valores pares:", pares)

#6 Faça um programa que receba do usuario um vetor com 10 posicoes. Em seguida devera
#ser impresso o maior e o menor elemento do vetor.

vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)

print("Maior valor:", maior)
print("Menor valor:", menor)

#7 Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor.
# Imprima o vetor, o maior elemento e a posicao que ele se encontra.

vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)

maior = max(vetor)

posicao = vetor.index(maior)

print("\nVetor:")
print(vetor)

print("\nMaior elemento:", maior)
print("Posição:", posicao)

#8 Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor,
# calcule e imprima a media geral.

notas = []

for i in range(15):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

media = sum(notas) / 15

print("\nMédia geral da turma:", media)

#9 Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a
#quantidade de numeros negativos e a soma dos numeros positivos desse vetor.

vetor = []

negativos = 0
soma_positivos = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if numero < 0:
        negativos += 1
    if numero > 0:
        soma_positivos += numero

print("\nQuantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)

#10 Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
#juntamente com o maior, o menor e a media dos valores.

valores = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)
media = sum(valores) / 5

print("\nValores digitados:")
print(valores)

print("\nMaior valor:", maior)
print("Menor valor:", menor)
print("Média:", media)

#11 Fazer um programa para ler 5 valores e, em seguida,
#mostrar a posicao onde se encontram o maior e o menor valor.

valores = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)

pos_maior = valores.index(maior)
pos_menor = valores.index(menor)

print("\nMaior valor:", maior)
print("Posição do maior valor:", pos_maior)

print("\nMenor valor:", menor)
print("Posição do menor valor:", pos_menor)
