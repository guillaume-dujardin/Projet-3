class Map :
    #Labyrinthe niveau 1 (plan du labyrinthe)
    def __init__(self) :
        self.affichage = affichage



labyrinthe = [
"###############",
"#######    ####",
"#x      ##    #",
"#### ####### ##",
"#### ###      #",
"#     ### ## ##",
"##### ### ## ##",
"##### ### ##  #",
"##    ### ## ##",
"## ###### ## ##",
"## ###### #####",
"##            #",
"##### #########",
"#####         #",
"###########O###\n",]

#Fonction d'affichage de notre labyrinthe
def affiche_labyrinthe(labyrinthe) :
    for ligne in labyrinthe :
        print(ligne)


