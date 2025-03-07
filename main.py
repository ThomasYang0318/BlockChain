from BlockChain import BlockChain
from Transaction import Transaction

import time

# 創建區塊鏈
blockchain = BlockChain()
blockchain.create_genesis_block()

# 添加交易
transaction1 = Transaction("Alice", "Bob", 50, 1, "Payment for services")
transaction2 = Transaction("Bob", "Charlie", 30, 1, "Gift")
blockchain.pending_transactions.append(transaction1)
blockchain.pending_transactions.append(transaction2)

# 挖掘區塊
blockchain.mine_block("Miner1")

# 打印區塊鏈
print(blockchain)
