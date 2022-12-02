# Créé par Elève, le 05/09/2022 en Python 3.7

"""
Ce fichier contient UNE erreur: quelques caractères ont été ajoutés EN TROP à un
endroit où ils ne devraient pas être. En l'état, le code plante: comment trouver
où est le problème alors qu'on ne connaît pas le code lui-même?
"""


def moyenne(data):
    """ Moyenne des valeurs d'une liste non vide """
    return sum(data) / len(data)


def funcB(data):
    """ Ecart-type """
    X = moyenne(data)
    y = sum( (x-X)**2 for x in data )
    return ( y / (len(data)-1) )**0.5


def funcC(data):
    """ Incertitude type """
    v = funcB(data)
    return v / len(data)**0.5




def print_data(nom,data):
    """ @nom: nom de la série de données
        @data: données numériques à traiter (liste ou tuple)
        @return: None
    """
# A propos de la fonction """...{}...""".format(x):
# Dans la chaîne de caractères (=le truc avec les "..."), les accollades sont
# remplacées par ce qui est dans les parenthèses de format(...).
# """abc: {} fgh: {}""".format(22,44) est donc équivalent à """abc: 22 fgh: 44"""

    print("""
{} :
    ... : {}
    ... : {}
    ... : {}
""".format(nom, moyenne(data), funcB(data), funcC(data) ))



#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------



def study(pas_bins, series):
    """ study(pas_bins, serie1, serie2, serie3, ...)

        @pas_bins:  largeur d'une bande de l'histogramme (v. trace_histo)
        @*series:   nombre arbitraire de séries de données, où une série de
                    données est une tuple: ('nom_série', [donnée1, donnée2, ...])
        @return:    None
    """
    # affiche les informations statistiques
    for nom,data in series:
        print_data(nom,data)

    # affiche tous les histogrammes possibles (toutes les combinaisons
    # des séries de données en entrées)
    for serie in series:
        trace_histo(pas_bins, serie)
    trace_histo(pas_bins, *series)


def trace_histo(pas_bins, *series):
    """ trace_histo(pas_bins, serie1, serie2, serie3, ...)

        @pas_bins:  largeur d'une bande de l'histogramme
        @*series:   nombre arbitraire de séries de données, "serie", où:
                      serie = ('nom_série', [donnée1, donnée2, ...])
        @return:    None
    """
    import matplotlib.pyplot as plt

    mi = min(min(data) for _,data in series)    # minimum global
    ma = max(max(data) for _,data in series)    # maximum global

    # Création des intervalles à partir du pas d'échantillonnage:
    bins_rng = [mi+n*pas_bins for n in range(int((ma-mi+pas_bins)/pas_bins))]

    if len(bins_rng)<2: raise Exception("""La valeur du pas utilisée n'est pas bonne (0 ou 1 "bin"). Augmenter la valeur de l'argument 'pas_bin'""")

    labels,datas = zip(*series)
    plt.hist(datas, range=(mi,ma+pas_bins), bins=bins_rng)
    plt.ylabel('Fréquence')
    plt.legend(labels)
    plt.show()




#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------


def unrelated():
    a = 1
    for i in range(2,10,3):
        a *= i
unrelated()


V1   = [18.1, 18.0, 17.4, 17.3, 17.4, 17.4]
V2   = [18.1, 17.6, 17.8, 17.9, 17.5, 18.4, 18.3]
Vall = (V1+V2) * 0
pas  = .2
study(pas, [('V1', V1), ('Véq', Vall)])