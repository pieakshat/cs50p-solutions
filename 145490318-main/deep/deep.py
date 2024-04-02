ans=input("what is the great question of life, the universe, and everything? ").lower().strip(" ")
if ans=="42":
    print("YES")
elif ans=="forty two":
    print("YES")
elif ans=="forty-two":
    print("YES")
else:
    print("NO")