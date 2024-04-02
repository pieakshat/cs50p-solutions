amount_due = 50
amount_inserted = 0

while amount_inserted<amount_due:
    user_input=int(input("enter amount: "))
    if user_input==5 or user_input==10 or user_input==25:
        amount_inserted += user_input
        print("Amount due: {}".format(amount_due-amount_inserted))
    else:
        print("Amount due: 50" )

change_due=amount_inserted-amount_due
print("Amount owed: ", change_due)

