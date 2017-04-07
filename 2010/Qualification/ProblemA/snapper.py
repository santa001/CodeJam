if __name__ == "__main__":
   T = int(raw_input())
   for i in range(1, T+1):
      N, K = map (int, raw_input().split())
      print "Case #{0}: {1}". format(i, "ON" if (K % (2 **N)) == ((2 ** N) - 1) else "OFF") 
