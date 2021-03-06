class GolfClub():
    """
    GolfClub class

    Attributes:
        hand: str
            example: 'left'
        brand: str
            example: 'TaylorMade'
    """

    def __init__(self, hand, brand):
        self.hand = hand
        self.brand = brand

    @property
    def choose(self):
        print(f'Grab the {self.hand} hand {self.brand} club')

    @staticmethod
    def swing():
        print(f'Grib it and rip it')


if __name__ == "__main__":

    g1 = GolfClub(hand='right', brand='Callaway')
    print(g1.hand, g1.brand)
    g1.choose

    g2 = GolfClub(hand='left', brand='Ping')
    print(g2.hand, g2.brand)
    g2.swing()
