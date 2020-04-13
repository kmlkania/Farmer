from Herd import Herd


def test_animal_can_be_added_to_herd():
    herd = Herd()
    herd.add_animal('rabbit', 10)
    assert herd.rabbit == 10

