# Battleships
# Kris Quinn

class Fleet(object):

    def __init__(self, name):
        self.ships = list()
        self.name = name
        self.destroyed = False

    def __str__(self):
        return self.name + ': ' + str(self.count_live_ships()) + ' ships afloat'

    def add_ship(self, ship):
        self.ships.append(ship)

    def count_live_ships(self):
        afloat = 0
        for ship in self.ships:
            if not ship.destroyed:
                afloat += 1
        return afloat

    def check_if_destroyed(self):
        afloat = 0
        for ship in self.ships:
            if not ship.destroyed:
                afloat += 1
        if afloat == 0:
            print(self.name + ' has been destroyed!')

    def check_if_hit(self, coordinates):
        for ship in self.ships:
            if self.destroyed:
                print(self.name + ': Sunk')
            else:
                ship.check_if_hit(coordinates)

    def report(self):
        print(self)
        for ship in self.ships:
            print(ship)
    
class Battleship(object):

    def __init__(self, name = ''):
        self.name = name
        self.destroyed = False
        self.positions = list()
        self.hits = list()

    def __str__(self):
        return 'Ship: ' + self.name + ', Destroyed: ' + str(self.destroyed)

    def add_position(self, coordinates):
        self.positions.append(coordinates)

    def check_if_hit(self, coordinates):
        hit = False
        for position in self.positions:
            if coordinates == position:
                hit = True
        if hit:
            self.validate_hit(coordinates)                   
        else:
            print("You missed!")

    def validate_hit(self, coordinates): 
        if len(self.hits) == 0:
            print("You hit " + self.name + "!") 
            self.hits.append(coordinates) 
        else:    
            for hit in self.hits:
                if coordinates == hit:
                    if self.destroyed:
                        print("You hit a destroyed ship.")
                    else:
                        print("Ship already hit in that location!!")
                else:
                    print("You hit " + self.name + "!")
                    self.hits.append(coordinates)
                    self.check_if_destroyed()

    def check_if_destroyed(self):                    
        if len(self.hits) == len(self.positions):
            self.destroyed = True
            print(self.name + ' has been destroyed!!')

def enter_coordinates():
    x = int(input("X coordinate: "))
    y = int(input("Y coordinate: "))

    coordinates = (x, y)
    return coordinates

def main():
    
    enterprise = Battleship(name = 'Enterprise')

    enterprise.add_position((1,2))
    enterprise.add_position((2,2))
    enterprise.add_position((3,2))

    voyager = Battleship(name = 'Voyager')

    voyager.add_position((4,5))
    voyager.add_position((4,6))
    voyager.add_position((4,7))

    bogie_1 = Battleship(name = 'Bogie 1')

    bogie_1.add_position((3,3))
    bogie_1.add_position((4,3))
    bogie_1.add_position((5,3))

    bogie_2 = Battleship(name = 'Bogie 2')

    bogie_2.add_position((3,4))
    bogie_2.add_position((4,4))
    bogie_2.add_position((5,4))

    ours = Fleet('Our Fleet')
    ours.add_ship(enterprise)
    ours.add_ship(voyager)

    theirs = Fleet('Their Fleet')
    theirs.add_ship(bogie_1)
    theirs.add_ship(bogie_2)

    ours.report()
    theirs.report()
    
    while ours.count_live_ships() and theirs.count_live_ships():
        
        coordinates = enter_coordinates()

        ours.check_if_hit(coordinates)
        theirs.check_if_hit(coordinates)

        print('Ships left: {}'.format(ours.count_live_ships() + theirs.count_live_ships()))
        ours.report()
        theirs.report()

    ours.check_if_destroyed()
    theirs.check_if_destroyed()
   
if __name__ == '__main__':
    main()
    
    
