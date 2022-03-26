from PROJET_PYTHON import mycursor,listeValide,mydb
import random
insert_moyenne = "INSERT INTO MOYENNE (valeur_moyenne,id_eleve) VALUES (%s,%s)"
mycursor.execute("SELECT id_eleve FROM Eleve")
Id_elevee =[]
moyenne =[]
for cle_eleve in mycursor.fetchall():
    Id_elevee.append(cle_eleve[0])
# print(Id_elevee)
for moy_eleve in listeValide:
    a= (moy_eleve['moy_gen'],random.choice(Id_elevee))
    moyenne.append(a)
    # print(moyenne)
for x in moyenne:
    mycursor.execute(insert_moyenne,(x))
# mydb.commit()