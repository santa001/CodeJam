def solve(classes, N):
    visited = [0 for x in range(N+2)]
    for i in range(1, N+2):
        if visited[i]:
            continue
        queue = []
        seen = [0 for x in range(N+2)]
        seen[i] = 1
        queue.append(i)
        while queue:
            k = queue.pop()
            for pos, val in enumerate(classes[k]):
                if pos > N+1:
                    break
                if val:
                    if seen[pos]:
                        return "Yes"
                    queue.append(pos)
                    seen[pos] = 1
                    visited[pos] = 1
    return "No"


if __name__ == "__main__":
    T = int(raw_input())

    for i in xrange(1, T+1):
        N = int(raw_input())
        classes = [[0 for x in range(N+2)] for y in range(N+2)]
        for j in xrange(1, N+1):
            inp = map(int, raw_input().strip().split())
            if not inp[0]:
                continue
            for k in inp[1:]:
                classes[j][k] = 1;

        possible = solve(classes, N)
        print "Case #{0}: {1}".format(i, possible)

