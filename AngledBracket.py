'''write a function that adds angle brackets to the beginning 
and end to make all angle brackets match and return it. 
The angle brackets "match" if for every '''


def solution(angles):
    openCount = 0
    addLeadOpentag = 0
    for i in angles:
        if i == '>':
            if openCount == 0:
                addLeadOpentag = addLeadOpentag+1
            else:
                openCount = openCount-1
        else:
            openCount = openCount+1
            
    return '<'[:1]*addLeadOpentag + angles + '>'[:1]*openCount


print(solution("<><><"))