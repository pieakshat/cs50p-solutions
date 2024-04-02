def main():
     plate = input("Plate: ")
     if is_valid(plate):
        print("Valid")
     else:
        print("Invalid")


def is_valid(s):
        if not s[0:2].isalpha():
             return False
        if len(s)<2 or len(s)>6:
             return False
        if s[-1].isdigit() or s[-1]=='0':
             return False
        if any(char in s for char in ". ,!@#$%^&*()_+[]{}|;':\"<>?"):
             return False

        return True


if __name__ == "__main__":



 main()