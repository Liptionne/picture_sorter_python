#-----------------------------------------------------------------------------------------------------------------------------------
#   Importation des librairies, et création des variables
#-----------------------------------------------------------------------------------------------------------------------------------

import os
import shutil
from tqdm import tqdm

repertoire_debut = input("entrez le chemin du dossier à trier : ")
choix = input("voulez vous trier les photos dans ce dossier ? (y/n)")

DOSSIERS = ['JPG','RAW','AUTRE']

EXT_JPG = ['.jpg','.svg','.png','.gif','.bmp','.JPG']

EXT_RAW = ['.CR2','.CR3','.RW2','.NEF']

D = EXT_JPG+EXT_RAW


#-----------------------------------------------------------------------------------------------------------------------------------
#   Création des fonction des déplacement, de suppression des doublons, et de vérification
#-----------------------------------------------------------------------------------------------------------------------------------

def verif():
    print("vérification des dossiers")
    for D in DOSSIERS:      # VERIFIE SI TOUT LES DOSSIERS NECESSAIRES SONT LA  
        if not os.path.isdir(D):
            print("Dossier {} manquant".format(D))
            os.mkdir('.\{}'.format(D))      # CREE UN DOSSIER SI IL EST MANQUANT   
            print("Dossier",D,"créé")
    print("tout les dossiers sont là")
    return

def deplacement(repertoire_debut,repertoire_fin):

    compteur = 0
    
    files = os.listdir(repertoire_debut)        # FAIS LA LISTE DES DOSSIERS ET FICHIERS PRESENTS DANS LE DOSSIER REPERTOIRE_DEBUT   
    files.sort()

    dossier_jpg = repertoire_fin+"\JPG"     #Création de variables avec les chemins de chaque dossier
    dossier_raw = repertoire_fin+"\RAW"
    dossier_autre = repertoire_fin+"\AUTRE"

    for f in tqdm(files):
        nom, extension = os.path.splitext(f)        # DISSOCIE LE NOM ET L'EXTENSION DU FICHIER
        #print(extension)
        if extension in EXT_JPG:
            #print("déplacement de "+f+" dans le dossier JPG")     # TRIE DANS LES DIFFERENTES CATEGORIES TRAITEES
            shutil.move(repertoire_debut+"/"+f,dossier_jpg)
        if extension in EXT_RAW:
            #print("déplacement de "+f+" dans le dossier RAW")
            shutil.move(repertoire_debut+"/"+f,dossier_raw)
        if extension == '':     # SI PAS D'EXTENSION ALORS C'EST UN DOSSIER : ON NE FAIT RIEN
            pass
        if extension == '.py':
            pass
        if extension not in D and extension != '' and extension != '.py':      # SI PAS DANS LES EXTENSION TRAITEES ET PAS UN DOSSIER ALORS ON LE TRIE PAS ET ON MET DANS AUTRES
            #print("déplacement de "+f+" dans le dossier AUTRE")
            shutil.move(repertoire_debut+"/"+f,dossier_autre)
        compteur += 1
        #print(compteur,'/',len(files),"("+str((compteur/len(files))*100)+"%)")
    print("DEPLACEMENT TERMINE")

def sup_raw(repertoire_fin):
    L=[]
    files = os.listdir(repertoire_fin+'/JPG')   #Crééer une liste avec les fichiers du dossier JPG
    files_R = os.listdir(repertoire_fin+'/RAW') #Crééer une liste avec les fichiers du dossier RAW
    #print(files)
    #print(files_R)
    for R in files_R:
        nom, extension = os.path.splitext(R)
        L.append(nom)   #Crééer une liste avec les noms des fichers du dossier RAW sans l'extension
    #print('Liste des fichiers RAW : ',L)
    for f in L:
        if f+'.JPG' not in files:
            os.remove(repertoire_fin+'/RAW/'+f+'.CR3')  #Si le JPG du RAW n'existe plus, c'est que le JPG a été supprimé.
                                                        #Donc on supprime le RAW associé à ce JPG

"""
Cette partie sert à appeller les différentes fonctions, 
"""

if choix == "y" or choix == "Y":
    choix3 = input("voulez vous un sous-dossier ? ")
    repertoire_fin = repertoire_debut

    if choix3 == 'n' or choix3 == 'N':
        print("le repertoire de debut et de fin seront les mêmes")
        os.chdir(repertoire_debut)
        verif()
        #Si on trie dans le même dossier, alors les répertoires de début et de fin sont confondus
        #print(repertoire_fin)
        deplacement(repertoire_debut,repertoire_fin)
    
    if choix3 == 'y' or choix3 == 'Y':
        os.chdir(repertoire_fin)
        sous_rep = input("entrez le nom de votre sous-dossier : ")
        os.mkdir('.\{}'.format(sous_rep))
        repertoire_fin = repertoire_fin+'/'+sous_rep
        os.chdir(repertoire_fin)
        verif()
        os.chdir(repertoire_debut)
        #print(repertoire_fin)
        deplacement(repertoire_debut,repertoire_fin)

if choix == "n" or choix == "N":
    repertoire_fin = input("entrez le chemin du dossier de fin : ")
    choix3 = input("voulez vous un sous-dossier ? ")
    if choix3 == "y" or choix3 == "Y":
        os.chdir(repertoire_fin)
        sous_rep = input("entrez le nom de votre sous-dossier : ")
        os.mkdir('.\{}'.format(sous_rep))
        repertoire_fin = repertoire_fin+'/'+sous_rep


    os.chdir(repertoire_fin)
    verif()
    os.chdir(repertoire_debut)
    #print(repertoire_fin)
    deplacement(repertoire_debut,repertoire_fin)

choix2 = input("voulez vous supprimer les RAW sans JPG ? (y si oui) ")

if choix2 == 'y' or choix2 == 'Y':
    sup_raw(repertoire_fin)
