##########################################
##-----------Anurag Banerjee------------##
##---------------CS 7030----------------##
##-----------  Assignment 3  -----------##
##########################################


import indexer
import infixToPostfix
import operations as op
import string
import re


def getDocIndex():
    '''
    In this dummy function we will simply call upon the functions we built in the indexer.py file
    :return: the inverted term-document index
    '''
    docTermDict = indexer.buildDocTerm()
    return indexer.buildInvIndx(docTermDict)
    # indexer.displayInvIndx(invIndx)


def getQuery():
    '''
    This functions asks user to input a query and cleans/lemmatizes it.
    :return:
    '''
    queryString = raw_input("Enter your query (using operators 'AND' 'OR' 'NOT' '()'): ")
    punctTbl = re.sub(ur'[()]', '', string.punctuation)
    queryString = queryString.translate(None, punctTbl)     # removing all punctuation except parenthesis
    temp = ""
    for char in queryString:
        if char.isalpha() or char.isspace():
            temp += char
        else:
            temp += ' '+char+' '
    queryString = temp.rstrip()
    queryString = re.sub(ur' +', ' ', queryString.lower())    # remove extra spaces
    qList = indexer.lemmatizer(queryString)    # now performing lemmatization
    #queryString = " ".join(qList)

    return qList    # query in List form


def processQ(query, postingList):
    '''
    This function processes the boolean query and returns the result
    :param query: Postfix form of query dict, with posting list
    :param invIndx:
    :return: a list of document IDs
    '''
    # docCount = indexer.docCount
    tempList = []
    currPostLst = [0, {}]
    i = 0
    while len(query) > 1:
        if query[i] in ('and', 'or'):
            leftOprnd = {query[i-2]: postingList[i-2]}
            rytOprnd = {query[i-1]: postingList[i-1]}
            (query[i-2:i+1], postingList[i-2:i+1]) = op.operate(leftOprnd, query[i], rytOprnd, i-2)
            i -= 2
        elif query[i] == 'not':
            leftOprnd = {}
            rytOprnd = {query[i-1]: postingList[i-1]}
            (query[i-1:i+1], postingList[i-1:i+1]) = op.operate(leftOprnd, query[i], rytOprnd, i-1)
            i -= 1
        else:
            i += 1
    for docIds in (postingList[0][1]).keys():
        tempList.append(docIds)

    return tempList


def boolsearch(invIndx):
    '''
    This function gives the result for a query according to the boolean model
    :return:
    '''
    postingList = []
    query = getQuery()  # query in a list form
    conversionObj = infixToPostfix.Conversion(len(query))
    query = conversionObj.infixToPostfix(query)     # the query in postfix form
    for i, term in enumerate(query):
        if term not in ('not', 'and', 'or'):
            postingList.append(invIndx[term] if term in invIndx else [0, {}])
        else:
            postingList.append([0, {}])
    docList = processQ(query, postingList)
    print("The result of your search:")
    result = docList if len(docList) != 0 else "No documents matching your criteria found!"
    print result


def main():
    '''
    Here we write all the starter code
    :return:
    '''
    invIndx = getDocIndex()
    ch = -99
    while ch != '2':
        ch = raw_input("\nEnter 1 to fire query\n\t\t2 to exit:")
        if ch == '1':
            boolsearch(invIndx)
        elif ch not in ('1', '2'):
            print "\nWrong input! Try again."
            ch = -99


def test():
    '''
    Here we write code to test modules
    :return:
    '''
    # getDocIndex()
    # getQuery()
    # boolsearch()


if __name__ == '__main__':
    # test()
    main()

