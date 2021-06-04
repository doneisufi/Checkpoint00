text1 = """Ok, bon laissez moi tout de meme vous la raconter.\n
Le petit Carl Friedrich Gauss etait un peu dissipe en classe.\n
Le maitre agace, par l'agitation de sa classe decida,\n 
de calmer sa classe a coup d'interrogation surprise.\n
Comme tout bon instituteur qui se respecte !"""

text2 = """Mangez une pomme c'est bon pour la santé ...
Elle est loin l'époque ou l'on pouvait mettre des fessées ..."""

text3 = """Très écoutez attentivement la suite.
L'instituteur posa le problème suivant :
Que vaut la somme de tous les nombre de 1 à 100 ?
L'instituteur pensant avoir un long moment de répit,
entendit la petite voix de Carl dire timidement '5050...'
nStupéfait de l'exactitude du résultat, il lui donna une autre punition à accomplir...
nLa dernière ligne est purement fictive."""



question_1 = input("Bonjour, connaissez vous la lègende du petit Gauss ?\n\nOui / Non\n\n")

if(question_1 == "Oui"):
    print("Super !" + " " + text1)
    question_2 = input("Cela vous offusque ?\n\nOui / Non\n\n")

    if (question_2 == "Oui"):
        print(text2)
    
    elif (question_2 == "Non"):
        print(text3)


elif (question_1 == "Non"):
  print ("Google est vôtre ami, ou demandez à Igor.\n" + text1)
