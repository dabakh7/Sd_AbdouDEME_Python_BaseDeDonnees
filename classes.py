from PROJET_PYTHON import listeValide,mycursor,mydb


sqlclas ="INSERT INTO classe(nom_classe) VALUE (%s)"
tabClas = []
tabClasse = []
for k in listeValide:
    tabClas = (k['classe'],)
    for clas in tabClas:
        if clas not in tabClasse:
            tabClasse.append(clas)
for m in tabClasse:
    mycursor.execute(sqlclas,(m,))
# mydb.commit()