class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def apply_discount(self,discount):
        print('Discount:',discount)
        self.price=self.price-discount
        print('Price after Discount:',self.price)
        
    def display(self):
        print('Book Title:',self.title)
        print('Original Price:',self.price)
b1=Book('Python Basics',15000)
b1.display()
b1.apply_discount(2000)
b1.display()