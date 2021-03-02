#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:38:15 2021

@author: Saadia Bayou
"""


# Imports bibliothèques matplotlib et numpy 
import matplotlib.pyplot as plt
import numpy as np

# Données - constantes
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  

# Initialisations Listes longeurs d'ondes et Energies
lambdas=[]
Energies=[]

# Données - variables
n1=1
n=[2,3,4,5,6] 

# Fonction de conversions

#metre -> nanometre
def convert_m_nm (l):
    """Convertit une grandeur en mètre en nanomètre"""
    L=l*(1e+09)
    return L
# nanometre -> metre
def convert_nm_m(l):
    """ Convertit une grandeur en nanomètre en mètre """
    L=l/(1e+09)
    return L
    
def convert_J_ev (EJ):
    """ Convertit une grandeur en  Joule en electronvolt """
    return EJ/evJ 

# Fonction calcul de la longeur d'onde
def calcul_lambd(n1,n2):
    lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
    lambd=convert_m_nm (lambd)
    lambd=round(lambd,2) 
    return lambd

# Boucle de calcul longueur d'onde
for n2 in n:
    lambd=calcul_lambd(1,n2)
    lambdas.append(lambd)

# Liste longeurs d'ondes calculées en nm
print("\nlambdas(nm) =",lambdas)

# Boucle calcul énergies de transitions
for l in lambdas:
    l=convert_nm_m(l)
    E=(h*c)/l
    E=convert_J_ev(E)
    E=round(E,2)
    Energies.append(E)

# Liste énergies de transition calculés en eV 
print("\nEnergies (ev) =",Energies)


# Tableaux de valeurs
n2=np.array([2,3,4,5,6]) # niveaux quantiques
#lambdas=np.array(lambdas) # longeurs d'ondes en nm
E=np.array(Energies)


# Tracé de l'énergie de transition en fonction des niveau quantiques
plt.plot(E,n2)

# titre graphe 
plt.title("Energie de transition - Serie de Lyman")

# légendes courbes 
plt.xlabel("Energies de transition - E(n) en ev")
plt.ylabel("Niveau quantique ,  n ")

# Sauvegarde - génère le graphe sous un format image .png 
plt.savefig("fig E(n).png")
# Affichage de la figure
plt.show()

