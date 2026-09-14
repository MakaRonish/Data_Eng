class Banking:
    def __init__(self, account, amount,age):
        self.account = account #public
        self.__amount = amount #private
        self._age=age #protected

    