def place_in_proper_list(listA, listB, f, s):
    if (f in listA and s in listB) or  (f in listB and s in listA):
        return (1)
            
    if (f in listA and s in listA) or (f in listB and s in listB):
        return (0)

    if f not in listA and f not in listB and s not in listA and s not in listB:
        return (2)
        
    if f in listA and s not in listB:
        listB.append(s)
    elif f in listB and s not in listA:
        listA.append(s)
    elif s in listA and f not in listB:
        listB.append(f)
    elif s in listB and f not in listA:
        listA.append(f)
    
    return (1)


if __name__ == "__main__":
    T = int(raw_input())

    for i in range(0, T):
	M = int(raw_input())
        listA = []
        listB = []
        pending_items = []
        not_possible = False
        
        f, s = raw_input().split()
        listA.append(f)
        listB.append(s)

        for j in range(1, M):
	    f, s = raw_input().split()
            if not_possible:
                continue

            val = place_in_proper_list(listA, listB, f, s)
            if val == 0:
                not_possible = True
                pending_items = []
            if val == 2:
                pending_items.append((f, s))
        
        while pending_items:
            (f, s) = pending_items.pop(0)
            
            val = place_in_proper_list(listA, listB, f, s)
            if val == 0:
                not_possible = True
                break
            if val == 2:
                pending_items.append((f, s))

        print "Case #%d: %s" %(i+1, "No" if not_possible else "Yes")
        continue
