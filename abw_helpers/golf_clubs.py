class GolfClub():
    """
    GolfClub class
    """
    def __init__(self, hand, brand):
        self.hand = hand
        self.brand = brand
    
    @property
    def choose(self):
        print('Grab the golf club')

    # @staticmethod
    def swing(self):
        print('Swing the golf club')

g1 = GolfClub(hand='right', brand='Callaway')
print(g1.hand, g1.brand)
g1.choose

g2 = GolfClub(hand='left', brand='Ping')
print(g2.hand, g2.brand)
g2.swing