
import csv
from datetime import date
from doctest import DONT_ACCEPT_TRUE_FOR_1
from sqlite3 import connect

import mysql.connector 
import random

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Dabakh7.",
  database = "Exercice1_python"
)
mycursor = mydb.cursor()
if mydb.is_connected():
    print("bonjour mame dabakh")

def check_date(Date):
    chaine = ",;:' '._-"
    for i in chaine:
            Date = Date.replace(i,"/")
            Date = Date.strip()
    return Date

def classeExact(clas):
    if len(clas) > 0:
        if clas[0] in ["3","4","5","6"] and clas[-1] in ["A","B"]:
            classe = clas[0]+"em"+clas[-1]
            return classe
        else:
            return False
#################################################################
def mois(x):
    x =x.lower()
    if x in "janvier":
        return "01"
    elif x in ["fev","fèv","février"]:
        return "02"
    elif x in "mars":
        return "03"
    elif x in "avril":
        return "04"
    elif x in "mai":
        return "05"
    elif x in "juin":
        return "06"
    elif x in "juillet":
        return "07"
    elif x in ["aout","août"]:
        return "08"
    elif x in "septembre":
        return "09"
    elif x in "octobre":
        return "10"
    elif x in "novembre":
        return "11"
    elif x in "decembre":
        return "12"
    else:
        return None
#################################################################
def verify_date(j, m, a):
    try:
        d = date(a, m, j)
        return True
    except ValueError:
        return False
#print(verify_date(22, 12, 2020))

##################################################################


##################################################################
def transformdate(datees):
    try:
        datees=check_date((datees))
        datees=datees.split("/")
        x=len(datees)
        i=0
        while i<x:
            if datees[i]=="":
                del datees[i]
                x=x-1
                i=i-1
            i=i+1
        if len(datees) == 3:
            j=datees[0]
            m=datees[1]
            a=datees[2]
            if m.isalpha():
                m=mois(m)
                if(m!=None):
                    m=int(m)
                    if j.isdigit() and a.isdigit():
                        j = int(j)
                        a = int(a)
                        dateval = verify_date(j,m,a)
                    else:
                        dateval = False
                else:
                    dateval = False
            elif m.isdigit() and j.isdigit() and a.isdigit():
                m=int(m)
                j = int(j)
                a = int(a)
                dateval = verify_date(j, m, a)
            else:
                dateval = False
        else:
            dateval = False
        if dateval == True:
                j = str(j)
                m = str(m)
                a = str(a)
                dateval = a + "-" + m + "-" + j
    except ValueError:
        dateval = False
    return  dateval

###################################################################

####################Pour nottoyer les données et calculer les moyenne##################################
# tableaumoy = []
def separe_note_function(notes):
    matierNoteList=[]
    listeSQL=dict()
    valide = True
    composition = 0
    moyenne_general = 0
    if notes.startswith('#'):
        notes = notes[1:]

    note_recuperer = notes.split('#')
    MATIERE=dict()
    for k in note_recuperer:
        k = k.replace(',',';')
        cpt = 0
        note_recup = k.replace(']', '')
        # note_separer = note_recup.split('[')  #====>['matiere','notes']
        matiere = note_recup.split('[')[0]
        matierNoteList.append(matiere)
        # print(matiere)
        for l in note_recup:      ### Pour gèrer les notes qui ont plus d'une composition
            if l == ':':
                cpt = cpt + 1
        if cpt != 1:
            valide = False
        else:
            # valeur_note = note_separer[1]
            separer_comp_devoir = note_recup.split('[')[1].split(':')
            if separer_comp_devoir[1] == "":  ###Pour enlever les notes qui ont un vide
                valide = False
            else:
                # print(separer_comp_devoir)
                devoirs = separer_comp_devoir[0]
                composition = separer_comp_devoir[1]
                if int(composition) < 0 or int(composition) > 20:
                    valide = False
                else:
                    noteCompo = composition
                    
                    devoir = devoirs.split(';')
                    for z in range(len(devoir)-1):
                        if int(devoir[z]) < 0 or int(devoir[z]) > 20:
                            valide = False
                    if valide == True:
                        # print(matiere, devoir, composition)

                        somme = 0
                        for val in devoir:
                            matierNoteList.append(val)
                            MATIERE['devoir'] = devoir
                            MATIERE['composition'] = noteCompo
                            listeSQL[matiere]=MATIERE
                            #print("Liste SQL",listeSQL)
                            somme = somme + int(val)
                        
                        moyenne_devoir = somme / len(devoir)
                        # tableaumoy.append(moyenne_devoir)

                        # moyenne_general = calcul_moyenne(tableaumoy, composition)
                        # print(moyenne_general)
                        moyenne_matiere = (moyenne_devoir + (2 * int(composition))) / 3
                        moyenne_general = moyenne_general + moyenne_matiere
                        moyenne_devoir=str(moyenne_devoir)
                        moy=str("moyDevoir "+moyenne_devoir)
                        matierNoteList.append(moy)
                        noteCompo = str(noteCompo)
                        noteCompo = str("composition "+noteCompo)
                        matierNoteList.append(noteCompo)


    moyenne_general = round(moyenne_general / len(note_recuperer), 2)
    info: any
    if valide == True:
        info = moyenne_general
    else:
        info = valide
    return listeSQL, moyenne_general
# note ="Math[11;13:06] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]"
# print(separe_note_function(note)[0][0])
#####################################################################

    #di = "30:Fev;98"
    #print(transformdate(di))

with open("/home/abdou/PYTHON/Note_eleve.csv", 'r') as Note:
    myReader = csv.reader(Note)
    listeValide=[]
    liste =[]
    test = []
   
    listeinv =[]
    p=0
    for row in myReader:
        code=row[1]
        nom=row[2]
        prenom=row[3]
        Date=row[4]
        classe=row[5]
        matiere=row[6]
        infoEtudiant=dict()
        date1 = transformdate(Date)
        classe1 =classeExact(classe)
        
        if (row[1]!='' and row[2]!='' and row[3]!='' and row[4]!='' and row[5]!='' and matiere!='' ) and \
                (len(code)==7 and code.isupper() and code.isalnum() and len(nom)>=2 and nom[0].isalpha() and len(prenom)>=3 and prenom.isalpha()) \
                and classe1!=False and date1 != False and separe_note_function!= False:
                        moyenne11, moyG =separe_note_function(matiere)
                    
                        # print("moyenne11", moyenne11)
                        
                        # comp11 = separe_note_function(matiere)
                        # print()
                        # liste.append([code,nom,prenom,transformdate(Date),classe,comp11;moyenne11])
                        # p = p + 1

                        infoEtudiant['code'] = row[1]
                        infoEtudiant['nom']=row[2]
                        infoEtudiant['prenom']=row[3]
                        infoEtudiant['Date']=date1
                        infoEtudiant['classe']=classe1
                        infoEtudiant['Note'] = moyenne11
                        infoEtudiant['moy_gen'] = moyG
                        #print("Info etudiant",infoEtudiant)
                        listeValide.append(infoEtudiant)
    # print(listeValide)
        else :
            listeinv.append([code,nom,prenom,date,classe,matiere])
       

#######################Insertion matière dans la base de données#################

sqlMat = "INSERT INTO matiere(nom_matiere) VALUE (%s)"
tabMat = []
for student in listeValide:
    for key in student['Note'].keys():
        if key not in tabMat:
            tabMat.append(key)
for k in tabMat:
    mycursor.execute(sqlMat,(k,))
mydb.commit()
# print(len(tabMat))
# print(tabMat)

################ Insertion classe ####################

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
mydb.commit()

################# Insertion des notes ####################################
# inserer_id="INSERT INTO note(id_eleve,id_mat) VALUES (%s)"
mycursor.execute("select id_eleve FROM Eleve")
# mycursor.execute("select id_mat FROM matiere")
idEleve=[]
compototal=[]
for eleve in mycursor.fetchall():
    idEleve.append(eleve[0])
for ligne in listeValide:
    ele=random.choice(idEleve)
    # print(ele)
    notes = ligne.get('Note')
    for matiere in notes:
        note_matiere = notes.get(matiere)
        # print(matiere, note_matiere)
        for dev_comp in note_matiere:
            if dev_comp !='devoir':
                valeur = note_matiere.get(dev_comp)
                compototal.append((valeur,ele))
                # print(compototal)
                insert_compo = "INSERT INTO note (Notes,type,id_eleve,id_mat) VALUES (%s,'composition',%s,'11')"
                for m in compototal:
                    mycursor.execute(insert_compo,(m))
                mydb.commit()
            else:
                valeur = (note_matiere.get(dev_comp)[0],note_matiere.get(dev_comp)[1],ele)
                insert_devoir = "INSERT INTO note (Notes,type,id_eleve,id_mat) VALUES (%s,'devoir'%s,%s,'10')"
                # for h in valeur:
                #     print(h)
                mycursor.execute(insert_devoir,valeur)
            mydb.commit()
    # # mycursor.execute(inserer_id,valeur)
    break

#############################################################################

############################ IDENTIFIANT ELEVE####################################

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
mydb.commit()

############################ MOYENNE #######################
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
mydb.commit()