from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
      'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
      'The Night Listener': 3.0},
     'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
      'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 3.5},
     'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
      'Superman Returns': 3.5, 'The Night Listener': 4.0},
     'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
      'The Night Listener': 4.5, 'Superman Returns': 4.0,
      'You, Me and Dupree': 2.5},
     'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 2.0},
     'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
     'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}



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

# SIMILA - EUCLIDEAN------------------------------------
def sim_distance(prefs, p1, p2):
    si = findsi(prefs, p1, p2)
    if len(si)==0: return 0
    sum_of_squares=sum([pow(prefs[p1][item]-prefs[p2][item],2) for item in prefs[p1] if item in prefs[p2]])
    
    return 1/(1+sqrt(sum_of_squares))

# SIMILA - PEARSON----------------------------------------
def sim_pearson(prefs, p1, p2):
    si = findsi(prefs, p1, p2)
    n = len(si)
    if n == 0: return 0
    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])
    sum1Sq=sum([pow(prefs[p1][item],2) for item in si])
    sum2Sq=sum([pow(prefs[p2][item],2) for item in si])
    pSum=sum([prefs[p1][item]*prefs[p2][item] for item in si])

    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r

# Returns list of tuples (similarity , item_name) based on person------
# Highest similarity
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other!=person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

# Return list of tuples (sim.x, item_name) ----------------------------
# Highest similarity x other's rating (r.x)
def getRecommendations(pref, person, similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other==person: continue
        sim=similarity(prefs,person,other)
        
        if sim<=0: continue # if it's Pearson, it would return negative
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim

    rankings=[(total/simSums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

# Transform x,y -> y,x---------------------------------------------
def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[person][item]
    return result

# Item-based Filtering -PRECOMPUTE-------------------------------
# Returns Dictionary of list as value and item_name as key
def calculateSimilarItems(prefs, n=10):
    result = {}
    itemPrefs=transformPrefs(prefs) # x,y -> y,x
    c=0
    for item in itemPrefs:
        c+=1
        if c%100==0: print "%d / %d" % (c, len(itemPrefs))
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item]=scores
    return result

# Item-based Filtering -RECOMMENDATION-------------------------
# Returns list of tuples (score , item_name)
def getRecommendedItems(prefs, itemMatch, user):
    userRatings=prefs[user]
    scores={}
    totalSim={}
    testr={}

    for (item, rating) in userRatings.items():
        for (similarity, item2) in itemMatch[item]:

            if item2 in userRatings: continue #ignore if user already rated
            
            scores.setdefault(item2, 0)
            scores[item2]+=similarity*rating
            print item2, scores[item2], similarity
            
            testr[item2] = rating

            totalSim.setdefault(item2, 0)
            totalSim[item2]+=similarity
            print item2, totalSim[item2], similarity

    # Returns list of tuples (score, item_name) that user di dnot rated!
    # Get average
    rankings=[(score/totalSim[item], item) for item,score in scores.items()]    
    rankings.sort()
    rankings.reverse()
    return rankings
