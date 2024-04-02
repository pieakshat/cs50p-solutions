grocery_list=[]

try:
    while True:
        item=input("enter item:  ")
        grocery_list.append(item)
except EOFError:
        pass

item_counts=counter([item.lower() for item in grocery_list])
sorted_items=sorted(set([item.capitalize() for item in grocery_list]))

for item in sorted_items:
    count=item_counts[item.lower()]
    print(f"{count} {item.upper()}")


