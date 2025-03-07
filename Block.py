import time
class Block:
    def __init__(self,previous_hash,difficulty,miner,miner_rewards):
        self.previous_hash = previous_hash
        self.hash = ''
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = int(time.time())
        self.transactions = []
        self.miner = miner
        self.miner_rewards = miner_rewards

    def __str__(self):
        transactions_str = "\n".join([str(tx) for tx in self.transactions])
        return f"Block mined by {self.miner} with hash {self.hash}:\n{transactions_str}"