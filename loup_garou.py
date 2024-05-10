import random

joueurs = {"Kevin":"Villageois",
           "Jonah": "Villageois",
           "Thomas": "Villageois",
           "Kylian": "Villageois",
           "Lucas": "Villageois",
           "Melvin": "Villageois",
           "Paul": "Villageois",
           "Nathan": "Villageois"}

nombre_de_loup = 2
loup = []

def choix_loup():
    global nombre_de_loup, joueurs, i
    choix = random.sample(list(joueurs.keys()), nombre_de_loup)
    for i in choix:
        joueurs[i] = "Loup"
        loup.append(i)
    return

def tue_joueur_par_loup():
    while True:
        choix = random.sample(list(joueurs.keys()), 1)
        joueur_mort = choix[0]
        if joueurs[joueur_mort] != "Loup":
            print(f"Les loups ont tué {joueur_mort} cette nuit.")
            del joueurs[joueur_mort]
            break

def tue_joueur_par_vote(elimin):
    if elimin in list(joueurs.keys()):
        print(f"Vous avez éliminé {elimin} qui était {joueurs[elimin]}.")
        del joueurs[elimin]
        return
    else:
        print("Le joueurs n'existe pas.")
        elimin = input("Qui voulez-vous éliminer? ")
        tue_joueur_par_vote(elimin)

def gagnant():
    global loup
    if "Loup" not in list(joueurs.values()):
        print("Le village a gagné.")
        return False
    if "Villageois" not in list(joueurs.values()):
        print("Les loups ont gagné. Ils étaient: ", " ".join(loup))
        return False
    else:
        return True

def joueurs_restant():
    restant = list(joueurs.keys())
    restant = " ".join(restant)
    print(f"Les joueurs restant sont {restant}.")

def main():
    jour = 1
    choix_loup()
    x = list(joueurs.keys())
    print("Les joueurs sont: ", end="", flush=True)
    for i in x:
        print(f"{i} ", end="", flush=True)
    print()
    while True:
        if not gagnant():
            break
        print(f"Jour {jour}")
        if jour != 1:
            tue_joueur_par_loup()
            joueurs_restant()
        jour += 1
        elimin = input("Qui voulez-vous éliminer? ")
        tue_joueur_par_vote(elimin)
        if not gagnant():
            break
        print("La nuit tombe.")

main()