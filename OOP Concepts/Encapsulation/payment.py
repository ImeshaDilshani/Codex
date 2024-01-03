class Payment:
    def __init__(self, price):
        self.__final_price = price + price * 0.1

book = Payment(100)
# print(book._final_price)
# book.__final_price = 200
print(book.__final_price)