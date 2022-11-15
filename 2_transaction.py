from web3 import Web3

RPC_URL = "http://localhost:7545"
web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Change to correct network

account_from = {
    "private_key": "1333bbf373c80c4384cc5bd140088905d2c5073fcc4cfba8d570e453b6285336",
    "address": "0xC39FeA19F7D4a7FB593CEb22BF084Fc77F345c44",
}
address_to = "0x23da39c4ac72cB4073344392d389627ED43b2191"

print(f'Attempting to send transaction from { account_from["address"] } to { address_to }')

tx_create = web3.eth.account.signTransaction({
        "nonce": web3.eth.getTransactionCount(account_from["address"]),
        "gasPrice": 0,
        "gas": 21000,
        "to": address_to,
        "value": web3.toWei("1", "ether"),
    },
    account_from["private_key"],
)

tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")
