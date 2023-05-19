# Projet de fuzzing de pure-ftpd et light-ftp

## Le projet

Le but de notre projet est de créer un fuzzer permettant de trouver des failles de sécurité

dans les logiciels pure-tpd et light-fpt.

## La réalisation

Nous avons commencé par essayer de créer un fichier dharma avec chatGPT, ça n'a pas marcher.

Nous avons ensuite créer la dharma nous-même avant de créer un script python permettant de générer

des commandes avec cette dernière.

Nous avons continué sur notre lancer en faisant en sorte que notre programme se connecte en envoie

automatiquement les commandes vers un serveurs ftp.

## La description du programme

Notre programme est constitué d'un ficheir main.py, d'un dossier resultats (qui sera automatiquement

créé au premier lancement de main.py), d'un dossier dharma_grammars contenant notre dharma et

d'un dossier src contenant :

  - un fichier ftp.py contenant les fonctions permettant de se connecter au serveur et de lui envoyé des commandes
  - d'un fichier generateur_dharma.py permettant de créer les commandes selon la grammaire dharma donnée
  - d'un fichier writer.py permettant d'écrire les résultats dans les fichiers correspondant
