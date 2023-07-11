import random

# estrazione di una parola random da un file di testo
lista = []
file = open("Lista parole.txt", "r") # Apertura in modalità lettura
righe = file.readlines() # Legge una singola riga del file
for parola in righe:
    lista.append(parola)
parola_incognita = random.choice(lista)
parola_incognita = parola_incognita[:-1] # bisogna togliere l'ultimo carattere dalla parola incognita se si sceglie dalla lista nel file


# scelgo il livello di difficoltà
livello = input("Scegli il livello: \n1:facile\n2:intermedio\n3:difficile\n ")
while livello != str(1) and livello != str(2) and livello != str(3):
    print("SCELTA NON VALIDA:RIPROVA")
    livello = input("Scegli il livello: \n1:facile\n2:intermedio\n3:difficile\n ")
if livello == str(1):
    tentativi_iniziali=10
elif livello == str(2):
    tentativi_iniziali=6
elif livello == str(3):
    tentativi_iniziali=3
print("Hai " + str(tentativi_iniziali) + " tentativi")


# stampa gli underscore in base alle lettere della parola
print("PAROLA DA INDOVINARE: " + str(list("_"*len(parola_incognita))))
tentativi = tentativi_iniziali
parola_aggiornata = list("_"*len(parola_incognita))
lettere_indovinate = []
while tentativi > 0:
    lettera = input("Inserisci lettera: ")
    if lettera in parola_incognita:
        print("La lettera è presente!")
        lettere_indovinate.append(lettera)
        for indice in range(len(parola_incognita)):
            if parola_incognita[indice] not in lettere_indovinate:
                parola_aggiornata[indice] = "_"
            else:
                parola_aggiornata[indice] = parola_incognita[indice]
        print(f"PAROLA DA INDOVINARE: {parola_aggiornata}")
        if parola_aggiornata == list(parola_incognita):
            break
    else:
        tentativi -= 1
        print(f"Lettera non presente! Ti rimangono {tentativi} tentativi")

if tentativi == 0:
    print(f"Sei morto impiccato! La parola era: {parola_incognita}")
else:
    print("Hai vinto!")