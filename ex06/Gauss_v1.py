text1 = """Ok, bon laissez moi tout de même vous la raconter.\n
Le petit Carl Friedrich Gauss était un peu dissipé en classe.\n
Le maître agacé, par l'agitation de sa classe décida,\n 
de calmer sa classe à coup d'interrogation surprise.\n
Comme tout bon instituteur qui se respecte !\n"""

text2 = "Mangez une pomme c'est bon pour la santé ...\n\n"

text3 = "Très écoutez attentivement la suite.\n"

text8 = """L'instituteur posa le problème suivant :\n
Que vaut la somme de tous les nombre de 1 à 100 ?\n
L'instituteur pensant avoir un long moment de répit,\n
entendit la petite voix de Carl dire timidement '5050...'\n
Stupéfait de l'exactitude du résultat, il lui donna une autre punition à accomplir...\n
La dernière ligne est purement fictive."""

text4 = "Oui ou Non, c'etait plus simple comme choix de réponse ..."

text5 ="\n\nC'est la deuxième fois que vous ne répondez pas.\n\n"

text6 = """Vous me prenez pour un imbécile à répondre à côté de la plaque, au revoir !
repl process died unexpectdetly: exit status 1"""

text7 = """Elle est loin l'époque ou l'on pouvait mettre des fessées ...
repl process died unexpectdetly: exit status 1"""



question_1 = input("Bonjour, connaissez vous la lègende du petit Gauss ?\n\nOui / Non\n\n")

if(question_1 == "Oui" or question_1 == "oui"):
    print("Super !\n\n" + text1)
    question_2 = input("Cela vous offusque ?\n\nOui / Non\n")

    if(question_2 == "Oui" or question_2 == "oui"):
        print(text2 + "\033[31m" + text7 + "\033[1m")
    
    elif(question_2 == "Non" or question_2 == "non"):
        print(text3 + text8)
    
    elif(question_2 == "Nan" or question_2 == "nan"):
        print(text8)
    
    elif(question_2 == "Nan" or question_2 == "nan"):
        print(text8)


elif(question_1 == "Non" or question_1 == "non"):
    print("Google est vôtre ami, ou demandez à Igor.\n" + text1)
    question_2 = input("Cela vous offusque ?\n\nOui / Non\n")

    if(question_2 == "Oui" or question_2 == "oui"):
        print(text2 + "\033[31m" + text7 + "\033[1m")
    
    elif(question_2 == "Non" or question_2 == "non"):
        print(text3 + text8)

    elif(question_2 == "Nan" or question_2 == "nan"):
        print(text8)
    
    elif(question_2 == "Nan" or question_2 == "nan"):
        print(text8)

elif(question_1 == "Jmenfou" or question_1 == "jmenfou"):
    print(text4 + "\n\n" + text1 + "\n")
    question_2 = input("Cela vous offusque ?\n\nOui / Non\n")

    if(question_2 == "Oui" or question_2 == "oui"):
        print(text2 + "\033[31m" + text7 + "\033[1m")
    
    elif(question_2 == "Non" or question_2 == "non"):
        print(text3 + text8)

    elif(question_2 == "Jmenfou aussi" or question_2 == "jmenfou aussi"):
        print(text4 + text5 + "\033[31m" + text6 + "\033[1m")
    
    elif(question_2 == "Nan" or question_2 == "nan"):
        print(text8)

