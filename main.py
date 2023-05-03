import src.generateur_dharma as gd



def main():
    list_command = gd.generate_dharma()
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    gd.write_file(string)
    
if __name__ ==  "__main__":
    main()