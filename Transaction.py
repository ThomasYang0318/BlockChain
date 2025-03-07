class Transaction:
    def __init__(self,sender,receiver,amounts,fee,message):
        self.sender = sender
        self.receiver = receiver
        self.amounts = amounts
        self.fee = fee
        self.message = message

    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver} of {self.amounts} with fee {self.fee}. Message: {self.message}"