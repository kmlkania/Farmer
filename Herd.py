class Herd:
    def __init__(self):
        self._animals = {
            'rabbit': 0,
            'sheep': 0,
            'pig': 0,
            'cow': 0,
            'horse': 0}

    def add_animal(self, animal, number):
        self._animals[animal] += number

    @property
    def rabbit(self):
        return self._animals['rabbit']
