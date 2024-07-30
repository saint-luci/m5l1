class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        if new_floor < self.num_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("No this floor")


h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 20)
h1.go_to(10)
h2.go_to(21)

