#Exercice 4:

#----1
tableau1 = [18,6,9,74,2,6]
tableau2 = [85,96,0,6,7]
tableau3 = [0,69,-5,0,65,41,3,-24,7,3]

def index_minimum(t, d, f):
    min = d
    for i in range(d,f+1):
        if t[i] < t[min]:
            min = i
    return min

#print(index_minimum(tableau1, 0, 5)) == 4
#print(index_minimum(tableau1, 1, 3)) == 1
#print(index_minimum(tableau2, 1, 4)) == 2
#print(index_minimum(tableau3, 0, 4)) == 2
#print(index_minimum(tableau3, 0, 9)) == 7

def triABulle(t): 
    taille = len(t)
    for i in range(taille-1): 
        for j in range(0, taille-i-1): 
             if t[j] > t[j+1] : 
                t[j], t[j+1] = t[j+1], t[j] 
  
#print ("tableau3 non trié : ", tableau3)  
#triABulle(tableau3) 
#print ("tableau3 trié : ", tableau3)

#----2

tableauCroissant1 = [4,7,27,29,35,56,99,145,605,902]

def recherche(t, e):
    i = 0
    while t[i] < e:
        i += 1
    if t[i] == e:
        return "Element présent à la case "+str(i)+"du tableau."
    else:
        return "Element non présent dans le tableau."

#print(recherche(tableauCroissant1,0))
#print(recherche(tableauCroissant1,145))

def rechercheDichotomique(t, e):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == e:
            return "Element présent à la case "+str(m)+"du tableau."
        elif t[m] < e:
            a = m + 1
        else:
            b = m - 1
    return "Element non présent dans le tableau."

#print(rechercheDichotomique(tableauCroissant1,0))
#print(rechercheDichotomique(tableauCroissant1,145))

def insertion(e, t, n):
    n = len(t)
    position = n
    for i in range(n):
        if t[i] > e:
            position = i
            break
    if position == n:
        t = t[:position] + [e]
    else:
        t = t[:position] + [e] + t[position:]
    return t

#tableauCroissant1 = insertion(0, tableauCroissant1, 0)
#tableauCroissant1 = insertion(67, tableauCroissant1, 0)
#tableauCroissant1 = insertion(902, tableauCroissant1, 0)
#tableauCroissant1 = insertion(1003, tableauCroissant1, 0)
#print(tableauCroissant1)

#insertion2() permet de s'arrêter à l'index n
def insertion2(e, t, n):
    position = n
    for i in range(n):
        if t[i] > e:
            position = i
            break
    t = t[:position] + [e] + t[position:]
    return t

#----3

def tri_extraction(t):
    n = len(t)
    for i in range(n):
        min = index_minimum(t,i,n-1)
        save = t[i]
        t[i] = t[min]
        t[min] = save

#print(tableau1)
#tri_extraction(tableau1)
#print(tableau1)
#print(tableau2)
#tri_extraction(tableau2)
#print(tableau2)
#print(tableau3)
#tri_extraction(tableau3)
#print(tableau3)

def tri_insertion(t):
    n = len(t)
    for i in range(1,n):
        save = t[i]
        del t[i]
        #On utilise insertion2()
        t = insertion2(save,t,i-1)
    return t

#print(tableau1)
#tableau1 = tri_insertion(tableau1)
#print(tableau1)
#print(tableau2)
#tableau2 = tri_insertion(tableau2)
#print(tableau2)
#print(tableau3)
#tableau3 = tri_insertion(tableau3)
#print(tableau3)