#1 Escreva um programa que crie uma lista com números aleatórios e a imprima na ela.
import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

print(lista)

#2. Escreva um programa que peça ao usuário três números e os armazene em uma lista.
# Em seguida, imprima a lista na tela.
lista = []

for i in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print(lista)

#3. Escreva um programa que peça ao usuário uma frase e converta a frase em
#uma lista com cada palavra separada. Imprima a lista na tela.
frase = input("Digite uma frase: ")

lista = frase.split()

print(lista)

#4. Escreva um programa que crie uma lista com os números de 1 a 10 e os imprima
#na tela em ordem reversa.
lista = []

for i in range(1, 11):
    lista.append(i)

lista.reverse()

#5. Escreva um programa que crie uma lista de palavras e imprima a palavra mais
#longa e a palavra mais curta da lista.
palavras = ["gato", "computador", "sol", "janela"]

maior = max(palavras, key=len)
menor = min(palavras, key=len)

print("Maior palavra:", maior)
print("Menor palavra:", menor)
print(lista)

#6. Escreva um programa que crie duas listas, 
# uma com os números pares de 1 a 10 e outra com os números ímpares de 1 a 10. 
# Em seguida, junte as duas listas em uma terceira lista e a imprima na tela.
pares = []
impares = []

for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

terceira = pares + impares

print(terceira)

#7. Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
#imprima apenas os números pares da lista.
lista = []

for i in range(1, 101):
    lista.append(i)

for numero in lista:
    if numero % 2 == 0:
        print(numero)

#8. Escreva um programa que crie uma lista com os números de 1 a 10 elevados ao quadrado. 
#Em seguida, calcule a soma dos elementos da lista e imprima o resultado.
lista = []

for i in range(1, 11):
    lista.append(i ** 2)

soma = sum(lista)

print(lista)
print("Soma:", soma)

#9. Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
#suas posições. 
#Em seguida, peça ao usuário para adivinhar a posição correta de uma determinada letra e informe se ele acertou ou errou.
import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")

random.shuffle(alfabeto)

print(alfabeto)

letra = input("Digite uma letra: ")

posicao = int(input("Digite a posição que acha que ela está: "))

if alfabeto[posicao] == letra:
    print("Acertou!")
else:
    print("Errou!")
    print("A letra estava na posição:", alfabeto.index(letra))

#10. Se você terminou os exercícios acima. Tente agora fazer o jogo da velha, mas
#utilizando listas.
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for linha in tabuleiro:
    print(linha)
