from key import verify_signature


class Transaction:
    def __init__(self, sender, receiver, amount, time=0, tx_number=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = time
        self.tx_number = tx_number
        self.tx_signer = None
        
    def __repr__(self):
        string = "Transaction number: " + str(self.tx_number) + "\n" + \
                 "Sender: " + str(self.sender) + "\n" + \
                 "Receiver: " + str(self.receiver) + "\n" + \
                 "Amount: " + str(self.amount) + "\n" + \
                 "Timestamp: " + str(self.time) + "\n"
        return string
    
    def to_dict(self):
        tx_dict = {}
        tx_dict["tx_number"] = self.tx_number
        tx_dict["sender"] = self.sender
        tx_dict["receiver"] = self.receiver
        tx_dict["amount"] = self.amount
        tx_dict["timestamp"] = self.time
        return tx_dict

    def sign(self, account):
        string = "Transaction number: " + str(self.tx_number) + "\n" + \
                 "Sender: " + str(self.sender) + "\n" + \
                 "Receiver: " + str(self.receiver) + "\n" + \
                 "Amount: " + str(self.amount) + "\n"+ \
                 "Timestamp: " + str(self.time) + "\n"
        self.tx_signer = account.sign(string)

    def verify(self):
        string = "Transaction number: " + str(self.tx_number) + "\n" + \
                 "Sender: " + str(self.sender) + "\n" + \
                 "Receiver: " + str(self.receiver) + "\n" + \
                 "Amount: " + str(self.amount) + "\n"+ \
                 "Timestamp: " + str(self.time) + "\n"
        if self.amount < 0 :
            return False
        if not verify_signature(self.tx_signer, string, self.sender):
            return False
        return True
