import sys

try:
    if len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("not a Python file")
except EOFError:
    sys.exit(1)

new = sys.argv[1].rstrip()
count = 0
with open(new) as file:
    for line in file:
        if not line.strip().startswith("#"):
            count += 1

print(count)
