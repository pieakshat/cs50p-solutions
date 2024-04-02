#def convert(text):
 #   text.replace(':)', '🙂').replace(':(', '🙁')
  #  return text

#def main():
 #   user_input=input("enter text: ")

  #  converted_text=convert(user_input)

   # print(converted_text)

#main()


def convert(text):
    # Replace text emoticons with emojis
    text = text.replace(':)', '🙂').replace(':(', '🙁')
    return text

def main():
    # Input text from the user
    user_input = input("Enter text: ")

    # Call the convert function and store the result in a variable
    converted_text = convert(user_input)

    # Print the converted text
    print(converted_text)

# Call the main function to start the program
if __name__ == "__main__":
    main()






