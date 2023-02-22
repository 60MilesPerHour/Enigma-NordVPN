# VPN Randomizer

This Python script connects to a VPN service (NordVPN or ExpressVPN) and changes the VPN server every N minutes, where N is specified by the user.

The country of the VPN server is randomized every time the VPN connection is changed. The script supports all 2-digit country codes, and if an invalid country code is entered, the script will try again with a different one until a valid one is found.

## Installation

1. Clone this repository:
``git clone https://github.com/60MilesPerHour/Enigma-NordVPN.git``

2. Install the required Python packages:
pip install -r requirements.txt

3. Have either nordvpn or expressvpn installed on linux.


## Usage

1. Run the script:
``python3 enigmavpn.py``

2. Enter the interval (in minutes) for changing VPN when prompted.
3. The script will connect to a random VPN server every N minutes (where N is the interval specified by the user).

## Supported VPN Services

- NordVPN
- ExpressVPN

## Notes

- The script is currently set to use the NordVPN service by default. If you want to use ExpressVPN instead, change the `vpn_service` parameter in the `connect_to_vpn` function to `'expressvpn'`.
- The console output is color-coded to make it more visually appealing.
- The script will run indefinitely until manually stopped.
