class House:
    def __init__(self, color, room):
        print("Self:", self)
        self.color = color
        self.room = room
    def describe(self):
        print(f"This is a {self.color} house with {self.room} rooms in it.")

    def renovate(self, new_color):
        self.color = new_color
        print(f"The house is now {self.color} after renovation.")


my_house = House("Blue", 10)
my_house.describe()
my_house.renovate("Red")
my_house1 = House("Purple", 11)
my_house1.describe()
my_house1.renovate("Red")
