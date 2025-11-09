class CellPhones:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price: float = 0

    def set_manufact(self, manufact: str):
        self.__manufact = manufact

    def set_model(self, model: str):
        self.__model = model

    def set_retail_price(self, retail_price: float):
        self.__retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price