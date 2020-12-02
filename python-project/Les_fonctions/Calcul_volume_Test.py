#Ne pas oublier de changer le module à importer
module="Les_conditions/Calcul_volume"

import sys
import io
from ma_bao import *
tester("from Calcul_volume import volume ",globals())

def f_sol(L,l,h):
  return L*l*h
  
#liste des couples input/output
input_output=[(0,0,0),(1,1,1),(1,9,5),(9,1,5),(0.5,1.5,2.5)]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"

#Afficher la correction
def afficher_correction():
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp in input_output:
        outp=f_sol(*inp)
        count1=volume(*inp)
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
