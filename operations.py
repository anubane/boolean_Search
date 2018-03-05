##########################################
##-----------Anurag Banerjee------------##
##---------------CS 7030----------------##
##-----------  Assignment 3  -----------##
##########################################

import indexer


def operate(leftOprnd, oprtr, rytOprnd, termNum):
    newPostingList = []
    tempDict = {}

    if oprtr == 'and':
        leftsz = leftOprnd.values()[0][0]
        rytsz = rytOprnd.values()[0][0]
        if leftsz * rytsz != 0:
            (lenlarge, large) = (leftsz, leftOprnd) if leftsz > rytsz else (rytsz, rytOprnd)
            (lensmall, small) = (leftsz, leftOprnd) if leftsz < rytsz else (rytsz, rytOprnd)
            for docid in (small.values()[0][1]).keys():
                if docid in small.values()[0][1]:
                    tempDict[docid] = 1

    elif oprtr == 'or':
        if leftOprnd.values()[0][0] != 0:
            for docid in (leftOprnd.values()[0][1]).keys():
                tempDict[docid] = 1
        if rytOprnd.values()[0][0] != 0:
            for docid in (rytOprnd.values()[0][1]).keys():
                tempDict[docid] = 1

    elif oprtr == 'not':
        for docid in indexer.getAllDocIds():
            if docid not in (rytOprnd.values()[0][1]).keys():
                tempDict[docid] = 1

    newPostingList.append(len(tempDict))
    newPostingList.append(tempDict)

    return (['term'+str(termNum)], [newPostingList])

# EOF
