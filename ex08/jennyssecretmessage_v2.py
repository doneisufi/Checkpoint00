def firstName():
     name = input("Quel est votre prénom ?\n")

     if (name == 'Johnny'):
         print("Je te déteste !")
     elif(name =='Paul' or name == 'Marc'):
        print("Hello my love !")
     else:
         print ("Salut, désolé pas le temps de te parler.")

firstName()