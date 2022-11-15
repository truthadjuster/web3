from compile import abi, bytecode
from web3 import Web3

RPC_URL = 'http://localhost:7545'
web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Change to correct network

account_from = {
    'private_key': '1333bbf373c80c4384cc5bd140088905d2c5073fcc4cfba8d570e453b6285336',
    'address': '0xC39FeA19F7D4a7FB593CEb22BF084Fc77F345c44',
}
contract_address = '0xdE6887afFE76C9B08A02333C1b6B3de95A12d8b4'

print(f'Calling the reset function in contract at address: { contract_address }')

Incrementer = web3.eth.contract(address=contract_address, abi=abi)

reset_tx = Incrementer.functions.reset().buildTransaction({
        'gasPrice': web3.eth.gas_price,
        'chainId': 1337,
        'from': account_from['address'],
        'nonce': web3.eth.getTransactionCount(account_from['address']),
    }
)

tx_create = web3.eth.account.signTransaction(reset_tx, account_from['private_key'])
tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')
