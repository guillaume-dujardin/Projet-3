class Map:
    #Labyrinthe niveau 1 (plan du labyrinthe)

    labyrinthe = [
    "############################",
    "#######    ############## ##",
    "#x      ##                ##",
    "#### ####### ############ ##",
    "#### ###                  ##",
    "#     ### ## ############ ##",
    "##### ### ## ###############",
    "##### ### ##     #####     G",
    "##    ### ## ### ##### ### #",
    "## ###### ## ### ##### ### #",
    "## ###### ###### ##### ### #",
    "##            ##         ###",
    "############################\n",]


#Fonction d'affichage de notre labyrinthe
def affiche_labyrinthe(labyrinthe) :
    for ligne in labyrinthe :
        print(ligne)


