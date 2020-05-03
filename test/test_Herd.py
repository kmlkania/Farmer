import pytest


def test_herd_can_be_obtained():
    from Game.Herd import Herd
    herd = Herd()
    assert herd.herd == {
        'rabbit': 0,
        'sheep': 0,
        'pig': 0,
        'cow': 0,
        'horse': 0,
        'small_dog': 0,
        'big_dog': 0
    }


def test_animal_can_be_retrieved_from_common_herd():
    from Game.Herd import CommonHerd
    herd = CommonHerd()
    retrieved_animals = herd.retrieve_animal('rabbit', 10)
    assert retrieved_animals == 10
    assert herd.herd == {
        'rabbit': 50,
        'sheep': 24,
        'pig': 20,
        'cow': 12,
        'horse': 6,
        'small_dog': 4,
        'big_dog': 2
    }


def test_only_available_animals_are_retrieved_when_request_exceeds():
    from Game.Herd import CommonHerd
    herd = CommonHerd()
    retrieved_animals = herd.retrieve_animal('horse', 7)
    assert retrieved_animals == 6
    assert herd.herd == {
        'rabbit': 60,
        'sheep': 24,
        'pig': 20,
        'cow': 12,
        'horse': 0,
        'small_dog': 4,
        'big_dog': 2
    }


def test_animal_can_be_added_to_common_herd():
    from Game.Herd import CommonHerd
    herd = CommonHerd()
    herd.add_animals({'sheep': 3, 'big_dog': 2})
    assert herd.herd == {
        'rabbit': 60,
        'sheep': 27,
        'pig': 20,
        'cow': 12,
        'horse': 6,
        'small_dog': 4,
        'big_dog': 4
    }


def test_animal_can_be_added_to_player_herd():
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd.set_retrieve_animal_from_common_herd_callback(lambda x, y: y)
    herd.animal_came('sheep', 2)
    assert herd.herd == {
        'rabbit': 0,
        'sheep': 1,
        'pig': 0,
        'cow': 0,
        'horse': 0,
        'small_dog': 0,
        'big_dog': 0
    }


def test_available_animals_can_be_added_to_player_herd():
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals['cow'] = 6
    herd.set_retrieve_animal_from_common_herd_callback(lambda x, y: 2)
    herd.animal_came('cow')
    assert herd.herd == {
        'rabbit': 0,
        'sheep': 0,
        'pig': 0,
        'cow': 8,
        'horse': 0,
        'small_dog': 0,
        'big_dog': 0
    }


def test_wolf_eats_big_dog(common_herd_mock):
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 2, 'sheep': 3, 'pig': 4, 'cow': 5, 'horse': 6, 'small_dog': 7, 'big_dog': 2})
    herd.set_add_animal_to_common_herd_callback(common_herd_mock.add)
    herd.animal_came('wolf')
    assert herd.herd == {
        'rabbit': 2,
        'sheep': 3,
        'pig': 4,
        'cow': 5,
        'horse': 6,
        'small_dog': 7,
        'big_dog': 1
    }
    assert common_herd_mock.herd == {'big_dog': 1}


def test_wolf_eats_sheeps_pig_cows(common_herd_mock):
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 2, 'sheep': 3, 'pig': 4, 'cow': 5, 'horse': 6, 'small_dog': 7, 'big_dog': 0})
    herd.set_add_animal_to_common_herd_callback(common_herd_mock.add)
    herd.animal_came('wolf')
    assert herd.herd == {
        'rabbit': 2,
        'sheep': 0,
        'pig': 0,
        'cow': 0,
        'horse': 6,
        'small_dog': 7,
        'big_dog': 0
    }
    assert common_herd_mock.herd == {'sheep': 3, 'pig': 4, 'cow': 5}


def test_fox_eats_small_dog(common_herd_mock):
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 12, 'sheep': 3, 'pig': 4, 'cow': 5, 'horse': 6, 'small_dog': 3, 'big_dog': 2})
    herd.set_add_animal_to_common_herd_callback(common_herd_mock.add)
    herd.animal_came('fox')
    assert herd.herd == {
        'rabbit': 12,
        'sheep': 3,
        'pig': 4,
        'cow': 5,
        'horse': 6,
        'small_dog': 2,
        'big_dog': 2
    }
    assert common_herd_mock.herd == {'small_dog': 1}


def test_fox_eats_rabbits_except_one(common_herd_mock):
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 12, 'sheep': 3, 'pig': 4, 'cow': 5, 'horse': 6, 'small_dog': 0, 'big_dog': 2})
    herd.set_add_animal_to_common_herd_callback(common_herd_mock.add)
    herd.animal_came('fox')
    assert herd.herd == {
        'rabbit': 1,
        'sheep': 3,
        'pig': 4,
        'cow': 5,
        'horse': 6,
        'small_dog': 0,
        'big_dog': 2
    }
    assert common_herd_mock.herd == {'rabbit': 11}


def test_player_can_sell_animals(common_herd_mock):
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 15, 'sheep': 3, 'pig': 4, 'cow': 1, 'horse': 2, 'small_dog': 2, 'big_dog': 2})
    herd.set_add_animal_to_common_herd_callback(common_herd_mock.add)
    herd.sell_animals({'rabbit': 6, 'sheep': 1, 'pig': 2})
    assert herd.herd == {
        'rabbit': 9,
        'sheep': 2,
        'pig': 2,
        'cow': 1,
        'horse': 2,
        'small_dog': 2,
        'big_dog': 2
    }
    assert common_herd_mock.herd == {'rabbit': 6, 'sheep': 1, 'pig': 2}


def test_player_can_buy_only_available_animals():
    from Game.Herd import PlayerHerd
    herd = PlayerHerd()
    herd._animals.update({'rabbit': 15, 'sheep': 3, 'pig': 4, 'cow': 1, 'horse': 2, 'small_dog': 2, 'big_dog': 2})
    herd.set_retrieve_animal_from_common_herd_callback(lambda x, y: y - 1)
    herd.buy_animals({'cow': 2, 'pig': 5})
    assert herd.herd == {
        'rabbit': 15,
        'sheep': 3,
        'pig': 8,
        'cow': 2,
        'horse': 2,
        'small_dog': 2,
        'big_dog': 2
    }


@pytest.fixture()
def common_herd_mock():
    class CommonHerd:
        def __init__(self):
            self.herd = {}

        def add(self, animals):
            for animal, number in animals.items():
                self.herd[animal] = self.herd[animal] + number if animal in self.herd.keys() else number
    return CommonHerd()
