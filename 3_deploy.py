from compile import abi, bytecode
from web3 import Web3

RPC_URL = 'http://localhost:7545'
web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Change to correct network

account_from = {
    'private_key': '1333bbf373c80c4384cc5bd140088905d2c5073fcc4cfba8d570e453b6285336',
    'address': '0xC39FeA19F7D4a7FB593CEb22BF084Fc77F345c44',
}

print(f'Attempting to deploy from account: { account_from["address"] }')

Incrementer = web3.eth.contract(abi=abi, bytecode=bytecode)

construct_txn = Incrementer.constructor(5).buildTransaction({
        'gasPrice': web3.eth.gas_price,
        'chainId': 1337,
        'from': account_from['address'],
        'nonce': web3.eth.getTransactionCount(account_from['address']),
    }
)

tx_create = web3.eth.account.signTransaction(construct_txn, account_from['private_key'])

tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')
