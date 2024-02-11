import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    # Print number of arguments
    if num_args == 0:
        print("0 argument.", end="")
    elif num_args == 1:
        print("1 argument:", end="")
    else:
        print("{} arguments:".format(num_args), end="")

    # Print arguments
    if num_args > 0:
        print()
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print(".")

