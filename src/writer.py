# Utilisé pour créer le dossier où sera écrit le résultat de la commande dharma
import os

from datetime import datetime

# write_file(string, file_name = "resultat_dharma.txt", directory = "./resultat/", mode = 'w')
# Va, s'il n'existe pas créer le dossier **directory**
# Va ensuite écrite **string** dans le fichier **file_name**
# du répertoire **directory** dans le mode **mode**
# Entrées :
## string : le message à écrire
## file_name : le nom du fichier, par défaut resultat_dharma.txt
## directory : le nom du dossier où est écrit **file_name**, par défaut ./resultats/
## mode : le mode d'écriture (entre 'w' et 'a'), par défault 'w'
#Sortie : rien
def write_file(string, file_name = "resultat_dharma_test.txt", directory = "./resultats/", mode = 'w'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory + file_name, mode)
    f.write(string)
    f.close()
    
def write_error(string, file_name = "error.txt", directory = "./resultats/", mode = 'a'):
    write_file(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " : \n" + string + "\n\n", file_name = file_name, directory=directory, mode=mode)