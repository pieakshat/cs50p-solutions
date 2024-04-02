import emoji

def emogize_text(text):
    emogi=emoji.emojize(text, language='alias')
    return emogi

user_input=input("input: ")
emojized_output=emogize_text(user_input)
print("output: ", emojized_output)
