import sys
def main():
    argv = sys.argv[1:]
    num_arguments = len(argv)
    if num_arguments != 1:
        a='s'
    else:
        a ='' 
    print(f"Number of argument{'s' if num_arguments != 1 else ''}: {num_arguments}", end='')
    if num_arguments > 0:
        print(":", end='')
    print()
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".fomart(i,arg))
if __name__ == "__main__":
    main()
