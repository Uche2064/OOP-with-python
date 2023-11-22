class Etudiant:
    
    def __init__(self, nom: str, note1: float, note2: float):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2
        
    def calc_moy(self):
        return (self.note1 + self.note2) / 2
    
    def afficher(self):
        print(f"La moyenne de {self.nom} est {self.calc_moy()}")
        
if __name__ == "__main__":
    name = input("Entrez votre nom: ")
    note1 = float(input("Entrez la note 1: "))
    note2 = float(input("Entrez la note 2: "))
    
    etudiant = Etudiant(name, note1, note2)
    etudiant.afficher()