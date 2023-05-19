from ftplib import FTP
import src.writer as w


# connexion(port = 21, host = 'localhost')
# Va créer la connexion vers un serveur ftp
# Entrées :
## port : le prt de la conexion, par défault 21
## host : l'adresse du serveur, par défault localhost
# Sortie :
## la connexion FTP, None si impossible de la créer
def connexion(port = 21, host = 'localhost'):
    try:
        co = FTP()
        co.connect(host, port)
        co.login()
        return co
    except Exception as e:
        print("Erreur lors de la connexion:", e)
        w.write_error("Erreur lors de la connexion:" + str(e))
        return None

# send_command(ftp, list_command, file_name = 'error.txt')
# Va envoyer une liste de commande au serveur ftp
# Entrées :
## ftp : la connexion ftp vers où envoyé les commandes
## list_command : la liste des commandes à envoyé au serveur
## file_name : le fichier où écrire les erreurs, par défault error.txt (dans le dossier resultat)
# Sortie :
## On renvoie le résultat des commandes ainsi que celle qui on créé une erreur
def send_command(ftp, list_command, file_name = 'error.txt'):
    res = ""
    error = ""
    for com in list_command:
            try:
                res += ftp.sendcmd(com) + "\n"
            except Exception as e:
                # if error -> save to file ?
                w.write_error("Commande : " + com + ", resultat : " + str(e) + "\n")
                error += "Commande : " + com + ", resultat : " + str(e) + "\n"
    return res, error