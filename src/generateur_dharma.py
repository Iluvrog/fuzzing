# Utilisé pour générer les mots via dharma
import subprocess
from subprocess import PIPE

import src.writer as w


# create_command(nb = 10, dharma_grammar = "ftp_grammar.dg")
# Va créer la commande utilisé pour générer des mots via dharma
# Entrées :
## nb : le nombre de mots généré, 10 par défaut
## dharma_grammar : le fichier de grammaire de dharma, par défaut ftp_grammar.dg
# Sortie :
## La commande permet de générer **nb** mots via la grammaire **dharma_grammar**
def create_command(nb = 10, dharma_grammar = "dharma_grammars/pure-ftpd_grammar.dg"):
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
def generate_dharma(nb = 10, dharma_grammar = "dharma_grammars/pure-ftpd_grammar.dg"):
    p = subprocess.Popen(create_command(nb = nb, dharma_grammar = dharma_grammar), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    list_command = out.decode("utf-8").replace('\r', '').split("\n\n")
    list_command.pop()
    return list_command

