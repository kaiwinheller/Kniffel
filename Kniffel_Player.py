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
        total_rolls = kept_dices + dice_rolls
        field, score = self.check_for_best_score(total_rolls, scoreboard)
        
        if score >= 25:
            return dice_rolls
        else:
            return []
    
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
        best_field = self.check_for_best_score(dice_values, scoreboard)[0]
        return best_field
    
    def check_for_best_score(self, dice_values, scoreboard):

        # Initialize variables for best score and field
        best_score = -1
        best_field = ""

        # Define the scoring rules for each field
        fields = {
            "Einser": dice_values.count(1) * 1,
            "Zweier": dice_values.count(2) * 2,
            "Dreier": dice_values.count(3) * 3,
            "Vierer": dice_values.count(4) * 4,
            "Fünfer": dice_values.count(5) * 5,
            "Sechser": dice_values.count(6) * 6,
            "Dreierpasch": sum(dice_values) if max(dice_values.count(dice) for dice in dice_values) >= 3 else 0,
            "Viererpasch": sum(dice_values) if max(dice_values.count(dice) for dice in dice_values) >= 4 else 0,
            "Full House": 25 if len(set(dice_values)) == 2 and any(dice_values.count(dice) == 3 for dice in set(dice_values)) else 0,
            "Kleine Straße": 30 if any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])) else 0,
            "Große Straße": 40 if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values) else 0,
            "Kniffel": 50 if len(set(dice_values)) == 1 else 0,
            "Chance": sum(dice_values)  # Chance always takes the sum of the dice
        }

        # Iterate through the fields and find the one with the maximum score
        for field, score in fields.items():
            if score > best_score and scoreboard[self.name][field] == None:
                best_score = score
                best_field = field

        return best_field, best_score
    
class Kniffel_Player_2(Kniffel_Player):
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
        return []