def main():
    gr=input("greeting: ").strip().lower()
    ans=value(gr)
    print(f"${ans}")

def value(gr):

    if gr.startswith("hello"):
        an=0
        return an

    elif gr.startswith("h"):
        an=20
        return an

    else:
        an=100
        return an

if __name__=="__main__":
    main()

