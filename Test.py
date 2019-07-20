import random
 
lol = [" 1 2 3 4 5"]
pos_ob = []

def objet() :
    for line in lol :
        for character in line :
            if character == " " :
                pos_ob.append(list(character))
objet()
print(pos_ob)

i = 0

while i != 3 :
    i += 1
    pos = random.sample(pos_ob,2)
    print(pos)