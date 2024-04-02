def dollars_to_float(d):
    dollars=d.lstrip('$')
    return float(dollars)

def percent_to_float(p):
    percent=p.rstrip('%')
    return float(percent)/100

def main():
    dollars= dollars_to_float(input("how much was the meal? "))
    percent=percent_to_float(input("what percent tip? "))
    tip=dollars*percent
    print(f'leave ${tip:.2f}')


main()

