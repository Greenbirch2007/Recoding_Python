

class LineItem:

    def __init__(self,description,weihgt,price):
        self.description =description
        self.weihgt = weihgt
        self.price  = price


    def subtotal(self):
        return self.weihgt * self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value > 0 :
            self._weight = value
        else:
            raise ValueError('value must be > 0')

