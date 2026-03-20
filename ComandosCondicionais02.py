print ("Exercício da floresta (slide) - 01")

caminho = input('Deseja ir para a direita ou esquerda?')

if caminho == "esquerda":
    print("Você encontrou um rio!")
else:
    print("Infelizmente você permanece perdido na floresta")
    exit ()

rio = input("Deseja atravessar o rio? S/N")

if rio == "S":
    rio = True
    print("Você atravessou o rio!")

elif rio == "N":
    rio = False
    print("Infelizmente você continua perdido na floresta")
    exit()

montanha = input ("Você encontrou uma montanha! Deseja subir? S/N")

if montanha == "S":
    montanha = True
    print("Você subiu a montanha!")
    print(" Então você encontrou um tesouro! Parabéns!")

elif montanha == "N":
    montanha = False
    print('Você continua perdido na floresta')

print ("Exercício 02")

numero = int (input ('Me diga um número'))
if numero >= 10 and numero <= 50:
    print ("O seu número está entre 10 e 50!")
elif numero < 10:
        print ("Seu número é menor que 10!")
elif numero > 50:
        print ("Seu número é maior que 50!")

print ("Exercício 03")

ano = int (input ("Diga um ano"))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Este ano é bissexto!")
else:
    print ("Este ano não é bissexto!")

print ("Exercício 04")

usuario = input("Digite o usuário:")

if usuario == "admin":
    print ("Bem vindo admin")
elif usuario == "convidado":
    print ("Acesso restrito")
else:
    print ("bloqueado")

senha = input ("Digite a senha:")
if senha == "1234":
    print ("Acesso autorizado, Bem vindo!")
else:
    print ("Acesso Bloqueado")

print ("Exercício 05")

cordenada1 = int (input ("Diga uma cordenada x"))
cordenada2 = int (input ("Diga uma cordenada y"))

if 0 < cordenada1 < 9 and 0 < cordenada2 < 9:
    print("Dentro do quadrado")
elif 0 <= cordenada1 <= 9 and 0 <= cordenada2 <= 9:
    print ("Na fronteira")
else:
    print ("Fora do quadrado")
