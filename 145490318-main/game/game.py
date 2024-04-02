import random
def loop(k):
     while True:
        try:
            k = int(k)
            if k > 0:
                return k
            else:
                k = int(input("level: "))
        except ValueError:
            continue


def main():
     set_level=loop(input("level: "))
     guess_int = random.randrange(1, set_level+1)

     user_guess=loop(input("guess: "))

     while user_guess != guess_int:
        if user_guess>guess_int:
            print("too large!")
        elif user_guess<guess_int:
            print("too small!")
        else:
            print("just right!")
        user_guess=loop(input("guess: "))

     print("just right!")




main()  
