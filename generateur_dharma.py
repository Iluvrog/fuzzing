import subprocess
from subprocess import PIPE


def create_command(nb = 10, file_name = "ftp_grammar.dg"):
    commande_base = "dharma -grammars"
    commande = commande_base + " " + file_name + " -count " + str(nb)
    return commande



p = subprocess.Popen(create_command(), shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print(out.decode("utf-8"))

