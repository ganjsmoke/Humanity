from web3 import Web3
from colorama import init, Fore, Style
import sys
import time

# Initialize colorama
init(autoreset=True)

# Header message
def display_header():
    print(Fore.CYAN + Style.BRIGHT + "===============================")
    print(Fore.YELLOW + Style.BRIGHT + "Auto Daily Claim $RWT Humanity Protocol")
    print(Fore.CYAN + Style.BRIGHT + "Bot created by: " + Fore.GREEN + "https://t.me/airdropwithmeh")
    print(Fore.CYAN + Style.BRIGHT + "===============================\n")

# Connect to the blockchain network
rpc_url = 'https://rpc.testnet.humanity.org'
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if connected to the network
if web3.is_connected():
    print(Fore.GREEN + "Connected to Humanity Protocol")
else:
    print(Fore.RED + "Connection failed.")
    sys.exit(1)  # Exit if connection fails

# Smart contract address and ABI
contract_address = '0xa18f6FCB2Fd4884436d10610E69DB7BFa1bFe8C7'
contract_abi = [{"inputs":[],"name":"AccessControlBadConfirmation","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"neededRole","type":"bytes32"}],"name":"AccessControlUnauthorizedAccount","type":"error"},{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bool","name":"bufferSafe","type":"bool"}],"name":"ReferralRewardBuffered","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":True,"internalType":"enum IRewards.RewardType","name":"rewardType","type":"uint8"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"RewardClaimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimBuffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cycleStartTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"vcContract","type":"address"},{"internalType":"address","name":"tkn","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"callerConfirmation","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"}],"name":"start","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userBuffer","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"epochID","type":"uint256"}],"name":"userClaimStatus","outputs":[{"components":[{"internalType":"uint256","name":"buffer","type":"uint256"},{"internalType":"bool","name":"claimStatus","type":"bool"}],"internalType":"struct IRewards.UserClaim","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userGenesisClaimStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

# Load the contract
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

# Function to load private keys from a text file
def load_private_keys(file_path):
    with open(file_path, 'r') as file:
        private_keys = [line.strip() for line in file if line.strip()]
    return private_keys

# Function to claim rewards
def claim_rewards(private_key):
    try:
        # Derive the sender's address from the private key
        account = web3.eth.account.from_key(private_key)
        sender_address = account.address

        # Check if the genesis reward has already been claimed
        genesis_reward_claimed = contract.functions.userGenesisClaimStatus(sender_address).call()

        # Get the current epoch from the contract
        current_epoch = contract.functions.currentEpoch().call()

        # Check if the reward has already been claimed for the current epoch
        reward_claim_status = contract.functions.userClaimStatus(sender_address, current_epoch).call()

        # reward_claim_status is a tuple: (buffer, claimStatus)
        buffer_amount, claim_status = reward_claim_status
        
        # If the genesis reward is claimed
        if genesis_reward_claimed:
            # If userClaimStatus is False, proceed to claim the reward
            if not claim_status:
                print(Fore.GREEN + f"Proceeding to claim reward for address: {sender_address} (Genesis reward claimed).")
                proceed_to_claim(sender_address, private_key)
            else:
                print(Fore.YELLOW + f"Reward already claimed for address: {sender_address} in epoch {current_epoch}. Skipping.")

        # If the genesis reward is not claimed
        else:
            print(Fore.GREEN + f"Proceeding to claim reward for address: {sender_address} (Genesis reward not claimed).")
            proceed_to_claim(sender_address, private_key)

    except Exception as e:
        error_message = str(e)

        # Check for specific error: "Rewards: user not registered"
        if "Rewards: user not registered" in error_message:
            print(Fore.RED + f"Error: User {sender_address} is not registered.")
        else:
            print(Fore.RED + f"Error claiming reward for {sender_address}: {error_message}")

def proceed_to_claim(sender_address, private_key):
    try:
        # Estimate gas limit for the claimReward transaction
        gas_amount = contract.functions.claimReward().estimate_gas({
            'chainId': web3.eth.chain_id,
            'from': sender_address,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender_address)
        })

        # Build the transaction to call the 'claimReward' function
        transaction = contract.functions.claimReward().build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender_address,
            'gas': gas_amount,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender_address)
        })

        # Sign the transaction with the private key
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # Wait for the transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(Fore.GREEN + f"Transaction successful for {sender_address} with hash: {web3.to_hex(tx_hash)}")
    
    except Exception as e:
        print(Fore.RED + f"Error processing claim for {sender_address}: {str(e)}")

# Main execution: display header, load private keys, and claim rewards for each
if __name__ == "__main__":
    display_header()
    # Infinite loop to run the process every 6 hours
    while True:
        private_keys = load_private_keys('private_keys.txt')
        for private_key in private_keys:
            claim_rewards(private_key)
        
        # Wait for 6 hours (1 * 60 * 60 seconds)
        print(Fore.CYAN + "Waiting for 6 hours before the next run...")
        time.sleep(6*60*60)  # For testing purposes, you may want to reduce this time
