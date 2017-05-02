def is_tidy(m_str):
    i = len(m_str) - 1
    while i > 0:
        if m_str[i] < m_str[i-1]:
            return False
        i -= 1
    return True

def solve(N):
    max_val = int(N)
    ms = list(N)

    if is_tidy(N):
        return int(N)

    i = len(ms) -1
    while i > 0:
	ms[i] = '9'
	ms[0:i] = list(str(int("".join(ms[0:i])) - 1))
	if ms[0] == '0':
	    return int("".join(ms))
        val = int("".join(ms))
        if (val<= max_val):
            if is_tidy(str(val)):
                return int("".join(ms))
	i -= 1

    return int("".join(ms))

if __name__ == "__main__":
    T = int(raw_input())
    for i in range (1, T+1):
	N = raw_input()
	s = solve(N)
	print "Case #{0}: {1}".format(i, s)
