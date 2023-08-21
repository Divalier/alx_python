import sys
def main():
    if __name__ == "__main__":
     argv = sys.argv[1:]
     num_arguments = len(argv)
     if num_arguments != 1:
        a='s'
     else:
        a ='' 
     print("Number of argument{}".format(a), end='')
     if num_arguments > 0:
        print(":", end='')
     print()
     for i, arg in enumerate(argv, start=1):
        print("{}: {}".fomart(i,arg))

