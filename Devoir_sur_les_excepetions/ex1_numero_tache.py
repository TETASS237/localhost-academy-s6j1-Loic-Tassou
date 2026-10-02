
# ================================Exercice 1 ===========================================

taches = ["Reviser Python", "Faire les exercices", "Lire le cours"]

#  Question 1
# print(taches[0])
# print(taches[1])
# print(taches[2])

# Question 2
# number = int(input("Entrez un numero"))
#  j'observe que int ne peut pas convertir les str en int.

# Questions 3 et 4

# try :
#     number = int(input("Entrez un numero : "))
            
# except ValueError :
#     print("Entrez un nombre entier")

# if number >= 1 and number <= len(taches) :
#     print("tache : ", number -1)
# else :
#     print('Choisissez un nombre entre 1 et 3')

# Question 5
# while True : 
#     try :
#         number = int(input("Entrez un numero : "))
            
#     except ValueError :
#         print("Entrez un nombre entier")

#     if number >= 1 and number <= len(taches) :
#         print("tache : ", number -1)
#     else :
#         print('Choisissez un nombre entre 1 et 3')

#     if len(taches) == 0 :
#         print("Liste vide")
# Question 6 
while True : 
    try :
        number = int(input("Entrez un numero : "))
            
    except ValueError :
        print("Entrez un nombre entier")

    else :

        if number >= 1 and number <= len(taches) :
            print("tache : ", number -1)
        else :
            print('Choisissez un nombre entre 1 et 3')

        if len(taches) == 0 :
            print("Liste vide")
    finally : 
        print('Fin de tentative')

# ===========================EXERCICE 2 ================================================




