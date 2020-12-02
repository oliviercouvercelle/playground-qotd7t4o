#Ne pas oublier de changer le module à importer
module="Les_boucles/Champernowne"

import sys
import io
from ma_bao import *
tester("from Champernowne import ma_fonction",globals())

#liste des couples input/output
input_output=[\
(1,0.1),\
(2,0.12),\
(7,0.1234567),\
(10,"0.12345678910"),\
(100,"0.123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100"),\
(0,0)\
]

# Si le mot de passe est bon on affiche la correction
try :  
    cheat(module,mdp) 
except: pass

#message d'aide si besoin
help="Attention si n est nul, le nombre de Champernowne vaut 0 aussi"

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
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        ma_fonction(inp)
        count1 = sys.stdout.getvalue()
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant la valeur {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant la valeur {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
