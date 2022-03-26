from PROJET_PYTHON import mycursor,listeValide,mydb
import random

# inserer_id="INSERT INTO note(id_eleve,id_mat) VALUES (%s)"
mycursor.execute("select id_eleve,numero FROM Eleve")
tab_eleve=[]
compototal=[]
tab_note_etudiant = []
for eleve in mycursor.fetchall():
    tab_eleve.append(eleve)
# print(tab_eleve)


mycursor.execute("select id_mat,nom_matiere FROM matiere")
tab_matiere=[] 
compototal=[]
for matiere in mycursor.fetchall():
    tab_matiere.append(matiere)
# print(tab_matiere)



for ligne in listeValide:

    notes=ligne.get('Note')
    numero_etu =ligne.get('code')

    for matiere in notes:
        devoirs = notes[matiere]['devoir']
        comp = notes[matiere]['composition']

        for element in tab_matiere:
            if element[1] == matiere:
                idMatiere = element[0]
                # print('Correspondance', matiere, idMatiere)

        for element in tab_eleve:
            if element[1] == numero_etu:
                idEleve = element[0]
                # print('Correspondance', numero_etu, idEleve)
        #tab_note_etudiant.append((numero_etu,matiere,devoirs,comp,idEleve,idMatiere))
        
        
        insert_note="INSERT INTO note(Notes,type,id_eleve,id_mat) VALUES (%s,%s,%s,%s)"
        mycursor.execute(insert_note,(comp,'composition',idEleve,idMatiere))
        for dev in devoirs:
            mycursor.execute(insert_note,(dev,'devoir',idEleve,idMatiere))
    # mydb.commit()

        



    #for tout_note in tab_note_etudiant:
        # print(entrer_note)
        #mycursor.executemany(insert_note,tout_note)
    #mydb.commit
    # print(tab_note_etudiant[0])
    # break


    # break
    # notes = ligne.get('Note')
    # for matiere in notes:
    #     note_matiere = notes.get(matiere)
    #     # print(matiere, note_matiere)
    #     for dev_comp in note_matiere:
    #         if dev_comp !='devoir':
    #             valeur = note_matiere.get(dev_comp)
    #             compototal.append((valeur,ele))
    #             # print(compototal)
    #             #insert_compo = "INSERT INTO note (Notes,type,id_eleve,id_mat) VALUES (%s,'composition',%s,'11')"
    #             for m in compototal:
    #                 pass
    #                 #mycursor.execute(insert_compo,(m))
    #             # mydb.commit()
    #         else:
    #             pass
    #             #valeur = (note_matiere.get(dev_comp)[0],note_matiere.get(dev_comp)[1],ele)
    #             #insert_devoir = "INSERT INTO note (Notes,type,id_eleve,id_mat) VALUES (%s,'devoir'%s,%s,'10')"
    #             # for h in valeur:
    #             #     print(h)
    #             #mycursor.execute(insert_devoir,valeur)
    #         # mydb.commit()
    # # # mycursor.execute(inserer_id,valeur)



    # break