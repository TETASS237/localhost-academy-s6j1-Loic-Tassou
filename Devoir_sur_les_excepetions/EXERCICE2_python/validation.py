#  Question 1

def verifier_priorite(valeur) :
   
    if valeur == "basse" or valeur == "haute" :
        return valeur
    else :
        raise ValueError("La priorité doit-être basse ou haute")