import subprocess
from subprocess import PIPE



p = subprocess.Popen("dharma -grammars ftp_grammar.dg", shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print(out.decode("utf-8"))

