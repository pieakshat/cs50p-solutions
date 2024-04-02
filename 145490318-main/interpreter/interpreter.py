ex=input("expression: ")
x, y, z=ex.split(" ")

x=float(x)
z=float(z)


if y=='/' and z==0:
    print("invalid")

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case"*":
        print(x*z)
    case"/":
        print(x/z)
    case"%":
        print(x%z)
    case _:
        print("invalid operator")

