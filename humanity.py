from web3 import Web3, HTTPProvider
import json
import time
from datetime import datetime

print("Auto Wrap & Unwrap ETH Taiko")
print("")

web3 = Web3(Web3.HTTPProvider("https://rpc.testnet.humanity.org"))

# Connect to web3
if web3.is_connected():
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()