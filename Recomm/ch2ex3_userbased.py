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
      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree':\
 3.5},
     'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Return\
s':4.0}}



# User-based Filtering - PRECOMPUTE----------------------------------
# Returns dict of 
# key = item_name
# value = list
def calculateSimilarUsers(prefs, n=10):
    result = {}
    c=0
    for user in prefs:
        # Status update for large datasets!!
        c+=1
        if c%100==0: print "%d / %d" % (c, len(prefs))
        scores = topMatches(prefs, user, n=n, similarity=sim_pearson)
        result[user]=scores
    return result

def sim_pearson(prefs, p1, p2):
    si = []
    for p in prefs[p1]:
        if p in prefs[p2]:
            si.append(p)

    n = len(si)
    if n == 0: return 0
    
    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])
    sum1Sq = sum([pow(prefs[p1][item],2) for item in si])
    sum2Sq = sum([pow(prefs[p2][item],2) for item in si])
    pSum = sum([prefs[p1][item]*prefs[p1][item] for item in si])

    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, userMatch, user):
    totals = {}
    simSums = {}
    top5 = userMatch[user]
    top5.sort()
    top5.reverse()
    # Use only 5 top users
    for (simi, other) in top5[0:5]:
        # don't compare me to myself
        if other==user: continue
        sim=sim_pearson(prefs, user, other)

        # ignore scores of zero or lower
        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[user] or prefs[user][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings = [(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
            
        

    
