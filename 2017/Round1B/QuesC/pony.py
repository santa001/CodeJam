import sys

def update_min(N, G):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j: continue
                if G[i][j] > (G[i][k] + G[k][j]):
                    G[i][j] = G[i][k] + G[k][j]

def new_time_graph(N, G, D, S):
    G_t = [[sys.maxint for x in range(N+1)] for y in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if G[i][j] <= D[i]:
                G_t[i][j] = (float(G[i][j]))/S[i]
    return G_t

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        N, Q = map(int, raw_input().strip().split())
        G = [[sys.maxint for x in range(N+1)] for y in range(N+1)]
        D = [0 for x in range(N+1)]
        S = [0 for x in range(N+1)]
        I = []
        for j in range(1, N+1):
            D[j], S[j]  = map(int, raw_input().strip().split())
        for j in range(1, N+1):
            G[j][1:] = map(int, raw_input().strip().replace("-1", str(sys.maxint)).split())
        for j in range(Q):
            u, v = map(int, raw_input().strip().split())
            I.append((u,v))
        # Update min distance in G    
        update_min(N, G)
        # Create new time based graph
        G_t = new_time_graph(N, G, D, S)
        # Update min time in G_t
        update_min(N, G_t)
        print "Case #{0}: ".format(i),
        for (u, v) in I:
            print "{0} ".format(round(G_t[u][v], 6)),
        print ""
