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
