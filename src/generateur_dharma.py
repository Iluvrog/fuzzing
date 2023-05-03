# Utilisé pour générer les mots via dharma
import subprocess
from subprocess import PIPE

# Utilisé pour créer le dossier où sera écrit le résultat de la commande dharma
import os


# create_command(nb = 10, dharma_grammar = "ftp_grammar.dg")
# Va créer la commande utilisé pour générer des mots via dharma
# Entrées :
## nb : le nombre de mots généré, 10 par défaut
## dharma_grammar : le fichier de grammaire de dharma, par défaut ftp_grammar.dg
# Sortie :
## La commande permet de générer **nb** mots via la grammaire **dharma_grammar**
def create_command(nb = 10, dharma_grammar = "ftp_grammar.dg"):
    commande_base = "dharma -grammars"
    commande = commande_base + " " + dharma_grammar + " -count " + str(nb)
    return commande

# generate_dharma(nb = 10, dharma_grammar = "ftp_grammar.dg")
# Va générer des mots via dharma
# Entrées :
## nb : le nombre de mots généré, 10 par défaut
## dharma_grammar : le fichier de grammaire de dharma, par défaut ftp_grammar.dg
# Sortie :
## Renvoie une liste de **nb** mots généré via la grammaire **dharma_grammar**
def generate_dharma(nb = 10, dharma_grammar = "dharma_grammars/ftp_grammar.dg"):
    p = subprocess.Popen(create_command(nb = nb, dharma_grammar = dharma_grammar), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    list_command = out.decode("utf-8").replace('\r', '').split("\n\n")
    list_command.pop()
    return list_command

# write_file(string, file_name = "resultat_dharma.txt", directory = "./resultat/", mode = 'w')
# Va, s'il n'existe pas créer le dossier **directory**
# Va ensuite écrite **string** dans le fichier **file_name**
# du répertoire **directory** dans le mode **mode**
# Entrées :
## string : le message à écrire
## file_name : le nom du fichier, par défaut resultat_dharma.txt
## directory : le nom du dossier où est écrit **file_name**, par défaut ./resultat/
## mode : le mode d'écriture (entre 'w' et 'a'), par défault 'w'
#Sortie : rien
def write_file(string, file_name = "resultat_dharma.txt", directory = "./resultat/", mode = 'w'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory + file_name, mode)
    f.write(string)
    f.close()
    

def main():
    list_command = generate_dharma()
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    write_file(string)
    
if __name__ ==  "__main__":
    main()