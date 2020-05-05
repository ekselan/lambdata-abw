#my_lambdata/polos.py

# Polo Class
# attributes / properties (NOUNS): size, style, color,
    # texture, price

#methods (VERBS): wash, fold, pop collar

# TODO: initialize a small blue polo and a large
# yellow polo


class Polo():
    def __init__(self, size, color):
        print(size)
        print(color)
        

if __name__ == "__main__":
    
# df = DataFrame(_________)
# df.columns
# df.head()

p1 = Polo(size='Small', color='blue')
print(p1.size, p1.color)
p1.wash

p2 = Polo(size='large', color='yellow')
print(p2.size, p2.color)
p2.fold()