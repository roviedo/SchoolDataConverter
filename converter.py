import sys

def main():
    pass
    if len(sys.argv) < 3:
        print "Please follow program running scheme is incorrect"
        exit(0)
    filename = sys.argv[1]
    print filename , "\n"
    #x = classblah()
    #x.classmethod(filename)
    types = sys.argv[2].split('2')
    print "\n", type(types)

if __name__ == "__main__":
    main()
