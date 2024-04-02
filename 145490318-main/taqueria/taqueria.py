menu= { "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

def main():
    order=[]
    total_cost=0

    try:
        while True:
            item_input=input("item: ").strip().capitaize()
            if item_input in menu:
                order.append(item_input)
                total_cost += menu[item_input]
                print(f"${total_cost}")
            else:
                pass
    except EOFError:
            print("item: ")

main()

