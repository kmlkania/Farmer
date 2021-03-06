from Game.Dice import Dice


def test_dice_can_be_rolled():
    green_dice = Dice(fields={'rabbit': 6, 'sheep': 3, 'pig': 1, 'cow': 1, 'wolf': 1})
    result = green_dice.roll_dice()
    assert result in ['rabbit', 'sheep', 'pig', 'cow', 'wolf']


def test_wolf_can_be_rolled_out():
    from random import seed
    seed(2)
    green_dice = Dice(fields={'rabbit': 6, 'sheep': 3, 'pig': 1, 'cow': 1, 'wolf': 1})
    result = green_dice.roll_dice()
    assert result == 'wolf'
