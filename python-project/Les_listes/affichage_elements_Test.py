#Ne pas oublier de changer le module à importer
from affichage_elements import ma_fonction
import sys
import io


#liste des couples input/output
input_output=[\
(["un mot"],"un mot"),\
(["mot 1","mot 2"],"mot 1\nmot 2"),\
(["maths", "info", "python", "exposant", "alpha", "fonction", "parabole", "equilateral", "orthogonal", "cercle", "isocèle"],"maths\ninfo\npython\nexposant\nalpha\nfonction\nparabole\nequilateral\northogonal\ncercle\nisocèle") \
]


#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        ma_fonction(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), r"En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),repr(str(count1)),repr(str(outp)))
        send_msg("Tests validés",r"En testant les valeurs {} le résultat obtenu est bien :".format(str(inp)))
        for mot in inp:
            send_msg("Tests validés", mot )
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
