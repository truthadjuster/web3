from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
if w3.isConnected():
    print("*** connected ***")
    latest = w3.eth.get_block('latest')
    print(type(latest))
    print(str(latest))
    # json_object = json.dumps(latest, indent = 4)
    # print(json_object)
