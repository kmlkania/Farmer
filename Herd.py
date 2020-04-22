class Herd:
    def __init__(self):
        self._animals = {
            'rabbit': 0,
            'sheep': 0,
            'pig': 0,
            'cow': 0,
            'horse': 0,
            'small_dog': 0,
            'big_dog': 0
        }

    @property
    def herd(self):
        return self._animals


class PlayerHerd(Herd):
    def __init__(self):
        super(PlayerHerd, self).__init__()
        self.retrieve_animal_from_common_herd = None
        self.add_animal_to_common_herd = None

    def add_animal(self, animal, number=1):
        if animal == 'wolf':
            if self.herd['big_dog']:
                self.add_animal_to_common_herd({'big_dog': 1})
                self.herd['big_dog'] -= 1
            else:
                self.add_animal_to_common_herd({'sheep': self.herd['sheep'], 'pig': self.herd['pig'],
                                                'cow': self.herd['cow']})
                self.herd['sheep'] = 0
                self.herd['pig'] = 0
                self.herd['cow'] = 0
        elif animal == 'fox':
            if self.herd['small_dog']:
                self.add_animal_to_common_herd({'small_dog': 1})
                self.herd['small_dog'] -= 1
            elif self.herd['rabbit'] > 1:
                self.add_animal_to_common_herd({'rabbit': self.herd['rabbit'] - 1})
                self.herd['rabbit'] = 1
        else:
            population_to_add = int((self.herd[animal] + number) / 2)
            available_animals = self.retrieve_animal_from_common_herd(animal, population_to_add)
            self.herd[animal] += available_animals

    def set_common_herd_retrieve_animal_callback(self, callback):
        self.retrieve_animal_from_common_herd = callback

    def set_add_animal_to_common_herd_callback(self, callback):
        self.add_animal_to_common_herd = callback

    def sell_animals(self, animals):
        self.add_animal_to_common_herd(animals)
        for animal, number in animals.items():
            self.herd[animal] -= number

    def buy_animals(self, animals):
        for animal, number in animals.items():
            self.herd[animal] += self.retrieve_animal_from_common_herd(animal, number)


class CommonHerd(Herd):
    def __init__(self):
        super(CommonHerd, self).__init__()
        self._initialize_common_herd()

    def _initialize_common_herd(self):
        self._animals.update({
            'rabbit': 60,
            'sheep': 24,
            'pig': 20,
            'cow': 12,
            'horse': 6,
            'small_dog': 4,
            'big_dog': 2
        })

    def retrieve_animal(self, animal, number):
        if self._animals[animal] < number:
            available_animals = self._animals[animal]
            self._animals[animal] = 0
        else:
            self._animals[animal] -= number
            available_animals = number
        return available_animals

    def add_animals(self, animals):
        for animal, number in animals.items():
            self._animals[animal] += number


class HerdHandler:
    def __init__(self, names):
        self.common = CommonHerd()
        self.players_herd = {name: PlayerHerd() for name in names}
        for player in self.players_herd.values():
            player.set_common_herd_retrieve_animal_callback(self.common.retrieve_animal)
            player.set_add_animal_to_common_herd_callback(self.common.add_animals)

    def get_common_herd(self):
        return self.common.herd

    def get_player_herd(self, name):
        return self.players_herd[name].herd

    def sell_animals(self, player, animals):
        self.players_herd[player].sell_animals(animals)

    def buy_animals(self, player, animals):
        self.players_herd[player].buy_animals(animals)

    def reproduce_animals(self, player, roll_result):
        if roll_result[0] == roll_result[1]:
            self.players_herd[player].add_animal(roll_result[0], 2)
        else:
            self.players_herd[player].add_animal(roll_result[0])
            self.players_herd[player].add_animal(roll_result[1])


