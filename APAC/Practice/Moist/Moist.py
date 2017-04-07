if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
	cost = 0
	N = int(raw_input())
	for k in range(0, N):
	    if (k == 0):
		prev = raw_input()
	    else:
		curr = raw_input()
		if (curr < prev):
		    cost += 1
		else:
		    prev = curr
	print "Case #%d: %d" %(i, cost)
