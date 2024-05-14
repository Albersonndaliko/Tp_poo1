class etudiant:
    def __init__(self,nom,cote1,cote2):
        self.nom = nom
        self.cote1 = cote1
        self.cote2 = cote2
    
    def calcul_note_moyen(self,cote1,cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        liste_note = [cote1,cote2]
        somme = sum(liste_note)
        moyenne = somme/2
        return moyenne
    def aff_nom_et_moyenne(self,nom,moyenne):
        self.nom = nom
        self.moyenne = moyenne
        aff_nom_et_moyenne = f"L'etudiant {nom} a Eu comme Moyenne {moyenne} "
        print(aff_nom_et_moyenne)
nom = input("entre le nom de le'etudiant  ")
cote1 = float(input("entre la cote 1  "))
cote2 = float(input("entre la cote 2  "))
moyene = etudiant(nom,cote1,cote2)
moyenne_calcul = moyene.calcul_note_moyen(cote1,cote2)
affiche = etudiant(nom,cote1,cote2)
affiche.aff_nom_et_moyenne(nom,moyenne_calcul)
