def getDepList(exp):
    dList = []

    va, rem = exp.split('=')
    fn, rem = rem.split('(')

    rem = rem.split(')')
    dep = []
    dList = [va]
    if len(rem[0]) > 0:
        dep = rem[0].split(',')
        dList.extend(dep)
    return dList

def resolvable(exp, rList):
    dList = getDepList(exp)
    #print "Exp: {0}, dList: {1}, rList: {2}".format(exp, dList, rList)
    if len(dList) == 1:
        rList.append(dList[0])
        return True
        
    dListLen = len(dList)
    count = 1
    for j in range(1, dListLen):
        if dList[j] in rList:
            count += 1
            
        if len(dList) == count:
            rList.append(dList[0])
            return True
    return False


def solve(eList):
    rList = []
    dGraph = {}

    eListLen1 = len(eList)
    eListLen2 = 0
    #print "Starting: eList: {0}".format(eList)
    

    while eListLen1 != eListLen2:
        eList[:] = [exp for exp in eList if not resolvable(exp, rList)]
        #print "eList: {0}".format(eList)
        eListLen2 = eListLen1
        eListLen1 = len(eList)

    return (len(eList) == 0)

if __name__ == "__main__":
    T = int(raw_input())

    for i in range(1, T+1):
        ExpList = []
        N = int(raw_input())
        for j in range(N):
            ExpList.append(raw_input())

        #print "\n Set {0} \n".format(i)
        #for k in ExpList:
        #    print k


        possible = "Good" if solve(ExpList) == 1 else "BAD"
        print "Case #{0}: {1}".format(i, possible)
