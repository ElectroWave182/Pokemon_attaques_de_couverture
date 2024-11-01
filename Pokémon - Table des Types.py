from sys import stdin,stdout
input,print = stdin.readline,stdout.write
def typesAdd(stock,dest,target,nb):
    dest.append(stock.index(target))
    stock[dest[-1]] = nb
    return [stock,dest]
def faibl(entree,sortie,counter,nbt):
    types = ["acier","combat","dragon","eau","electrik","fee","feu","glace","insecte","normal","plante","poison","psy","roche","sol","spectre","tenebres","vol"]
    tabl = [[2,5,5,2,2,9,2,9,5,5,5,5,5,9,5,5,5,5],[9,5,5,5,5,2,5,9,2,9,5,2,2,9,5,0,9,2],[2,5,9,5,5,0,5,5,5,5,5,5,5,5,5,5,5,5],[5,5,2,2,5,5,9,5,5,5,2,5,5,9,9,5,5,5],[5,5,2,9,2,5,5,5,5,5,2,5,5,5,0,5,5,9],[2,9,9,5,5,5,2,5,5,5,5,2,5,5,5,5,9,5],[9,5,2,2,5,5,2,9,9,5,9,5,5,2,5,5,5,5],[2,5,9,2,5,5,2,2,5,5,9,5,5,5,9,5,5,9],[2,2,5,5,5,2,2,5,5,5,9,2,9,5,5,2,9,2],[2,5,5,5,5,5,5,5,5,5,5,5,5,2,5,0,5,5],[2,5,2,9,5,5,2,5,2,5,2,2,5,9,9,5,5,2],[0,5,5,5,5,9,5,5,5,5,9,2,5,2,2,2,5,5],[2,9,5,5,5,5,5,5,5,5,5,9,2,5,5,5,0,5],[2,2,5,5,5,5,9,9,9,5,5,5,5,5,2,5,5,9],[9,5,5,5,9,5,9,5,2,5,2,9,5,9,5,5,5,0],[5,5,5,5,5,5,5,5,5,0,5,5,9,5,5,9,2,5],[5,2,5,5,5,2,5,5,5,5,5,5,9,5,5,9,2,5],[2,9,5,5,2,5,5,5,9,5,9,5,5,2,5,5,5,5]]
    while entree:
        print("Entrez le(s) type(s) de votre pokémon, sans accent, séparés d'un espace s'il y en a deux...\n")
        typeP = list(input().split())
        type1,type2 = typeP[0],typeP[-1]
        if type1 in types and type2 in types:
            num1,num2 = types.index(type1),types.index(type2)
            entree = False
        if type1 == type2: print("► " + type1 + "\n\n")
        else: print("► " + type1 + " et " + type2 + ".\n\n")
    coef = [tabl[num1][typeDef] + tabl[num2][typeDef] for typeDef in nbt]
    weak = min(coef)
    typesW = [coef.index(weak)]
    coef[typesW[0]] = 19
    for nbWeak in nbt:
        if weak == min(coef):
            coef,typesW = typesAdd(coef,typesW,weak,19)
        elif nbWeak == 0:
            weak = min(coef)
            coef,typesW = typesAdd(coef,typesW,weak,19)
            counter = True
        else: break
    coef = [sum([tabl[typeOff][typeW]*18 if counter else tabl[typeOff][typeW] for typeW in typesW]) for typeOff in nbt]
    strong = max(coef)
    typesS = [coef.index(strong)]
    coef[typesS[0]] = 0
    for nbStrong in nbt:
        if strong == max(coef):
            coef,typesS = typesAdd(coef,typesS,strong,0)
        elif nbStrong == 0:
            strong = max(coef)
            coef,typesS = typesAdd(coef,typesS,strong,0)
        else: break
    for num in typesS:
        if num == typesS[-1]: sortie += "ou " + types[num] + "."
        else: sortie += types[num] + ", "
    return sortie
print(faibl(True,"Afin d'être super efficace, votre pokémon doit apprendre une attaque de type...\n► ",False,range(18)))