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

