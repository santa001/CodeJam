if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        time_taken = []
        D, N = map(int, raw_input().strip().split())
        for j in range(N):
            K, S = map(int, raw_input().strip().split())
            t = (float(D - K))/S
            time_taken.append(t)

        max_time = max(time_taken)
        avg_speed = float(D)/max_time
        print "Case #{0}: {1:.6f}".format(i, round(avg_speed, 6))
 
