import subprocess
from subprocess import PIPE

nb = 10
commande_base = "dharma -grammars"
file_name = "ftp_grammar.dg"
command = commande_base + " " + file_name + " -count " + str(nb)

p = subprocess.Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print(out.decode("utf-8"))

