#Exercice 2 :

#----a)
tab = [4,21,6,9,11,6,30,60]

def moyenne(tableau):
    moy = 0
    for i in tableau:
        moy += i
    moy = moy/len(tableau)
    return moy

print(moyenne(tab))

def occurence(tableau, element):
    cpt = 0
    for i in tableau:
        if i == element :
            cpt += 1
    return cpt

print(occurence(tab,6))

def supdix(tableau):
    cpt = 0
    for i in tableau:
        if i >= 10:
            cpt += 1
    return cpt

print(supdix(tab))

def valmax(tableau):
    max = tableau[0]
    for i in tableau:
        if i > max:
            max = i
    return max

print(valmax(tab))

def elementpresent(tableau, element):
    present = False
    for i in tableau:
        if i == element:
            present = True
    return present

print(elementpresent(tab,30))
print(elementpresent(tab,8))

#----b)

import random

def createRandomTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(-100,100))
    return table

print(createRandomTable(5))

def createRandomFirstTable(n):
    table = []
    for i in range(n):
        table.append(i)
    random.shuffle(table)
    return table

print(createRandomFirstTable(10))

import time

startTime = time.time()
print(moyenne(createRandomTable(10000000)))
endTime = time.time()
timeValue = endTime-startTime
print("Trouver la moyenne : Le temps pris pour l'execution est : ",timeValue,"secondes.")

startTime = time.time()
print(elementpresent(createRandomFirstTable(10000000),256))
endTime = time.time()
timeValue = endTime-startTime
print("Rechercher un élément : Le temps pris pour l'execution est : ",timeValue,"secondes.")