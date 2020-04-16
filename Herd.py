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

    def add_animal(self, animal, number):
        pass

    @property
    def rabbit(self):
        return self._animals['rabbit']


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
            self._animals[animal] -= number
            available_animals = number
        else:
            available_animals = self._animals[animal]
            self._animals[animal] = 0
        return available_animals


class HerdHandler:
    def __init__(self, names):
        self.common = CommonHerd()
        self.players_herd = {name: PlayerHerd() for name in names}

