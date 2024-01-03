class Payment:
    def __init__(self, price):
        self.__final_price = price + price * 0.05

    def get_final_price(self):
        return self.__final_price
        
    def set_final_price(self, discount):
        self.__final_price = self.__final_price - (self.__final_price*(discount/100))

book = Payment(10)
# print(book._final_price)
# book.__final_price = 200
book.set_final_price(10)
print(book.get_final_price())