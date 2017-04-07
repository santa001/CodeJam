import sys
import heapq
from collections import OrderedDict

def shortestPath(G, start, end):
   Q = [(0, start, "", [])] # heapqueue (cost, vertex, prev, [paths])
   visited = set()
   while Q:
      (cost, v, p, path) = heapq.heappop(Q)
      if v not in visited:
         visited.add(v)
         if p:
             c, s = G[p][v]
             path = path+[s]
         if end == v:
            return path
         for (v1, (cost1, s)) in G[v].iteritems():
            if v1 not in visited:
               heapq.heappush(Q, (cost + cost1, v1, v, path))
   else:
       return []


def shortestPaths(G, start, end):
    Q = [(0, start, "", [])] # heapqueue (cost, vertex, prev, [paths])
    visited = set()
    path_list = []
    min_cost = sys.maxint
    while Q:
        (cost, v, p, path) = heapq.heappop(Q)
        if cost > min_cost:
            continue
        visited.add(v)
        if p:
            c, s = G[p][v]
            path = path+[s]
        if end == v:
            if (min_cost == sys.maxint):
                min_cost = cost
            path_list += [(cost, path)]
            continue
        for (v1, (cost1, s)) in G[v].iteritems():
            if v1 not in visited:
                heapq.heappush(Q, (cost + cost1, v1, v, path))
    else:
        return path_list



def all_paths(G, start, end):
    Q = [(0, start, "", [])] # heapqueue (cost, vertex, prev, [paths])
    visited = set()
    path_list = []
    full_paths = []
    min_cost = sys.maxint
    while Q:
        #print "Q entries : {0}".format(Q)
        (cost, v, n, path) = heapq.heappop(Q) #Q.pop(0)
        if cost > min_cost:
            continue
        visited.add(v)
        if n:
            path = path + [n]
        if end == v:
            if (min_cost == sys.maxint):
                min_cost = cost
            min_cost = min(min_cost, cost)
            if path in full_paths: continue
            full_paths.append(path)
            #print "New path: {0}, full_paths: {1}".format(path, full_paths)
            path_list += [(cost, path)]
            #print "Path List: {0}".format(path_list)
            continue
        for key in G[v].keys():
           for (cost1, h) in G[v][key]:
              if key not in visited:
                 Q.append((cost + cost1, key, h, path))
                 heapq.heappush(Q, (cost + cost1, key, h, path))
    else:
        return path_list




if __name__ == "__main__":
    T = int(raw_input())

    for i in range(1, T+1):
        N, M = map (int, raw_input().split())
        paths = OrderedDict()
        #paths = {}
        bad_roads = []
        inputlist = []
        min_b = sys.maxint
        max_b = 0
        for k in range(0, M):
            u, v, c = raw_input().split()
            inputlist.append((u, v, c, k))
            t = int(u) if int(u) < int(v) else int(v)
            min_b = min(min_b, t)
            t = int(v) if int(v) > int(u) else int(u)
            max_b = max(max_b, t)
            c = int(c)
            entry = paths.get(u, None)
            if entry == None:
                paths[u] = {v: [(c, str(k))]}
            else:
               if None == paths[u].get(v, None):
                  paths[u].update({v: [(c, str(k))]})
               else:
                  paths[u][v].append((c, str(k)))
            entry = paths.get(v, None)
            if entry == None:
                paths[v] = {u: [(c, str(k))]}
            else:
               if None == paths[v].get(u, None):
                  paths[v].update({u: [(c, str(k))]})
               else:
                  paths[v][u].append((c, str(k)))
        
#        print paths
#        print "inputlist = {0}".format(inputlist)
        # ap = all_paths(paths, '1', '2')
        # print "All paths betweeen {0}-{1} = {2}".format('1', '2', ap)

        #print "Checking or 0-1 "
        #print "\n"
        #print "All paths (0-1): {0}".format(all_paths(paths, '0', '1'))
        


        good_roads = set()
        for (a, b, c, d) in inputlist:
           ap = all_paths(paths, a, b)
           for (c, p) in ap:
              good_roads.update(set(p))


        # good_roads = set()
        # for x in range(min_b, max_b):
        #    for y in range(x+1, max_b+1):
        #       ap = all_paths(paths, str(x), str(y))
        #       for (c, p) in ap:
        #          good_roads.update(set(p))
#              print "All paths {0}-{1} = {2}".format(x, y, ap)

#        print "All good roads {0}".format(good_roads)  

        bad_roads = []
        for x in range(min_b, max_b+1):
           if str(x) not in good_roads:
              bad_roads.append(str(x))
        
        

        print "Case #{0}:".format(i)
        for k in bad_roads:
           print k

        
        
