from datetime import datetime
import inflect
p=inflect.engine()

def calculate_age_in_minutes(date_of_birth):
    # Convert date of birth string to a datetime object
    birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')


    # Get today's date
    today_date = datetime.now().date()

    # Calculate age in minutes
    age_in_minutes = (today_date - birth_date.date()).total_seconds() / 60

    return round(age_in_minutes)

def main():
    # Prompt the user for their date of birth

    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")


    # Calculate age in minutes
    age_in_minutes = calculate_age_in_minutes(date_of_birth)
    words=p.number_to_words(age_in_minutes)

    # Print the age in minutes using English words
    print(f"You are approximately {words} minutes old.")

if __name__ == "__main__":
    main()