def main():
    inp = input("Input: ")
    output = shorten(inp)
    print(output)

def shorten(k):
    ans_str = ""
    for char in k:
        if char not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            ans_str += char
    return ans_str

if __name__ == "__main__":
    main()




