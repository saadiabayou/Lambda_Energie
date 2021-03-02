# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:35:28 2021

@author: Saadia Bayou
"""

""" Ce programme trace le graphe des valeurs des longueurs d'ondes lambda 
    en fonction des niveaux quantiques n2 , de la Serie de Lyman n1=1 """


# Imports des bibliothèques matplotlib et numpy 
import matplotlib.pyplot as plt
import numpy as np

# Tableaux de valeurs
n2=np.array([2,3,4,5,6]) # niveaux quantiques
lambd=np.array([122,103,97,95,94]) # longeurs d'ondes en nm

# Tracé des longeur d'onde en fonction des niveau quantiques
plt.plot(lambd,n2)

# titre graphe 
plt.title("Serie de Lyman")

# légendes courbes 
plt.xlabel("Longueur d'onde en nm - lambda (n)")
plt.ylabel("Niveau quantique ,  n ")

# Sauvegarde - génère le graphe sous un format image .png 
plt.savefig("fig lambda(n).png")
# Affichage de la figure
plt.show()






