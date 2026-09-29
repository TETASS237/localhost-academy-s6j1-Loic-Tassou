#========================================
#  Exercice 1
# ==========================================
# note = float(input("Quel est votre note sur 20 : "))
# if note > 16 :
#     print('Excellent')
# elif note >= 12 :
#     print('Bien')
# else :
#     print('Insufisant')

# =========================================
# EXERCICE 2
# =========================================
# for i in range(1, 11) :
#     print(i, i**2)


#  a : parceque range affiche jusqu'au nombre stop-1 => range (start, stop)

# B - La boucle 
# for i in range(21) : 
#     if i % 2 == 0 :
#         print(i)
#     else : 
# #         continue
# c- boucle qui calcul la somme
# somme = 0
# for i in range(1,101) :
#     somme = somme + i
  

# print(somme)
# # EXO 3
# mot_de_passe = "python2026"
# tentative = 3


# mot = input('Entrez votre mot de passe : ')  

# while tentative <= 3 :
#     mot = input('Entrez un mot de passe : ')
#     tentative +=1
#     if mot != mot_de_passe :
#         continue
#     else : 
#         'break'
#========================================================
#  EXERCICE 4 :
# =====================================================
# def est_pair(n) :
#     if n % 2 == 0 :
#         return('true')
#     else :
#         return('false')
# print(est_pair(4))

# def max(a, b) :
#     if a> b :
#         return a
#     else :
#         return b
# print(max(12, 5))

# def compter_voyelles(mot) :
#     voyelles = ["a,", "e", "i", "o", "u"]
#     nombre_voyelles = 0
#     for letter in mot :
#         if letter in voyelles :
#             nombre_voyelles = nombre_voyelles +1
#     print(nombre_voyelles)
# (compter_voyelles('Joyeux'))
# ===============================================
# Exercice 5 
# ==============================================
# 1-
# def presenter(nom, ville="Yaounde"):
#     print(f"{nom} habite a {ville}.")
# presenter("TEKEU")
# presenter('TEKEU', "Bafoussam")
# 2-
# def somme_totale(*nombres) :
#     return sum(nombres)

#print(somme_totale(1,5,34))
# =====================================
# Exercice 6
# =======================================
#  La fonction original ne marchait pas parceque solde etait defini à l'exterieur de la fonction
# def retirer(montant):
#     solde = 1000
#     solde = solde- montant
#     return solde
# nouveau_solde = retirer(200)
# print(nouveau_solde)    
# ===========================================
# # Bonus
# ============================================
for i in range(0,51) : 
   
    if i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 2 == 0 :
        print('fizzbuzz')
    else : 
        print(i)
    