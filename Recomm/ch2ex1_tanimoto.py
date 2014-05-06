from math import sqrt


# Get the list of shared_items--------------------------
def findsi(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    return si

# SIMILA - TANIMOTO-------------------------------------
def sim_tanimoto(prefs, p1, p2):
    inter = []
    union= []

    # Get Intersection Set
    for item in prefs[p1]:
        if item in prefs[p2]:
            inter.append(item)
    # Get Union Set
    for item in prefs[p1]:
        union.append(item)
    for item in prefs[p2]:
        if item not in prefs[p1]:
            union.append(item)
    sum_inter = sum([prefs[p1][item] for item in inter])
    sum_union1 = sum([prefs[p1][item] for item in union if item in prefs[p1]])
    sum_union2 = sum([prefs[p2][item] for item in union if item not in prefs[p1]])

    return float(sum_inter)/(sum_union1+sum_union2)
