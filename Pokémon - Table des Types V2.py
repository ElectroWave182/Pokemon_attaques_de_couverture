from sys import stdin, stdout
input, print = stdin.readline, stdout.write

def main ():


    # Données

    noms = ["acier", "combat", "dragon", "eau", "electrik", "fee", "feu", "glace", "insecte", "normal", "plante", "poison", "psy", "roche", "sol", "spectre", "tenebres", "vol"]
    table = list ()
    table.append ([1,4,4,1,1,13,1,13,4,4,4,4,4,13,4,4,4,4])
    table.append ([13,4,4,4,4,1,4,13,1,13,4,1,1,13,4,0,13,1])
    table.append ([1,4,13,4,4,0,4,4,4,4,4,4,4,4,4,4,4,4])
    table.append ([4,4,1,1,4,4,13,4,4,4,1,4,4,13,13,4,4,4])
    table.append ([4,4,1,13,1,4,4,4,4,4,1,4,4,4,0,4,4,13])
    table.append ([1,13,13,4,4,4,1,4,4,4,4,1,4,4,4,4,13,4])
    table.append ([13,4,1,1,4,4,1,13,13,4,13,4,4,1,4,4,4,4])
    table.append ([1,4,13,1,4,4,1,1,4,4,13,4,4,4,13,4,4,13])
    table.append ([1,1,4,4,4,1,1,4,4,4,13,1,13,4,4,1,13,1])
    table.append ([1,4,4,4,4,4,4,4,4,4,4,4,4,1,4,0,4,4])
    table.append ([1,4,1,13,4,4,1,4,1,4,1,1,4,13,13,4,4,1])
    table.append ([0,4,4,4,4,13,4,4,4,4,13,1,4,1,1,1,4,4])
    table.append ([1,13,4,4,4,4,4,4,4,4,4,13,1,4,4,4,0,4])
    table.append ([1,1,4,4,4,4,13,13,13,4,4,4,4,4,1,4,4,13])
    table.append ([13,4,4,4,13,4,13,4,1,4,1,13,4,13,4,4,4,0])
    table.append ([4,4,4,4,4,4,4,4,4,0,4,4,13,4,4,13,1,4])
    table.append ([4,1,4,4,4,1,4,4,4,4,4,4,13,4,4,13,1,4])
    table.append ([1,13,4,4,1,4,4,4,13,4,13,4,4,1,4,4,4,4])


    # Prise d'input

    while True:

        print ("Entrez le(s) type(s) de votre pokémon, sans accent, séparés d'un espace s'il y en a deux...\n")
        entree = input ().rstrip ('\n').split ()
        
        match (len (entree)):
        
            case 1:
                nom_a = entree[0]
                nom_b = nom_a
                print ("► " + nom_a)
            
            case 2:
                nom_a, nom_b = entree
                print ("► " + nom_a + " et " + nom_b)
                
            case other:
                nom_a = ""
                nom_b = ""
            
        print ("\n\n")

        if nom_a in noms and nom_b in noms:
            type_a = noms.index (nom_a)
            type_b = noms.index (nom_b)
            break


    # Coefficients de résistance basiques

    def somme_croisee (liste_a, liste_b):

        taille = len (liste_a)
        return [liste_a[ind] + liste_b[ind] for ind in range (taille)]

    atk_a = table[type_a]
    atk_b = table[type_b]

    atk_base = somme_croisee (atk_a[:], atk_b[:])


    # Coefficients de résistance avec un type complémentaire

    """
    Calcul des qualités offensives
    (avec les quarentaines de poids fort là où le type défensif résiste le mieux)
    """

    def mise_entier (atk_liste):

        # Séparation en portions (0, 1, 2, 3 pour pas/peu/moyen/super efficace)
        portions = []
        for atk in atk_liste:

            if atk == 0:
                rang = 0
            elif 1 <= atk <= 3:
                rang = 1
            elif 4 <= atk <= 12:
                rang = 2
            elif 13 <= atk <= 39:
                rang = 3

            portions.append (rang)

        moy = 40 ** 18 * sum (portions)

        # Prise en compte des résistances en priorité pour préciser les cas de rang égaux
        atk_liste.sort (reverse = True)

        coef_atk = moy
        poids = 1
        for atk in atk_liste:
            coef_atk += atk * poids
            poids *= 40

        return coef_atk

    # Fonction de tri de tuples sur leur premier élément
    def take_first (un_tuple):
        return un_tuple[0]

    # Test sur chaque type complémentaire possible
    maxi = 0
    possibilites = []
    for type_c in range (18):

        atk_c = table[type_c]
        atk_fin = somme_croisee (atk_base, atk_c)
        coef_atk = mise_entier (atk_fin[:])


        # Stockage pour donner un éventail plus large d'options au joueur

        possibilites.append ((coef_atk, type_c))
        possibilites.sort (reverse = True, key = take_first)



    # Affichage du résultat

    print ("Voici les types d'attaque de support qu'il peut apprendre (du meilleur au pire)...\n")

    for couple in possibilites:
        type = couple[1]
        nom = noms[type]
        print ("- " + nom + "\n")


main ()
