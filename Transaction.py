class Transaction:
    def __init__(self, sender, receiver, amount, fee, message):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.message = message

    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver} of {self.amount} with fee {self.fee}. Message: {self.message}"