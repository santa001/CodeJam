# File Fix-it

def add_child(p, c):
    if not p.has_key(c):
        p[c] = {}
        return True
    return False

def build_tree(e_dirs, d_list):
    count = 0
    temp = e_dirs

    for i in d_list:
        if temp.has_key(i):
            temp = temp[i]
            continue
        else:
            if True == add_child(temp, i):
                count += 1
            temp = temp[i]

    return count

def solve(n, m):
    count = 0
    e_dirs = {}
    build_tree(e_dirs, ['/'])
    
    for i in range(0, n):
        dir_p = raw_input().split('/')
        if len(dir_p[0]) == 0:
            if len(dir_p) == 1:
                continue
            else:
                dir_p = dir_p[1:]
        build_tree(e_dirs, dir_p)

    for i in range(0, m):
        dir_p = raw_input().split('/')
        if len(dir_p[0]) == 0:
            if len(dir_p) == 1:
                continue
            else:
                dir_p = dir_p[1:]
        count += build_tree(e_dirs, dir_p)

    return count


if __name__ == "__main__":
    T = int(raw_input())
    
    for i in range(1, T+1):
        n, m =  map (int, raw_input().split())        
        count = solve(n, m)
        print "Case #{0}: {1}".format(i, count)
        
