from pydelicious import *
import pprint as p

def initTagData():
    pols = {}
    tags = ['anomynous', 'interactive', 'evangelion', 'portal', 'apple', 'google', 'game', 'software','engineering', 'MIT', 'Stanford', 'ai', 'programmer', 'coder', 'code', 'c++']

    for tag in tags:
        pols[tag] = get_popular(tag)
    return pols

def tagSim(data_dict):
    prog_tags = []
    for item in get_popular('programming'):
        prog_tags.append(item['tags'])
    
    tag_dict = {}
    for tag_key in data_dict:
        tags = []
        for postList in data_dict[tag_key]:
            tags.append(postList['tags'])
        tag_dict[tag_key] = tags

    tag_score = []
    for tag_key in tag_dict:
        score = 0
        for tag1 in tag_dict[tag_key]:
            for tag2 in prog_tags:
                if tag1 == tag2:
                    score += 1
        tag_score.append((tag_key, score))
    
    tag_score.sort()
    tag_score.reverse()
    return tag_score


    
