from dharma import load_grammar

# Chargement de la grammaire à partir d'un fichier externe
ftp_grammar = load_grammar("ftp_grammar.dg")

# Génération des entrées de test
for i in range(10):
    input_data = ftp_grammar.generate("<start>")
    print(input_data)