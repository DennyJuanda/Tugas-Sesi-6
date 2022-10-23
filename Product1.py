class Product:
    id = 0 
    name = ''
    price = 0
    quantity = 0
    total = 0

    def __init__(self, id , name, price, quantity):
        self.id = id
        self.name = name 
        self.price = price  
        self.quantity = quantity

    def displayProduct(self):
        print("id : ", self.id)
        print("name :",self.name)
        print("price :",self.price)
        print("quantity :",self.quantity)

prod1 = Product("001","Baju",50000,10)
prod1.displayProduct()