def combine(x, y):
    return x + y if x < y else y + x

def solve(N, R, P, S):
    p = "P"
    r = "R"
    s = "S"
    for i in range(0, N):
        p1 = combine(p, r)
        r1 = combine(r, s)
        s1 = combine(p, s)

        p = p1
        r = r1
        s = s1

    if P == p.count('P') and R == p.count('R') and S == p.count('S'):
    	return p
    if P == r.count('P') and R == r.count('R') and S == r.count('S'):
    	return r
    if P == s.count('P') and R == s.count('R') and S == s.count('S'):
    	return s

    return "IMPOSSIBLE"


if __name__ == "__main__":
    T = int(raw_input())

    for i in range(1, T+1):
        N, R, P, S = map(int, raw_input().split())
        solution = solve(N, R, P, S)
        print "Case #{0}: {1}".format(i, solution)
