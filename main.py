# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:53:04 2023

@author: geoff
"""

import src.generateur_dharma as gd



def main():
    list_command = gd.generate_dharma()
    string = "Liste des commandes générées :\n"
    for c in list_command:
        string += "- " + c + "\n"
    gd.write_file(string)
    
if __name__ ==  "__main__":
    main()