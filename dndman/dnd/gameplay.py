class DiceRoll:
    __amount: int
    __dice_type: int

    def __init__(self, amount, dice_type):
        self.__amount = amount
        self.__dice_type = dice_type

    def get_amount(self) -> int:
        return self.__amount

    def get_dice_type(self) -> int:
        return self.__dice_type
