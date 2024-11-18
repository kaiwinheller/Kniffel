#Kniffel player


class Kniffel_Player():
    def __init__(self, name):
        "Name should be a string"
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' The player's choice on what dices to keep.
        Input:
        - scoreboard: A copy of the scoreboard with information about the game. (see Kniffel_Game.py file)
        Type: dict
        - kept_dices: A copy of the dice values, that are already kept from previous rolls
        Type: list
        - dice_rolls: A copy of the dice values just rolled, that have to be decided on, whether to keep or not to keep.
        Type: list
        - roll: The number of the roll. Either 0 (first roll) or 1 (second roll). After the third roll the dices are automatically kept
        Type: int

        Output:
        A list of the dice values, that want to be kept. Can also be an empty list.
        Beware: The list needs to only include valid sublists of dice_rolls. Otherwise no dices will be kept.
        '''
        pass
    
    def decide_which_field_to_enter(self, scoreboard, dice_values):
        ''' The player's choice on the field, they want to enter the points in.
        Input:
        - scoreboard: A copy of the scoreboard with information about the game. (see Kniffel_Game.py file)
        Type: dict
        - dice_values: A copy of the dice values, that are in front of you.
        Type: list

        Output:
        One of the following strings:
        "Einser"
        "Zweier"
        "Dreier"
        "Vierer"
        "Fünfer"
        "Sechser"
        "Dreierpasch"
        "Viererpasch"
        "Full House"
        "Kleine Straße"
        "Große Straße"
        "Kniffel"
        "Chance"
        If the field is already taken, or the output is not one of the following strings, 
        a random field that is not yet taken will be occupied with the number 0.
        '''
        pass