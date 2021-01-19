class Zoo:
    __animals = 0

    def __int__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, names):
        if species == 'mammal':
            self.mammals.append(names)
        elif species == 'fish':
            self.fishes.append(names)
        elif species == 'birds':
            self.birds.append(names)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"{species} in {self.name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"{species} in {self.name}: {', '.join(self.fishes)}"
        elif species == 'birds':
            result += f"{species} in {self.name}: {', '.join(self.birds)}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
