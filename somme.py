class somme:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def som(self,nnombre1,nombre2):
        resultat = nnombre1 + nombre2
        return resultat

nbr1util = int(input("entre le nombre 1  "))
nbr2util = int(input("entre le nombre 2  "))

somme1 = somme(nbr1util,nbr2util)

print(f"La Somme de {nbr1util} et {nbr2util} = {somme1.som(nbr1util,nbr2util)}")

