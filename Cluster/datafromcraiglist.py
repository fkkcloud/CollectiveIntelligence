from sys import exit
import re
import urllib2
import pprint
import operator
from bs4 import BeautifulSoup as bs

def getDataFromUrl( url ):
    loadedUrl = urllib2.urlopen( url )
    dataBuf = loadedUrl.read()
    soupObj = bs( dataBuf )
    return soupObj

def get2LettersFromEntry( entry ):
    entry = re.compile('[^a-z^A-Z]+').sub(' ',entry)
    listSingleWords = re.compile(' ').split( entry.strip().lower() )
    for d in ['for','a','of','get','the','with',\
                  'per','now','hiring','included',\
                  'wanted','and','you','hr','hrs','rate','to','up']:
        try:
            listSingleWords.remove(d)
        except:
            continue
    for l in listSingleWords:
        if len(l) == 1:
            listSingleWords.remove(l)

    listTwoWords = []
    for i in range(len(listSingleWords)-1):
        listTwoWords.append( listSingleWords[i]+' '+listSingleWords[i+1] )
    return listTwoWords

def getEntriesFromSoupObj( soupObj ):
    links = soupObj( 'a' )
    listOfWordList = []
    sentinel = 0
    for i in range(len(links)):
        # print "Looking into link #%d" % i
        try:
            entry = links[i].contents[0]

            if entry.strip() == 'next >':
                sentinel += 1
                continue

            if sentinel !=  1:
                continue

            if (i%2) == 0:
                listOfWordList.append( get2LettersFromEntry( entry ) )
                # print "link #%d was sucessfull."

        except:
            # print "link #%d was not sucessful."
            continue
    return listOfWordList

def getJobsPerCity( cities ):    
    jobsPerCities = []
    jobsCountPerCities = []
    for i in range(len(cities)):
        tmpLs = []
        tmpDic = {}
        jobsPerCities.append(tmpLs)
        jobsCountPerCities.append(tmpDic)
    
    jobsList = []
    for i in range(len(cities)):
        url = "http://"+cities[i]+".craigslist.org/search/jjj?query=''"
        soupObj = getDataFromUrl( url )
        jobsList.append(getEntriesFromSoupObj( soupObj ))
        tmp = jobsList[i]
        for j in tmp:
            for k in j:
                jobsPerCities[i].append(k)
        for word in jobsPerCities[i]:
            jobsCountPerCities[i].setdefault(word, 0)
            jobsCountPerCities[i][word] += 1

    return jobsCountPerCities

def sortDic( dic ):
    max = i

def main():
    cities = ['lasvegas', 'losangeles', 'sanfranscisco', 'irvine']
    
    result = getJobsPerCity( cities )
    data = []
    for k in range(len(cities)):
        print '\n\n\n %s' % cities[k]
        sortedDic = sorted(result[k].iteritems(), key = operator.itemgetter(1), reverse = True)
        data.append(sortedDic[0:10])
        for item in data[k]:
            print item


        # pprint.pprint(result[k])
    
if __name__ == "__main__":
    main()
