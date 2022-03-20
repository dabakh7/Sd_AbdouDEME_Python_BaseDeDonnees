# script créé le : Fri Mar 11 11:29:16 GMT 2022 -   syntaxe MySQL ;
USE Exercice1_python;
# use  VOTRE_BASE_DE_DONNEE ;

DROP TABLE IF EXISTS matiere ;
CREATE TABLE matiere (id_mat INT(50) NOT NULL,
nom_matiere VARCHAR(255),
PRIMARY KEY (id_mat) ) ENGINE=InnoDB;

DROP TABLE IF EXISTS classe ;
CREATE TABLE classe (id_classe INT NOT NULL,
nom_classe VARCHAR(255),
PRIMARY KEY (id_classe) ) ENGINE=InnoDB;

DROP TABLE IF EXISTS Eleve ;
CREATE TABLE Eleve (numero VARCHAR(100) NOT NULL,
prenom_el VARCHAR(100),
nom_eleve VARCHAR(50),
Date_naissance VARCHAR(10),
id_classe INT NOT NULL,
PRIMARY KEY (numero) ) ENGINE=InnoDB;

DROP TABLE IF EXISTS note ;
CREATE  TABLE   note (
    id_note INT PRIMARY KEY AUTO_INCREMENT,
    Notes FLOAT,
    type VARCHAR(50),
    id_eleve INT,
    id_mat INT
    ) ENGINE=InnoDB;

DROP TABLE IF EXISTS MOYENNE ;
CREATE  TABLE   MOYENNE (
    id_moyenne INT PRIMARY KEY AUTO_INCREMENT ,
    valeur_moyenne FLOAT ,
    id_eleve INT) ENGINE=InnoDB;

ALTER TABLE Eleve ADD CONSTRAINT FK_Eleve_id_classe FOREIGN KEY (id_classe) REFERENCES classe (id_classe);
ALTER TABLE note ADD CONSTRAINT FK_note_numero FOREIGN KEY (id_eleve) REFERENCES Eleve (id_eleve);
ALTER TABLE note ADD CONSTRAINT FK_note_numero FOREIGN KEY (id_mat) REFERENCES matiere (id_mat);
ALTER TABLE MOYENNE ADD CONSTRAINT FK_MOYENNE_id_eleve FOREIGN KEY (id_eleve) REFERENCES Eleve (id_eleve);
