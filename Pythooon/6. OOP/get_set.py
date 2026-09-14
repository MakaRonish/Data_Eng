class Child:
    def __init__(self,address):
        self.__address

    def update_address(self,new_address):
        self.__address = new_address

    def get_address(self):
        return self.__address