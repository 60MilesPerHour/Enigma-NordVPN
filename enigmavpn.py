import os
import random
import time
import pycountry
from termcolor import colored

supported_vpn_services = ['nordvpn', 'expressvpn']

# get list of country codes
country_codes = [country.alpha_2 for country in pycountry.countries]

# function to connect to a VPN server
def connect_to_vpn(vpn_service, country_code):
    if vpn_service not in supported_vpn_services:
        print(colored(f"{vpn_service} is not a supported VPN service.", 'red'))
        return False
    
    if not country_code:
        country_code = random.choice(country_codes)
    elif country_code not in country_codes:
        print(colored(f"{country_code} is not a valid country code. Trying again with a different one...", 'yellow'))
        country_code = random.choice(country_codes)
    
    os.system(f'{vpn_service} c {country_code}')
    return True

# main function
def main(interval):
    while True:
        success = connect_to_vpn('nordvpn', None)  # change this to 'expressvpn' if needed
        if success:
            print(colored(f"VPN connected to {pycountry.countries.get(alpha_2=os.environ['NORDVPN_COUNTRY']).name}.", 'green'))
        else:
            print(colored("Failed to connect to VPN. Retrying...", 'red'))
        time.sleep(interval * 60)  # convert interval to seconds

if __name__ == '__main__':
    interval = int(input("Enter the interval (in minutes) for changing VPN: "))
    main(interval)
