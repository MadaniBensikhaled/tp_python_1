#Exercice 1 :

#----1
v1 = "Variable"
print(2, "Salut", v1)
#Pour passer à la ligne, il faut faire un autre appel à la fonction print()

#----2
#Boucle while:
#i = 0
#while (i <= 100):
#    print(i)
#    i = i+1

#Boucle for:
#for i in range(101):
#    print(i)
#    i = i+1

from turtle import *

#Fonction pour créer une figure géométrique
#Paramètres : figureType = Type de figure géométrique (Carré ou Triangle)
# tailleArrete = longueur des arrêtes, couleurArrete = couleur des arrêtes,
#creuxBool = si la figure géométrique est creuse ou non, couleurInterieur = couleur de l'intérieur si la
#figure géométrique n'est pas creuse

def creerFigureGeometrique(figureType, tailleArrete, couleurArrete, creuxBool, couleurInterieur):
    color(couleurArrete, couleurInterieur)
    #Si la figure géométrique est non creuse
    if creuxBool == False:
        begin_fill()
        while True:
            forward(tailleArrete)
            if figureType == "Carré":
                left(90)
            if figureType == "Triangle":
                left(120)
            if abs(pos()) < 1:
                break
        end_fill()
        done()
    #Si la figure géométrique est creuse
    else:
        while True:
            forward(tailleArrete)
            if figureType == "Carré":
                left(90)
            if figureType == "Triangle":
                left(120)
            if abs(pos()) < 1:
                break
        done()
    
#creerFigureGeometrique("Carré", 200, "red", False, "Yellow")
#creerFigureGeometrique("Carré", 200, "red", True, "")

#creerFigureGeometrique("Triangle", 200, "red", False, "Yellow")
#creerFigureGeometrique("Triangle", 200, "red", True, "")


#----3
l = [5,9,7,2]
print(l)

print(len(l))

l[2] = 10
print(l)

del l[2]
print(l)

l.insert(2,10)
print(l)

for i in l:
    print(i)

i = 0
while i < len(l):
    print(l[i])
    i = i+1

#----4
import random
#Nombre aléatoire entre 3 et 9
print(random.randint(3, 9))
print(random.randrange(3, 9))
#Elément aléatoire dans une liste
l = ["pomme", "banane", "cerise"]
print(random.choice(l))
#Réorganise aléatoirement la liste
random.shuffle(l)
print(l)