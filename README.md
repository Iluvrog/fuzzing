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

## Description de la dharma

Notre dharma va renvoyé une **command_complete**

Une **command_complete** est constitué soit :

  - d'une **command**
  - d'une **commande** et d'un **argument** séparé par un espace

Un **argument** est soit :

  - un **word**
  - un **path**
  - un **filename**
  - un **path** suivie d'un **filename** sans séparation
  - un **char**
  - un **filename**
  - un **password**
  - un **username** et un **password** séparé par un :

Une **command** est une commande accepter par ftp

Un **username** est un **word**

Un **password** est soit :

  - un **char**
  - un **char_spec**
  - un **password** suivi d'un **char**
  - un **password** suivi d'un **char_spec**

C'est donc une liste de **char** et de **char_spec**

Un **path** est soit :

  - un **path_rel**
  - un **path_abs**

Un **path_rel** est un chemin relatif, c'est donc soit :

  - ./
  - ../
  - un **word** suivi d'un /
  - un **path_rel** suivi d'un **word** suivi d'un /

Un **path_abs** est un chemin absolu, c'est donc soit :

  - /
  - / suivi d'un **path_abs_chunk** suiv d'un /

Un **path_abs_chunk** est soit :

  - un **word**
  - un **path_abs_chunk** suivi d'un / suivi d'un **word**

Un **filename** est un nom de fichier, il est donc composé d'un **filename_wt_ext** et d'une **ext** séparé par un .

Un **filename_wt_ext** est un nom de fichier sans extension, il est donc soit :

  - un **word**
  - deux **word** séparés par un .

Une **ext** est une extension de fichier commune

Un **word** est une suite de **char**, il est donc soit :

  - un **char**
  - un **word** suivi d'un **char**

Un **char_spec** est une liste de charactère spéciaux (+ \ _ - < > | ? !)

Un **char** est un charactère entre a et z ou entre 0 et 9
