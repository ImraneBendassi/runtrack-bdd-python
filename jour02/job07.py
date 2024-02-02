import mysql.connector

class Employe:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imrane13",
            database="entreprise"
        )
        self.curseur = self.connexion.cursor()

    
    def recuperer_employes(self):
        self.curseur.execute("SELECT * FROM employe")
        employes = self.curseur.fetchall()
        return employes

    def inserer_employe(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(sql, valeurs)
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()


employe = Employe()
employe.inserer_employe("Doe", "John", 3500.00, 1)
employes = employe.recuperer_employes()
for e in employes:
    print(e)
employe.fermer_connexion()
