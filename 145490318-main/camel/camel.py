def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

user_input = input("camel case: ")
snake_case_result = camel_to_snake(user_input)
print("snake case: ", snake_case_result)

