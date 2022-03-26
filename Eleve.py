from PROJET_PYTHON import mycursor,listeValide,mydb
import random
Insert_Eleve = "INSERT INTO Eleve(numero,prenom_el,nom_eleve,Date_naissance,id_classe) VALUES (%s,%s,%s,%s,%s)"
tabEleve = []
tabcles=[]
mycursor.execute("SELECT id_classe FROM classe")
for b in mycursor.fetchall():
    tabcles.append(b[0])
for numero in listeValide:
    g= (numero['code'],numero['prenom'],numero['nom'],numero['Date'],random.choice(tabcles))
    tabEleve.append(g)
mycursor.executemany(Insert_Eleve,tabEleve)
# mydb.commit()