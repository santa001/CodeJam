# Standing Ovation

import sys

class Opera:
    required = 0
    total_available = 0
    max_shy = 0;
    inputs = []

    def __init__ (self, max_val, input_line):
        self.max_shy = int(max_val)
        self.inputs = map(int, input_line)

    def display(self):
        print "Max shy {}" .format(self.max_shy)
        print "Inputs {}" .format(self.inputs)
    
    def solve(self):
        limit = len(self.inputs)
        self.total_available = self.inputs[0]
        for i in range(1, limit):
            if (self.inputs[i]):
                if (i > self.total_available):
                    additional = i - self.total_available
                    self.required += additional
                    self.total_available += additional + self.inputs[i]
                else:
                    self.total_available += self.inputs[i]
        return self.required

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "No input file "
        sys.exit(-1)

    input_file = sys.argv[1]
    output_file = input_file+"_out"
    output_buffer = ""
    
    fd_in = open(input_file, 'r')
    
    num = int(fd_in.readline().strip())
    for i in range(0, num):
        buffer = fd_in.readline()
        max_shy, input_line = buffer.split()
        
        opera = Opera(max_shy, input_line)
        #opera.display()
        val = opera.solve()
        #print "Case #{0}: {1}".format(i+1, val)
        output_buffer += "Case #{0}: {1}\n".format(i+1, val)

    fd_out = open(output_file, "w")
    fd_out.write(output_buffer)
    fd_out.close()
    fd_in.close()
        

    
        
