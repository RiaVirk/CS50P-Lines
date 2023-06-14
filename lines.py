# import sys

# if len(sys.argv) == 2:
#     if sys.argv[1][-2] == "py":
#         try:
#             with open(sys.argv[1]) as file:
#                 nlines = 0
#                 for line in file:
#                     if not line.lstrip().startswith("#") and line.lstrip() != "":
#                         nlines += 1
            
#             print(nlines)
#         except FileNotFoundError:
#             sys.exit("File not found")
    
# elif sys.argv[1][-2:] != "py":
#     sys.exit("Not a python file")

# elif len(sys.argv) < 2:
#     sys.exit("Too few command-line arguments")

# elif len(sys.argv) > 2:
#     sys.exit("Too many command-line arguments")


import sys


def main():
    arg_check(sys.argv)

    print(get_lines(sys.argv[1]))


def arg_check(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def get_lines(filename):
    counter = 0
    try:
        with open(filename) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter


if __name__ == "__main__":
    main()