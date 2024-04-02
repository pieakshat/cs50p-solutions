import tabulate
import sys
rows=[]
try:
    if len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("not a Python file")
except EOFError:
    sys.exit(1)

with open (sys.argv[1]) as file:
    reader=csv.reader(file)
    for row in reader:
        rows.append(row)


