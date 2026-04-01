print ("Exercício 03") 

numero = int(input("Estudante, digite um número de 0 a 10"))

while numero > 10 or numero < 0: # Ou posso usar 0 < numero < 10 se preferir (no pyton)
    print ("Inválido, digite uma número de 0 a 10")
    numero = int(input("Digite um número de 0 a 10: ")) # Repete

print (f"sua nota é {numero}") 
