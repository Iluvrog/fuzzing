import subprocess
from subprocess import PIPE
import os


def create_command(nb = 10, dharma_grammar = "ftp_grammar.dg"):
    commande_base = "dharma -grammars"
    commande = commande_base + " " + dharma_grammar + " -count " + str(nb)
    return commande

def generate_dharma(nb = 10, dharma_grammar = "ftp_grammar.dg"):
    p = subprocess.Popen(create_command(nb = nb, dharma_grammar = dharma_grammar), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    list_command = out.decode("utf-8").replace('\r', '').split("\n\n")
    list_command.pop()
    return list_command

def write_file(string, file_name = "resultat_dharma.txt", directory = "./resultat/", mode = 'w'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory + file_name, mode)
    f.write(string)
    

def main():
    list_command = generate_dharma()
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    write_file(string)
    
if __name__ ==  "__main__":
    main()