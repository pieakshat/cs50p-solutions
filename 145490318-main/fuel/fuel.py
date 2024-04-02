def main():
        res=get_in("fraction: ")
        result(res)


def get_in(prompt):
    while True:
        try:
            fr=input(prompt).split('/')
            x=int(fr[0])
            y=int(fr[1])
        except (ValueError, IndexError):
                pass
        else:
                break
    per = (x / y)*100
    per=int(per)
    return per

def result(per):
    if per<=1:
        print("E")
    elif per>=99:
        print("F")
    else:
        print(f"{per}%")

main()


