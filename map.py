class Map:
    #Labyrinthe niveau 1 (plan du labyrinthe)

    labyrinthe = [
    "###############",
    "#######    ####",
    "#x      ##    #",
    "#### ####### ##",
    "#### ###       #",
    "#     ### ## ##",
    "##### ### ## ##",
    "##### ### ##  #",
    "##    ### ## ##",
    "## ###### ## ##",
    "## ###### #####",
    "##            #",
    "##### #########\n",
    "#####         #",
    "###########O###",]

#Fonction d'affichage de notre labyrinthe
def affiche_labyrinthe(labyrinthe) :
    for ligne in labyrinthe :
        print(ligne)


