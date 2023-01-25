from listchainnee import Liste


#Testons les différentes fonctions de  liste chainée 


#__________Avec les entiers________
l1 = Liste()
print("#\nLa liste est vide?", l1.estVide())

#On insère 15 éléments (entiers) dans la liste chaînée
print("\n _________INSERTION_ de 15 premiers eniers______________")
for i in range(15):
    l1.AjoutFin(i)
print("\nListe  actuelle :")
l1.AfficheList()

print("\nNombre d'éléments =>", l1.Taille())
print("La liste est vide?", l1.estVide())
print("ELement à l'indice 5 : ", l1.searchValeur(5))
print("Indice de la valeur 10 : ", l1.searchIndice(10))


print("\nOn ajoute la valeur 50 à l'indice 5")
l1.AjoutPos(5, 50)
print("Liste  actuelle :") 
l1.AfficheList()

print("\nOn retire le 50")
l1.supFirstValue(50)
print("Liste  actuelle :"),
l1.AfficheList()

print("\nOn ajoute  16 et  17 aux positions 9 et 10")
l1.AjoutPos(9, 16)
l1.AjoutPos(10, 17)
print("Liste  actuelle :")
l1.AfficheList()


print("\nOn retire le 9, le 16 et le 17")
l1.supFirstValue(9)
l1.supFirstValue(16)
l1.supFirstValue(17)

print("Liste  actuelle :")
l1.AfficheList()

print("\nOn retire le 0")
l1.SupAllElement(0)
print("Liste  actuelle :")
l1.AfficheList()

print("\nOn retire tous les éléments allant de 1 à 5 inclus.")
for i in range(1, 6):
    l1.SupAllElement(i)
print("Liste  actuelle :")
l1.AfficheList()

print("\nOn retire le premier élément")
l1.SupTete()
print("Liste  actuelle :")
l1.AfficheList()
 
print("\nOn insère 10 fois la valeur 1 dans la liste")
i = 0
while i < 10:
    l1.AjoutFin(1)
    i += 1
print("Liste  actuelle :")
l1.AfficheList()

print("\nOn recherche tout les indices de la valeur 1\n")
print("tout les indices de la valeur 1 sont: ", l1.searchAllIndice(1))

print("\nOn compte le nombre d'occurence de la valeur ayant la valeur 1\n")
print("Le nombre d'ocurence ayant la valeur 1 est:", l1.countValue(1))

print("\nOn efface tous les occurence de 1:")
l1.SupAllElement(1)
l1.AfficheList()

print("\nOn supprime l'élement en tête de la liste")
l1.SupTete()
l1.AfficheList()

print("\nOn supprime l'élement en fin de la liste ")
l1.SupFin()
l1.AfficheList()

print("\nOn supprime l'élement à la position 5 de la liste ")
l1.SupPos(3)
l1.AfficheList()

print("\n___ON VIDE LA LISTE")
l1.effaceListe()



