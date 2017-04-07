def find_longest1(F_List, F_O_F, index, temp, count):
    max_count = count
    bf = F_List[index]
    if bf not in temp:
        val = find_longest1(F_List, F_O_F, bf, temp + [bf], count+1)
        if (val == -1):
            return -1

        if (max_count < val):
            max_count = val
            #print "Max_Count : %d" %(val)
            #print (temp + [bf])
        return max_count
    else:
            # if (max_count < count):
            #     return count
            # else:
            #     return max_count

        if (bf == temp[-2]):
            for f in F_O_F[index]:
                if f in temp:
                    continue
                #print "Calling with optional friend: current len %d" %(count)
                val = find_longest1(F_List, F_O_F, f, temp + [f], count+1)
                if (val == -1):
                    continue
                if (max_count < val):
                    max_count = val
                    #print "Max_Count : %d" %(val)
                    #print (temp + [f]) 
            else:
                for k in F_List:
                    if k in temp:
                        continue
                    val = find_longest1(F_List, F_O_F, k, temp + [k], count+1)
                    if (val == -1):
                        continue
                    if (max_count < val):
                        max_count = val
        else:
            if (bf == temp[0]):
                return count
            else:    
                return -1
    return max_count

def find_longest(F_List, F_O_F, N, index, temp, count):
    max_count = count
    
    # if (len(F_O_F[index]) == 0):
    #     return -1

    for f in F_O_F[index]:
        # temp_count = count
        # temp_temp = temp[:]

        if (f in temp):
             continue
        # if len(F_O_F[f]) == 0:
        #     if temp_temp[0] == F_List[f]:
        #         temp_count = temp_count + 1
        #         if (max_count < temp_count):
        #             max_count = temp_count
        #             possible = 1
        #             continue
        #     else:
        #         continue
        val = find_longest(F_List, F_O_F, N, f, (temp + [f]), count+1)
        if (max_count < val):
            max_count = val
            #print "Longest seq: %d " %(max_count) 
            #print (temp+[f])
    return max_count    

def solve(F_List, F_O_F, N):
    max_count = 0
    for i in range(1, N+1):
        val = find_longest1(F_List, F_O_F, i, [i], 1)
        if (max_count < val):
            max_count = val

    return max_count

if __name__ == "__main__":
    T = int(raw_input())
    i = 0

    while i < T:
        N       = int(raw_input())
        String  = raw_input().strip().split()

        temp = map(int, String)
        F_List = [0] + temp
        F_O_F  = [0] * (N+1)

        #print F_List
        for j in range(1, N+1):
            temp = [] #[F_List[j]]
            for k in range(1, N+1):
                if j == k:
                    continue
                if F_List[k] == j:
                    temp = temp + [k]
            F_O_F[j] = temp        
           
        #print F_O_F
        count = solve(F_List, F_O_F, N)
 	#print "Case #%d: %d, %s" %((i+1), count, str(F_List))
        print "Case #%d: %d" %((i+1), count)
        i += 1
