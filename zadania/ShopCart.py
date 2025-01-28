

class ShopCart:

    def __init__(self):
        self.items = {}

    def AddItem(self, itemName, price):
        if itemName not in self.items:
            self.items[itemName] = 0

        self.items[itemName] += price

    def RemoveItem(self, itemName):
        if itemName in self.items:
            del self.items[itemName]
        else:
            print("Item", itemName," not in cart")

    def PrintContent(self):
        for key in self.items:
            print(key, ": ", self.items[key], " eur")
        
        print("celkovo: ", sum(self.items.values()))


cart = ShopCart()
cart.AddItem("Subaru WRX", 30000)
cart.AddItem("zuvacky", 1)
cart.AddItem("zemiaky", 5)
cart.AddItem("zemiaky", 5)

cart.PrintContent()

cart.RemoveItem("zuvacky")
cart.RemoveItem("a")

cart.PrintContent()

