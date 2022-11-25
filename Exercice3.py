#Exercice 3 :

class Promotion:
    #Classe des promotions

    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []
    
    def ajouterEtudiant(self, etudiant):
        self.etudiants.append(etudiant)
    
    def etudiantNoteMoyenneMaximal(self):
        moy = 0
        cpt = 0
        noteMoyenneMax = 0
        etudiantMax = []
        #Boucle
        for etudiant in self.etudiants:
            moy = etudiant.moyenneNotes()
            if noteMoyenneMax == moy:
                etudiantMax.append(etudiant)
            if noteMoyenneMax < moy:
                noteMoyenneMax = moy
                etudiantMax.clear()
                etudiantMax.append(etudiant)
        return etudiantMax


class Etudiant:
    #Classe des étudiants

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.notes = []

    def ajouterNote(self, discipline, valeurNote):
        self.notes.append([discipline,valeurNote])
    
    def changeNom(self, nom):
        self.nom = nom
    
    def changeNom(self, prenom):
        self.prenom = prenom
    
    def moyenneNotes(self):
        moy = 0
        for note in self.notes:
            moy = moy + note[1]
        moy = moy/len(self.notes)
        return moy


class Discipline:
    #Classe des disciplines

    def __init__(self, nom):
        self.nom = nom
    
    def moyennePromotion(self, promotion):
        moy = 0
        cpt = 0
        for etudiant in promotion.etudiants:
            for note in etudiant.notes:
                if note[0] == self:
                    moy += note[1]
                    cpt += 1
        moy = moy/cpt
        return moy
    
    def etudiantNoteMaximal(self, promotion):
        noteMax = 0
        etudiantMax = []
        #Première boucle pour trouver la note maximale
        for etudiant in promotion.etudiants:
            for note in etudiant.notes:
                if note[0] == self:
                    if noteMax < note[1]:
                        noteMax = note[1]
        #Deuxième boucle pour trouver les étudiants
        #qui ont une note égale à la note maximale
        for etudiant in promotion.etudiants:
            for note in etudiant.notes:
                if note[0] == self:
                    if noteMax == note[1]:
                        etudiantMax.append(etudiant)
        return etudiantMax


#On crée les étudiants
etu1 = Etudiant("NomEtu1","PrenomEtu1")
etu2 = Etudiant("NomEtu2","PrenomEtu2")
etu3 = Etudiant("NomEtu3","PrenomEtu3")

#On crée la promotion
promo1 = Promotion("Promotion 1")

#On crée les disciplines
maths = Discipline("Mathématiques")
prog = Discipline("Programmation")

#On ajoute les étudiants à la promotion
promo1.ajouterEtudiant(etu1)
promo1.ajouterEtudiant(etu2)
promo1.ajouterEtudiant(etu3)

#On ajoute des notes aux étudiants
etu1.ajouterNote(maths, 18)
etu1.ajouterNote(prog, 12)
etu2.ajouterNote(maths, 9)
etu2.ajouterNote(prog, 19)
etu3.ajouterNote(maths, 3)
etu3.ajouterNote(prog, 20)

#----1
print("Voici les étudiants (adresse des objets) de la promotion :", promo1.etudiants)

#----2
#Moyenne des note des étudiants
print("Moyenne de etu1 : ", etu1.moyenneNotes())
print("Moyenne de etu2 : ", etu2.moyenneNotes())
print("Moyenne de etu3 : ", etu3.moyenneNotes())

#----3
print("Moyenne pour les mathématiques : Promotion 1 : ", maths.moyennePromotion(promo1))
print("Moyenne pour la programmation : Promotion 1 : ", prog.moyennePromotion(promo1))

#----4
#Etudiants qui ont eu la note moyenne maximale de la promotion
print("Etudiants de la promo avec la note moyenne maximale : ", promo1.etudiantNoteMoyenneMaximal())
#Etudiants qui ont eu la note moyenne maximale de la disicpline pour la promotion
print("Etudiants de la promo avec la note moyenne maximale en mathématiques: ", maths.etudiantNoteMaximal(promo1))
print("Etudiants de la promo avec la note moyenne maximale en programmation: ", prog.etudiantNoteMaximal(promo1))

#----5
#Peut déjà être utilisé pour un nombre quelconque de notes
#En revanche, les notes doivent appartenir à une discipline existant quelconque