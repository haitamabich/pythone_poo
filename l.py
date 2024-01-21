class Produit:

    def __init__(self, reference, description, prix, qteStock):
        self.reference = reference
        self.description = description
        self.prix = prix
        self.qteStock = qteStock

    def __str__(self):
        return f"le produit:le reference {self.reference}description {self.description}"

    def montant(self):
        montant = self.qteStock * self.prix
        return f"le montant  " + str(montant)

    def afficher(self):
        print(
            f" le reference est:{self.reference}\n description:{self.description}\n le prix: {self.prix}dhs  qtestock{self.qteStock}  {self.montant()}")

    def maj(self, qte):

        if self.qteStock >= qte:
            self.qteStock -= qte
            return f"le stock est maj: {self.qteStock}"
        else:
            return "impposible"

    def provisione(self, qte):
        self.qteStock += qte
        return f"le qteprovision est {self.qteStock}"


class Magasin:

    def __init__(self, nom, adresse, ville):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.liste = []

    def ajouter(self, p):
        self.liste.append(p)
        return "produit ajouter avec succès"

    def listeProduit(self):
        for p in self.liste:
            print(p.afficher())

    def total(self):
        t = 0
        for p in self.liste:
            t += p.montant()
        return f"le montant totale est: {t} dhs"


m1=Magasin("haitam","sidi othman,rue 27 ","casablenca")
p1=Produit("bdsde","solid",23,1)
p2=Produit("macbock","pc",233,12)
m1.ajouter(p1)
m1.ajouter(p2)
print(m1.listeProduit())


m2=Magasin("wissam","sidimoumen rue 13","casablenca")
p3=Produit("phone","sony",434,16)
p4=Produit("smartwach","apple",643,20)

m2.ajouter(p3)
m2.ajouter(p4)
print(m2.ajouter())


