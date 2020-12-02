#Ne pas oublier de changer le module à importer
from fonction_pluriel import pluriel as f
import sys
import io


#liste des couples input/output
input_output=["test","maths","sinus","Triangle","miss","cheval"]

#la fonction attendue:
def reponse(mot):
  if mot[-1]!="s":
    return mot+"s"
  else:
    return mot

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for x in input_output:
        assert f(x) == reponse(x), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(x)),str(reponse(x)))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
