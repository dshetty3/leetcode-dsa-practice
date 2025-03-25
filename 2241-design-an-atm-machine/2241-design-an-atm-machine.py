class ATM(object):

    def __init__(self):

        self.bank_notes = [20, 50, 100, 200, 500]
        self.cash = [0] * 5
        

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i, n in enumerate(banknotesCount):
            self.cash[i] += n

    
    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        res = [0] * 5


        for i in range(len(self.bank_notes) - 1, -1, -1):
            if amount >= self.bank_notes[i]:  
                req = min(self.cash[i], amount // self.bank_notes[i])  
                res[i] = req
                amount -= req * self.bank_notes[i]

        if amount != 0:  
            return [-1]

        for i in range(5):
            self.cash[i] -= res[i]

        return res




        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)