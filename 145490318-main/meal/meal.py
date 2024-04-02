def convert_time_to_decimal(time_str):
    hours, minutes = time_str.split(":")
    hours=int(hours)
    minutes=int(minutes)
    decimal_time=hours + (minutes/60)
    return(decimal_time)

def main():
    ti=input("what time is it? ").strip()
    z=convert_time_to_decimal(ti)
    print("time in decimal format: ",z)

    if(7<= z <=8):
        print("breakfast time")

    elif(12<= z <=1):
        print("lunch time")

    elif(18<= z <=19):
        print("dinner time")

main()





