from validation import verifier_priorite 
from tâches import ajouter_tache 

taches = []
while True :
    titre = input('Entrez un titre : ')
    priorite = input('Entrez votre priorité : ')

    try :
        verifier_priorite(priorite)
        ajouter_tache(taches, titre, priorite)
        print(taches) 
        
    except ValueError :
        print("error")
    else :
        break