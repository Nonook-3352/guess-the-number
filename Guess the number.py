import random 

inp = input("Choisi un nombre de tentative : ")
win = False
#début
print("BIENVENUE DANS : Guess the number !")
print(" ")
print(f"Tu as {inp} tentavive de trouvez le nombres mystère qui se trouvent entre 1 et 100.")
print(" ")

#nombre choisi
number = random.randint(1, 100)




for i in range(0, int(inp)):
        #input
        choix = input("donnez un nombre : ")
        #var pour boucle infini


        if int(choix) < number :
                print("Le nombre que tu a proposez est plus petit que le nombre mystère.")
        if int(choix) > number :
                print("Le nombre que tu a proposez est plus grand que le nombre mystère.")
        if int(choix) == number :
                print("bravo tu a trouvez le nombre mystère") 
                print(number)
                win = True
                
                
if win != True:
    print("Tu as perdu !")
