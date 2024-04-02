import requests
import sys
import json

def main():
    number_of_bits = get_bits()
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = json.loads(response.text)
    amount_str = data['bpi']['USD']['rate']
    amount_str = amount_str.replace(",", "")
    usd_val = float(amount_str)
    amount = usd_val * number_of_bits
    print(f"Amount: ${amount:,.4f}")

def get_bits():
    if len(sys.argv) < 2:
        sys.exit("Missing command line argument")
    try:
        bit_no = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a float")
        sys.exit(1)
    return bit_no

if __name__ == "__main__":
    main()