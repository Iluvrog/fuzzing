import subprocess
from subprocess import PIPE


def create_command(nb = 10, file_name = "ftp_grammar.dg"):
    commande_base = "dharma -grammars"
    commande = commande_base + " " + file_name + " -count " + str(nb)
    return commande

def generate_dharma(nb = 10, file_name = "ftp_grammar.dg"):
    p = subprocess.Popen(create_command(nb = nb, file_name = file_name), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    list_command = out.decode("utf-8").replace('\r', '').split("\n\n")
    list_command.pop()
    return list_command

def write_file(string, file_name = "resultat_dharma.txt", mode = 'w'):
    f = open(file_name, mode)
    f.write(string)
    

list_command = generate_dharma()
string = "Liste des commandes générées :\n"
for c in list_command:
    string += "- " + c + "\n"
write_file(string)