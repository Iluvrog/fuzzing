import src.generateur_dharma as gd
import src.writer as w
import src.ftp as FTP



def main():
    # Génération des commandes 
    list_command = gd.generate_dharma(nb = 50)
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    w.write_file(string)
    
    # connection au serveur FTP local
    ftp = FTP.connexion() 
    
    if ftp == None:
        return 1
       
    # envoie des commandes
    res, err = FTP.send_command(ftp, list_command)
  
    
if __name__ ==  "__main__":
    main()
