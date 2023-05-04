import src.generateur_dharma as gd
from ftplib import FTP


def main():
    # Génération des commandes 
    list_command = gd.generate_dharma()
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    gd.write_file(string)
    
    # connection au serveur FTP local
    host = 'localhost'
    port =  21
    ftp = FTP((host,port)) 
       
    # envoie des commandes
    for com in list_command:
            try:
                res = ftp.sendcmd(com)
            except:
                # if error -> save to file ?
                write_file(com)
  
    
if __name__ ==  "__main__":
    main()
