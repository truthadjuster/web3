from compile import abi, bytecode
from web3 import Web3

RPC_URL = 'http://localhost:7545'
web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Change to correct network

contract_address = '0xdE6887afFE76C9B08A02333C1b6B3de95A12d8b4'

print(f'Making a call to contract at address: { contract_address }')

Incrementer = web3.eth.contract(address=contract_address, abi=abi)
number = Incrementer.functions.number().call()

print(f'The current number stored is: { number } ')
