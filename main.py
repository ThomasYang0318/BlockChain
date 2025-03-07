from BlockChain import BlockChain
from Transaction import Transaction

import time

def main():
    blockchain = BlockChain()
    blockchain.create_genesis_block()

    while True:
        print("\n1. 添加交易")
        print("2. 挖掘區塊")
        print("3. 查看區塊鏈")
        print("4. 查看帳戶餘額")
        print("5. 驗證區塊鏈")
        print("6. 退出")
        choice = input("請選擇操作: ")

        if choice == '1':
            sender = input("輸入發送者: ")
            receiver = input("輸入接收者: ")
            amount = float(input("輸入金額: "))
            fee = float(input("輸入手續費: "))
            message = input("輸入訊息: ")
            transaction = Transaction(sender, receiver, amount, fee, message)
            blockchain.pending_transactions.append(transaction)
            print("交易已添加。")
        elif choice == '2':
            miner = input("輸入礦工名稱: ")
            blockchain.mine_block(miner)
            print("區塊已挖掘並添加到區塊鏈。")
        elif choice == '3':
            print(blockchain)
        elif choice == '4':
            account = input("輸入帳戶名稱: ")
            balance = blockchain.get_balance(account)
            print(f"{account} 的餘額為: {balance}")
        elif choice == '5':
            if blockchain.verify_blockchain():
                print("區塊鏈驗證成功。")
            else:
                print("區塊鏈驗證失敗。")
        elif choice == '6':
            break
        else:
            print("無效的選擇，請重新輸入。")

if __name__ == "__main__":
    main()
