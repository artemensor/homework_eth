from web3 import Web3

contract_address = '0x9A03A6Ab10bEc3c1f2239982A016fdf77bba33Cc'
address = "0x9102Ad82D0B038773D341BceFF80D029bF27c45d"

file = open("private_key.txt")
private_key = file.read()
file.close()

with open('contract_interface.json', 'r') as f:
    contract_interface = f.read()

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/764b1536256a4dcd98743505863bfae3'))



contract = w3.eth.contract(contract_address, abi=contract_interface)

# Выведем все начальные данные
# uint balance
# string currency
# uint total_transfers_amount;
# uint total_produce_amount;

print('Баланс - {0}, Название - {1}, Всего передано, через трансферы - {2}, Всего передано, через пополнения - {3}'.format(
    contract.functions.balance(address).call(),
    contract.functions.currency().call(),
    contract.functions.total_transfers_amount().call(),
    contract.functions.total_produce_amount().call()
))

# Сделаем транзакции

nonce = w3.eth.getTransactionCount(address)
trans_info = contract.functions.produce(5)
trans_produce = trans_info.buildTransaction({'chainId': 5, 'gas': 70000, 'nonce': nonce})
trans_signed = w3.eth.account.sign_transaction(trans_produce, private_key)
hash = w3.eth.send_raw_transaction(trans_signed.rawTransaction)
print('Баланс - {0}, Последняя операция(тип) - {1}, Последнее пополнение - {2}, Всего передано, через пополнения - {3}'.format(
    contract.functions.balance(address).call(),
    contract.functions.last_operation().call(),
    contract.functions.last_produce_amount().call(),
    contract.functions.total_produce_amount().call()
))
trans_info = contract.functions.transfer(2, address)
nonce = w3.eth.getTransactionCount(address)
trans_transfer = trans_info.buildTransaction({'chainId': 5, 'gas': 70000, 'nonce': nonce})
trans_signed = w3.eth.account.sign_transaction(trans_transfer, private_key)
hash = w3.eth.send_raw_transaction(trans_signed.rawTransaction)
print('Баланс - {0}, Последняя операция(тип) - {1}, Последний трансфер - {2}, Всего передано, через трансферы - {3}'.format(
    contract.functions.balance(address).call(),
    contract.functions.last_operation().call(),
    contract.functions.last_transfer_amount().call(),
    contract.functions.total_transfers_amount().call()
))

# Итог

print('Баланс - {0}, Название - {1}, Всего передано, через трансферы - {2}, Всего передано, через пополнения - {3}'.format(
contract.functions.balance(address).call(),
contract.functions.currency().call(),
contract.functions.total_transfers_amount().call(),
contract.functions.total_produce_amount().call()
))

