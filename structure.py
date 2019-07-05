#Message d'introduction au jeu

message_debut = "Vous incarner Mcgiver dans un labyrinthe ! Aider le à sortir indemne"
message_debut_modifier = message_debut.center(120,"*")
print(message_debut_modifier)


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

print("Vous êtes X et devez rejoindre la sortie ! Bonne chance...\n")

#Fonction d'affichage de notre labyrinthe
def affiche_labyrinthe(labyrinthe) :
    for ligne in labyrinthe :
        print(ligne)


#Definir (x) comme étant notre personnage

affiche_labyrinthe(labyrinthe) #afficher le labyrinthe
