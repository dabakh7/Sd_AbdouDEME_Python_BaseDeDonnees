from PROJET_PYTHON import listeValide,mycursor,mydb


sqlMat = "INSERT INTO matiere(nom_matiere) VALUE (%s)"
tabMat = []
for student in listeValide:
    for key in student['Note'].keys():
        key = key.strip()
        if key.startswith('M'):
            key = 'Math'
        elif key.startswith('F'):
            key = 'Francais'  
        elif key.startswith('A'):
            key = 'Anglais'
        elif key.startswith('Science'):
            key = 'PC'
        if key not in tabMat:
            tabMat.append(key)
for k in tabMat:
    mycursor.execute(sqlMat,(k,))
# mydb.commit()
# print(len(tabMat))
# print(tabMat)

