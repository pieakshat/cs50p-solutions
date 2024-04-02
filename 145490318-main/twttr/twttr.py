input_str=input("input: ")
ans_str=""
for char in input_str:
    if char not in ['a','e','i','o','u','A','E','I','O','U']:
        ans_str += char
print("output: ", ans_str)
