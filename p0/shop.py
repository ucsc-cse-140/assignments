"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
"""

class FruitShop(object):
    def __init__(self, name, fruitPrices):
        """
        name: Name of the fruit shop

        fruitPrices: Dictionary with keys as fruit
        strings and prices for values e.g.
        {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
        """

        self.fruitPrices = fruitPrices
        self.name = name

        print('Welcome to %s fruit shop' % (name))

    def getCostPerPound(self, fruit):
        """
        fruit: Fruit string

        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """

        if fruit not in self.fruitPrices:
            print("Sorry we don't have %s" % (fruit))
            return None

        return self.fruitPrices[fruit]

    def getPriceOfOrder(self, orderList):
        """
        orderList: List of (fruit, numPounds) tuples

        Returns cost of orderList. If any of the fruit are
        """

        totalCost = 0.0
        for fruit, numPounds in orderList:
            costPerPound = self.getCostPerPound(fruit)
            if (costPerPound is not None):
                totalCost += numPounds * costPerPound

        return totalCost

    def getName(self):
        return self.name

    def __repr__(self):
        return "Fruit Shop: %s, Prices: %s" % (self.name, sorted(self.fruitPrices.items()))
