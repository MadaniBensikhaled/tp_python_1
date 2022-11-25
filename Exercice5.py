#Exercice 5:
import random
import time

from Exercice4 import *

#---- /!\ Gnuplot utilsé avec l'application, donc pas d'import sur le fichier Python

#----1
tableau1 = [1,2,3]

def copie(t):
    nouveauT = list(t)
    return nouveauT

#tableau2 = copie(tableau1)
#tableau2.append(4)
#print(tableau1)
#print(tableau2)

#----2
def inverse(t):
    nouveauT = list(t)
    nouveauT.reverse()
    return nouveauT

#tableau2 = inverse(tableau1)
#tableau2.append(4)
#print(tableau1)
#print(tableau2)

#----3
def tableau_premiers_entiers(n):
    t = []
    for i in range(1,n+1):
        t.append(i)
    return t

#tableauEntiers1 = tableau_premiers_entiers(12)
#print(tableauEntiers1)

def tableau_premiers_entiers_melanges(n):
    t = []
    for i in range(1,n+1):
        t.append(i)
    random.shuffle(t)
    return t

#tableauEntiersAleatoires1 = tableau_premiers_entiers_melanges(12)
#print(tableauEntiersAleatoires1)

def tableau_premiers_entiers_inverses(n):
    t = []
    for i in range(1,n+1):
        t.append(i)
    t.reverse()
    return t

#tableauEntiersInverses1 = tableau_premiers_entiers_inverses(12)
#print(tableauEntiersInverses1)

#----4

def ligne_dans_fichier(f,n,t):
    file = open(f, "a")
    file.write("%d " %n)
    for i in t:
        file.write("%d" %i)
    file.write("\n")
    file.close()

#ligne_dans_fichier("f.txt",3,tableau1)

#----5

def temps_tri_bulles(t):
    startTime = time.time()
    nouveauT = list(t)
    triABulle(nouveauT)
    endTime = time.time()
    timeValue = endTime-startTime
    return timeValue

#tableau3 = tableau_premiers_entiers_melanges(5000000)
#tempsCopieTableau1 = temps_tri_bulles(tableau3)
#print(tempsCopieTableau1)

#----6

def stats_melange(nmin,nmax,pas,fois):
    file = open("stats_melange_triABulle.txt", "w")
    i = nmin
    while i <= nmax:
        tempsTotal = 0
        for j in range(fois):
            tempsTotal += temps_tri_bulles(tableau_premiers_entiers_melanges(i))
        tempsTotal = tempsTotal/fois
        file.write("%d " %i)
        file.write("%f\n" %tempsTotal)
        i += pas
    file.close()

#stats_melange(100,1000,100,5)

#----7

def stats_ordonne(nmin,nmax,pas,fois):
    file = open("stats_ordonne_triABulle.txt", "w")
    i = nmin
    while i <= nmax:
        tempsTotal = 0
        for j in range(fois):
            tempsTotal += temps_tri_bulles(tableau_premiers_entiers(i))
        tempsTotal = tempsTotal/fois
        file.write("%d " %i)
        file.write("%f\n" %tempsTotal)
        i += pas
    file.close()

#stats_ordonne(100,1000,100,5)

#----8

def stats_inverse(nmin,nmax,pas,fois):
    file = open("stats_inverse_triABulle.txt", "w")
    i = nmin
    while i <= nmax:
        tempsTotal = 0
        for j in range(fois):
            tempsTotal += temps_tri_bulles(tableau_premiers_entiers_inverses(i))
        tempsTotal = tempsTotal/fois
        file.write("%d " %i)
        file.write("%f\n" %tempsTotal)
        i += pas
    file.close()

#stats_inverse(100,1000,100,5)

#----9

#----10

def temps_tri_insertion(t):
    startTime = time.time()
    nouveauT = list(t)
    tri_insertion(nouveauT)
    endTime = time.time()
    timeValue = endTime-startTime
    return timeValue

def temps_tri_extraction(t):
    startTime = time.time()
    nouveauT = list(t)
    tri_extraction(nouveauT)
    endTime = time.time()
    timeValue = endTime-startTime
    return timeValue

def temps_tri_rapide(t):
    startTime = time.time()
    nouveauT = list(t)
    nouveauT.sort()
    endTime = time.time()
    timeValue = endTime-startTime
    return timeValue

def stats_melange_general(nmin,nmax,pas,fois,fonction_temps_tri_type,fonction_creation_tableau,nom_fichier):
    file = open(nom_fichier, "w")
    i = nmin
    while i <= nmax:
        tempsTotal = 0
        for j in range(fois):
            tempsTotal += fonction_temps_tri_type(fonction_creation_tableau(i))
        tempsTotal = tempsTotal/fois
        file.write("%d " %i)
        file.write("%f\n" %tempsTotal)
        i += pas
    file.close()

"""
#Tableaux entiers mélangés aléatoirement
stats_melange_general(100,1000,100,5,temps_tri_bulles,tableau_premiers_entiers_melanges,"stats_melange_triABulle.txt")
stats_melange_general(100,1000,100,5,temps_tri_extraction,tableau_premiers_entiers_melanges,"stats_melange_triExtraction.txt")
stats_melange_general(100,1000,100,5,temps_tri_insertion,tableau_premiers_entiers_melanges,"stats_melange_triInsertion.txt")
stats_melange_general(100,1000,100,5,temps_tri_rapide,tableau_premiers_entiers_melanges,"stats_melange_triRapide.txt")

#Tableaux entiers avec tri rapide
stats_melange_general(100,1000,100,5,temps_tri_rapide,tableau_premiers_entiers_melanges,"stats_melange_triRapide.txt")
stats_melange_general(100,1000,100,5,temps_tri_rapide,tableau_premiers_entiers,"stats_ordonne_triRapide.txt")
stats_melange_general(100,1000,100,5,temps_tri_rapide,tableau_premiers_entiers_inverses,"stats_inverse_triRapide.txt")
"""