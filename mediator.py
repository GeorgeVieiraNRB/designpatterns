class product:
    name = ''
    id = -1
    price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class seller:
    name = ''
    money = 0
    products = []
    id = -1
    mediator = None

    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def __str__(self) -> str:
        return self.name

    def setMediator(self, mediator):
        self.mediator = mediator

    def addProduct(self, product1):
        countProduct = self.products.count(product1)
        if countProduct == 0 and isinstance(product1, product):
            self.products.append(product1)
        else:
            print(
                f'the product {product1} is already on the seller {self} list')

    def removeProduct(self, product):
        try:
            self.products.remove(product)
        except:
            print(f'product {product.name} was not found')

    def getProducts(self):
        return self.products

    def setId(self, id):
        self.id = id

    def setMoney(self, money):
        self.money = money

    def getMoney(self):
        return self.money


class buyer:
    name = ''
    money = 0
    mediator = None
    id = -1

    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def __str__(self) -> str:
        return self.name

    def setMediator(self, mediator):
        self.mediator = mediator

    def setId(self, id):
        self.id = id

    def setMoney(self, money):
        self.money = money

    def getMoney(self):
        return self.money

    def buy(self, product):
        if self.mediator != None:
            self.mediator.buyOperation(mediator, self, product)

    def seeProducts(self):
        self.mediator.showAllProducts(self.mediator, self)


class mediator:
    buyers = []
    sellers = []
    id = -1

    def __init__(self, id=0):
        pass

    def __str__(self):
        return self.id

    def addBuyer(self, buyer):
        if self.buyers.count(buyer) == 0:
            self.buyers.append(buyer)
            buyer.setMediator(self)
            buyer.setId(len(self.buyers)+1)

    def addSeller(self, seller):
        if self.sellers.count(seller) == 0:
            self.sellers.append(seller)
            seller.setMediator(self)
            seller.setId(len(self.sellers)+1)

    def setId(self, id):
        self.id = id

    def showAllProducts(self, buyer):
        if buyer in self.buyers:
            for s in self.sellers:
                print(f'\nseller {s}')
                for p in s.getProducts():
                    print(f'{p.getName()}-{p.getPrice()}', end=',')
        else:
            print(
                f'operation failed, the buyer is not linked to the mediator{self.id}')

    def buyOperation(self, buyer, product):
        if buyer in self.buyers:
            for seller in self.sellers:
                if product in seller.getProducts():
                    if buyer.getMoney() >= product.getPrice():
                        buyer.setMoney(buyer.getMoney()-product.getPrice())
                        seller.setMoney(seller.getMoney()+product.getPrice())
                        print(
                            f'\noperation done, the buyer {buyer} has bought {product} from {seller}')
                    else:
                        print(product.getPrice())
                        print(
                            f'\noperation failed, the buyer {buyer} has not enough money')
                    break
                else:
                    print(
                        f'\noperation failed, the product {product} is not available')
        else:
            print(
                f'\noperation failed, the buyer is not linked to the mediator{self.id}')


mediador = mediator()
vendedorA = seller('george')
comprador = buyer('carlos', money=100)

p1 = product(name='potato', price=13)
p2 = product(name='strawberry', price=16)
p3 = product(name='grape', price=57)
p4 = product(name='orange', price=122)
p5 = product(name='tomato', price=125)
p6 = product(name='icecream', price=28)

mediator.addBuyer(mediator, comprador)
mediator.addSeller(mediator, vendedorA)

vendedorA.addProduct(p1)
vendedorA.addProduct(p2)
vendedorA.addProduct(p3)
vendedorA.addProduct(p4)
vendedorA.addProduct(p5)
vendedorA.addProduct(p6)

comprador.seeProducts()  # mediator.showAllProducts(mediator,comprador)
comprador.buy(p4)  # mediator.buy(mediator,comprador,p4)
