from web3 import Web3

RPC_URL = "http://localhost:7545"
web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Change to correct network

address_from = "0xC39FeA19F7D4a7FB593CEb22BF084Fc77F345c44"
address_to = "0x23da39c4ac72cB4073344392d389627ED43b2191"

balance_from = web3.fromWei(web3.eth.getBalance(address_from), "ether")
balance_to = web3.fromWei(web3.eth.getBalance(address_to), "ether")

print(f"The balance of { address_from } is: { balance_from } ETH")
print(f"The balance of { address_to } is: { balance_to } ETH")
