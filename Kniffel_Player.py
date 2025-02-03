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

# Player_1 Priorisiert obere spalten, ist risikoscheu, 
class Ahrens_1(Kniffel_Player):
    def __init__(self, name):
        super().__init__(name)
        
    def first_decision(self, scoreboard, dice_rolls): # wird genutzt, wenn wir uns im ersten Wurf befinden oder noch keine Würfel behalten wurden       
    
        dices_numbers_we_want_to_keep = []
        
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        max_count_dice_roll_value = self.count_dices(dice_rolls)[1]
        max_count_dice_roll_key = self.count_dices(dice_rolls)[2]
        max_count_dice_roll_value_2 = self.count_dices(dice_rolls)[3]
        max_count_dice_roll_key_2 = self.count_dices(dice_rolls)[4]
        
        sample_for_road = self.following_numbers(scoreboard, dice_rolls)
        
        ### Der Würfelwurf kann theoretisch schon so eingetragen werden
        # Wenn ein Dreierpaar geworfen wurde und dieses noch nicht eingetragen ist
        if max_count_dice_roll_value >= 3 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        elif max_count_dice_roll_value_2 >= 3 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key_2]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value_2 * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # ansonsten prüfe ob ein Full House gewürfelt wurde
        elif scoreboard[self.name]["Full House"] == None and max_count_dice_roll_value == 3 and max_count_dice_roll_value_2 == 2 : 
            dices_numbers_we_want_to_keep += [max_count_dice_roll_key] * 3
            dices_numbers_we_want_to_keep += [max_count_dice_roll_key_2] * 2
            return dices_numbers_we_want_to_keep
        
        # Wenn eine Straße geworfen wurde, und noch keine eingetragen ist
        elif scoreboard[self.name]["Große Straße"] == None or scoreboard[self.name]["Kleine Straße"] == None:
            # Wenn eine Große Straße geworfen wurde
            if len(sample_for_road) == 5:
                dices_numbers_we_want_to_keep += sample_for_road
                return dices_numbers_we_want_to_keep
            # Wenn eine Kleine Straße geworfen wurde
            elif len(sample_for_road) == 4:
                dices_numbers_we_want_to_keep += sample_for_road
                return dices_numbers_we_want_to_keep
        
        ### versuche einen Teil der Würfel zu behalten um darauf aufzubauen
        
        # Behalte Würfel, die für die obere Hälfte (Einser, Zweier etc.) nützlich sind. Aber nur dann wenn sie noch nicht eingetragen wurden.
        if max_count_dice_roll_value >= 2 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte Würfel, die am zweit häufigsten geworfen wurden, aber nur dann wenn sie zwei mal vorkommen und die augenzahl noch nicht in der oberen Hälfte eingetragen ist            
        elif max_count_dice_roll_value_2 >= 2 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key_2]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value_2 * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # besteht die möglichkeit auf ein Full House?
        elif max_count_dice_roll_value  == 2 and max_count_dice_roll_value_2 == 2:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte die meist gewürfelten Augenzahl, wenn sie größer gleich 4 ist, um auf Kniffel zu gehen. Aber nur wenn noch kein Kniffel eingetragen ist.
        elif max_count_dice_roll_value >= 4 and scoreboard[self.name]["Kniffel"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte die meist geworfene Augenzahl, wenn sie größer gleich 3 ist, um auf Viererpasch zu gehen. Aber nur wenn noch kein Viererpasch eingetragen ist..
        elif max_count_dice_roll_value >= 3 and scoreboard[self.name]["Viererpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # ansonsten bahelte die meist geworfene Augenzahl, wenn sie größer gleich 2 ist, um auf Dreierpasch zu gehen. Aber nur wenn kein Dreierpasch eingetragen ist.
        elif max_count_dice_roll_value >= 2 and scoreboard[self.name]["Dreierpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        #Wenn ein Muster für eine Straße erkennbar ist (z. B. 3, 4,5), halte diese Würfel.
        elif len(sample_for_road) >= 3:
            dices_numbers_we_want_to_keep += sample_for_road
            return dices_numbers_we_want_to_keep
        
        # fallback, falls keine der moeglichkeiten eintritt
        return dices_numbers_we_want_to_keep
    
    
    
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        
        dices_numbers_we_want_to_keep = []
        
        count_dices_number = self.count_dices(dice_rolls)[0]
        max_count_dice_roll_value = self.count_dices(dice_rolls)[1]
        max_count_dice_roll_key = self.count_dices(dice_rolls)[2]        
        

        ### Wenn nur noch ein Feld frei ist:        
        last_dices = kept_dices + dice_rolls
        last_max_count_dice_roll_value = self.count_dices(last_dices)[1]
        last_max_count_dice_roll_key = self.count_dices(last_dices)[2] 
        count_fields = 0
        position = {
             "Einser":1,
             "Zweier":2,
             "Dreier":3,
             "Vierer":4,
             "Fünfer":5,
             "Sechser":6
             }
        count_last_dices = []
        for c in scoreboard[self.name]:
            if scoreboard[self.name][c] != None:
                count_fields += 1
            else:
                wanted_dice = c
        
        if count_fields == 12:
            # Wenn das Feld im oberen Teil liegt 
            if wanted_dice == 'Einser' or wanted_dice == 'Zweier' or wanted_dice == 'Dreier' or wanted_dice == 'Vierer' or wanted_dice == 'Fünfer' or wanted_dice == 'Sechser':
                for p in scoreboard[self.name]:
                    if scoreboard[self.name][p] == None:
                        for dice in last_dices:
                            if dice == position[p]:
                                count_last_dices.append(dice)
                dices_numbers_we_want_to_keep += count_last_dices
                return dices_numbers_we_want_to_keep    
            # Wenn das Feld ein Pasch oder Knifel ist:
            elif wanted_dice == 'Viererpasch' or wanted_dice == 'Dreierpasch' or wanted_dice == 'Kniffel':
                dices_numbers_we_want_to_keep += last_max_count_dice_roll_value * [last_max_count_dice_roll_key]
                return dices_numbers_we_want_to_keep
            else:
                return self.first_decision(scoreboard, last_dices)
                
                
        # wenn wir uns im ersten Wurf befinden
        elif roll == 0:   
            return self.first_decision(scoreboard, dice_rolls)
                            
        
        # wenn wir uns im zweiten Wurf befinden    
        elif roll == 1:
            
            new_dices = dice_rolls + kept_dices
            
            possible_entries_upper_part = self.get_possible_entries_upper_part()
            
            kept_max_count_dice_roll_value = self.count_dices(kept_dices)[1]
            kept_max_count_dice_roll_key = self.count_dices(kept_dices)[2]
            new_max_count_dice_roll_value = self.count_dices(new_dices)[1]
            new_max_count_dice_roll_key = self.count_dices(new_dices)[2]
                

            ## Wenn im ersten Wurf Würfel behalten wurden die für die obere Hälfte nützlich sind, oder als pasch/Kniffel verwendet werden können 
            # und es nun auf basis der würfel sinn ergibt drauf aufzubauen:   
            # wir stellen sicher dass die liste dices_numbers_we_want_to_keep nicht leer ist und
            # wir zählen mit .count wie oft die erste zahl in der liste vorkommt. Wenn das gleich der länge ist wissen wir, dass sich nur identische zahlen in der Liste befinden.
            if kept_dices and kept_dices.count(kept_dices[0]) == len(kept_dices):
                # Behalte Würfel, die die gleiche Augenzahl haben wie die, die schon behalten wurden.
                for k in count_dices_number.keys():
                    if k == kept_dices[0]:
                        if count_dices_number[k] >= 1:
                            dices_numbers_we_want_to_keep += [k] * count_dices_number[k]
                            return dices_numbers_we_want_to_keep
                        # Wenn im ersten Wurf Würfelpaare behalten wurden, nun jedoch kein weiterer Würfel dazu passt und ein besseres Würfelpaar existiert
                        elif new_max_count_dice_roll_value >= kept_max_count_dice_roll_value and new_max_count_dice_roll_key > kept_max_count_dice_roll_key and scoreboard[self.name][possible_entries_upper_part[new_max_count_dice_roll_key]] == None:
                            dices_numbers_we_want_to_keep += new_max_count_dice_roll_value * [new_max_count_dice_roll_key]
                            return dices_numbers_we_want_to_keep
                                                   
                    
                    # Wenn sich ein Full House ergeben hat und dieser noch nicht eingetragen wurde:
                    elif scoreboard[self.name]["Full House"] == None:
                        if len(kept_dices) == 3: 
                            if max_count_dice_roll_value == 2:
                                if k == max_count_dice_roll_key:
                                    dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
                                    return dices_numbers_we_want_to_keep
                        elif len(kept_dices) == 2:    
                            if max_count_dice_roll_value == 3:
                                if k == max_count_dice_roll_key:
                                    dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key]
                                    return dices_numbers_we_want_to_keep
                   
            
            ## Wenn im ersten wurf ein Straßenmuster behalten wurde (Würfel, die hintereinander folgen)
            # und es nun auf basis der würfel Sinn macht drauf aufzubauen:
            elif kept_dices and kept_dices == list(range(min(kept_dices), max(kept_dices) + 1)):
                for n in dice_rolls:
                    if n == min(kept_dices) - 1:
                        dices_numbers_we_want_to_keep.append(n)
                        dices_numbers_we_want_to_keep.sort()
                        return dices_numbers_we_want_to_keep
                        
                    elif n == max(kept_dices) + 1:
                        dices_numbers_we_want_to_keep.append(n)
                        dices_numbers_we_want_to_keep.sort()
                        return dices_numbers_we_want_to_keep

                        
                        
            ## Wenn im ersten Wurf kein würfel behalten wurde:
            elif not kept_dices:
                return self.first_decision(scoreboard, dice_rolls)
                        
            # fallback, falls keine der moeglichkeiten eintritt
            return dices_numbers_we_want_to_keep
                # ausblick für später: fallback & scorecard statistisch analysieren (z.b. durch debugging oder printing), 
                # um daraus mögliche fälle für zu behaltende würfel abzuleiten
            
    
    def decide_which_field_to_enter(self, scoreboard, dice_values):
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        max_count_dice_roll_value = self.count_dices(dice_values)[1]
        max_count_dice_roll_key = self.count_dices(dice_values)[2]
        found = self.count_dices(dice_values)[5]
        
        sample_for_road = self.following_numbers(scoreboard, dice_values)

        # Wenn Kniffel geworfen wurde:
        if max_count_dice_roll_value == 5 and scoreboard[self.name]["Kniffel"] == None:
            return 'Kniffel'
        # Wenn für den oberen Teil geworfen wurde. Es soll min. ein Dreierpasch sein
        elif max_count_dice_roll_value >= 3 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            return possible_entries_upper_part[max_count_dice_roll_key]
        # Wenn die zahl im oberen feld schon eingetragen wurde soll geguckt werden ob sie beim Viererpasch eingetragen weren kann:
        elif max_count_dice_roll_value == 4 and scoreboard[self.name]["Viererpasch"] == None:
            return "Viererpasch"
        # Wenn die zahl im oberen feld schon eingetragen wurde soll geguckt werden ob sie beim Dreierpasch eingetragen weren kann:
        elif max_count_dice_roll_value == 3 and scoreboard[self.name]["Dreierpasch"] == None:
            return "Dreierpasch"
        # Wenn FullHouse geworfen wurde:
        elif max_count_dice_roll_value == 3 and found == True and scoreboard[self.name]["Full House"] == None: 
            return "Full House"
        # Wenn eine Große Straße geworfen wurde:
        elif len(sample_for_road) == 5 and scoreboard[self.name]["Große Straße"] == None:
            return 'Große Straße'
        # Wenn eine Kleine Straße geworfen wurde:
        elif len(sample_for_road) == 4 and scoreboard[self.name]["Kleine Straße"] == None:
            return 'Kleine Straße'
        # Wenn ein einserpaar gewürfelt wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 1 and scoreboard[self.name]["Einser"] == None:
            return 'Einser'
        # Wenn eine einzelne Einz geworfen wurde:
        elif max_count_dice_roll_value == 1 and max_count_dice_roll_key == 1 and scoreboard[self.name]["Einser"] == None:
            return 'Einser'
        # Wenn ein Zweierpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 2 and scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        # Wenn eine einzelne Zwei geworfen wurde:
        elif max_count_dice_roll_value == 1 and max_count_dice_roll_key == 2 and scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        # Wenn keine von den vorherigen fällen eintritt geh auf Chance
        elif scoreboard[self.name]["Chance"] == None:
            return 'Chance'
        
        
        # Wenn Chance schon besetzt ist: Entscheidung welches feld gestrichen werden soll       
        elif scoreboard[self.name]["Kniffel"] == None:
            return 'Kniffel'   
        elif scoreboard[self.name]["Viererpasch"] == None:
            return 'Viererpasch'
        elif scoreboard[self.name]["Full House"] == None:
            return 'Full House'
        elif scoreboard[self.name]["Große Straße"] == None:
            return 'Große Straße'
        elif scoreboard[self.name]["Dreierpasch"] == None:
            return 'Dreierpasch'
        elif scoreboard[self.name]["Kleine Straße"] == None:
            return 'Kleine Straße'
        elif scoreboard[self.name]["Einser"] == None:
            return 'Einser' 
        elif scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        elif scoreboard[self.name]["Dreier"] == None:
            return 'Dreier'
        elif scoreboard[self.name]["Vierer"] == None:
            return 'Vierer'
        elif scoreboard[self.name]["Fünfer"] == None:
            return 'Fünfer'
        elif scoreboard[self.name]["Sechser"] == None:
            return 'Sechser'
        
        
# Priorisiert untere spalten
class Ahrens_2(Kniffel_Player):
    def __init__(self, name):
        super().__init__(name)
            


    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        
        new_dices = dice_rolls + kept_dices
        
        dices_numbers_we_want_to_keep = []
        
        possible_entries_upper_part = self.get_possible_entries_upper_part()
              
        max_count_dice_roll_value = self.count_dices(new_dices)[1]
        max_count_dice_roll_key = self.count_dices(new_dices)[2]
        max_count_dice_roll_value_2 = self.count_dices(new_dices)[3]
        max_count_dice_roll_key_2 = self.count_dices(new_dices)[4]
        
        sample_for_road = self.following_numbers(scoreboard, new_dices)
        
        ### Der würfelwurf kann theoretisch schon so eingetragen werden
        
        # Wenn ein Kniffel geworfen wurde
        if max_count_dice_roll_value == 5 and scoreboard[self.name]["Kniffel"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # Wenn eine Straße geworfen wurde, und noch keine eingetragen ist  
        elif scoreboard[self.name]["Große Straße"] == None or scoreboard[self.name]["Kleine Straße"] == None:
            # Wenn eine Große Straße geworfen wurde
            if len(sample_for_road) == 5:
                dices_numbers_we_want_to_keep += sample_for_road
                return dices_numbers_we_want_to_keep
            # Wenn eine Kleine Straße geworfen wurde
            elif len(sample_for_road) == 4:
                dices_numbers_we_want_to_keep += sample_for_road
                return dices_numbers_we_want_to_keep
            
        # Wenn ein Viererpasch geworfen wurde
        elif max_count_dice_roll_value == 4 and scoreboard[self.name]["Viererpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep 
        
        # ansonsten prüfe ob ein Full House gewürfelt wurde
        elif scoreboard[self.name]["Full House"] == None and max_count_dice_roll_value == 3 and max_count_dice_roll_value_2 == 2 : 
            dices_numbers_we_want_to_keep += [max_count_dice_roll_key] * 3
            dices_numbers_we_want_to_keep += [max_count_dice_roll_key_2] * 2
            return dices_numbers_we_want_to_keep
       
        # Wenn ein Dreierpasch geworfen wurde
        elif max_count_dice_roll_value == 3 and scoreboard[self.name]["Dreierpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        
        ### versuche einen Teil der Würfel zu behalten um darauf aufzubauen
        
        # Behalte die meist gewürfelten Augenzahl, wenn sie größer gleich 3 ist, um auf Kniffel zu gehen. Aber nur wenn noch kein Kniffel eingetragen ist.
        if max_count_dice_roll_value >= 3 and scoreboard[self.name]["Kniffel"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        #Wenn ein Muster für eine Straße erkennbar ist (z. B. 3, 4), halte diese Würfel.    
        elif len(sample_for_road) >= 2 and scoreboard[self.name]['Große Straße'] == None or scoreboard[self.name]['Kleine Straße'] == None:
            dices_numbers_we_want_to_keep += sample_for_road
            return dices_numbers_we_want_to_keep
            
        # ansonsten behalte die meist geworfene Augenzahl, wenn sie größer gleich 2 ist, um auf Viererpasch zu gehen. Aber nur wenn noch kein Viererpasch eingetragen ist..
        elif max_count_dice_roll_value >= 2 and scoreboard[self.name]["Viererpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # besteht die möglichkeit auf ein Full House?
        elif max_count_dice_roll_value  == 2 and max_count_dice_roll_value_2 == 2:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # ansonsten bahelte die meist geworfene Augenzahl, wenn sie größer gleich 2 ist, um auf Dreierpasch zu gehen. Aber nur wenn kein Dreierpasch eingetragen ist.
        elif max_count_dice_roll_value >= 2 and scoreboard[self.name]["Dreierpasch"] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte Würfel, die für die obere Hälfte (Einser, Zweier etc.) nützlich sind. Aber nur dann wenn sie noch nicht eingetragen wurden.
        elif max_count_dice_roll_value >= 2 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte Würfel, die am zweit häufigstengeworfen wurden, aber nur dann wenn sie zwei mal vorkommen und die augenzahl noch nicht in der oberen Hälfte eingetragen ist            
        elif max_count_dice_roll_value_2 == 2 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value_2 * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # ansonsten behalte einen einzelnen Würfel, der im oberen Teil noch nicht eingetragen ist
        elif max_count_dice_roll_value and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None: 
            dices_numbers_we_want_to_keep += max_count_dice_roll_value * [max_count_dice_roll_key] 
            return dices_numbers_we_want_to_keep
            
        elif max_count_dice_roll_value_2 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key_2]] == None:
            dices_numbers_we_want_to_keep += max_count_dice_roll_value_2 * [max_count_dice_roll_key_2]
            return dices_numbers_we_want_to_keep
        
        # fallback, falls keine der moeglichkeiten eintritt
        return dices_numbers_we_want_to_keep  

    
    def decide_which_field_to_enter(self, scoreboard, dice_values):
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        possible_entries_upper_part = self.get_possible_entries_upper_part()
        
        max_count_dice_roll_value = self.count_dices(dice_values)[1]
        max_count_dice_roll_key = self.count_dices(dice_values)[2]
        found = self.count_dices(dice_values)[5]
        
        sample_for_road = self.following_numbers(scoreboard, dice_values)
                
        # Entscheidung wann welches feld eingetragen werden soll:        
        # Wenn Kniffel geworfen wurde:
        if max_count_dice_roll_value == 5 and scoreboard[self.name]["Kniffel"] == None:
            return 'Kniffel'
        # Wenn eine Große Straße geworfen wurde:
        elif len(sample_for_road) == 5 and scoreboard[self.name]["Große Straße"] == None:
            return 'Große Straße'
        # Wenn eine Kleine Straße geworfen wurde:
        elif len(sample_for_road) == 4 and scoreboard[self.name]["Kleine Straße"] == None:
            return 'Kleine Straße'
        # Wenn Viererpasch geworfen wurde:
        elif max_count_dice_roll_value == 4 and scoreboard[self.name]["Viererpasch"] == None:
            return "Viererpasch"
        # Wenn FullHouse geworfen wurde:
        elif max_count_dice_roll_value == 3 and found == True and scoreboard[self.name]["Full House"] == None: 
            return "Full House"
        # Wenn Dreierpasch geworfen wurde:
        elif max_count_dice_roll_value == 3 and scoreboard[self.name]["Dreierpasch"] == None:
            return "Dreierpasch"
        # Wenn für den oberenteil geworfen wurde. Es soll min. ein Dreierpasch sein
        elif max_count_dice_roll_value >= 3 and scoreboard[self.name][possible_entries_upper_part[max_count_dice_roll_key]] == None:
            return possible_entries_upper_part[max_count_dice_roll_key]
        # wenn ein Einserpaar geworfen wurde
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 1 and scoreboard[self.name]["Einser"] == None:
            return 'Einser'
        # Wenn eine einzelne Einz geworfen wurde:
        elif max_count_dice_roll_value == 1 and max_count_dice_roll_key == 1 and scoreboard[self.name]["Einser"] == None:
            return 'Einser'
        # Wenn ein Zweierpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 2 and scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        # Wenn eine einzelne Zwei geworfen wurde:
        elif max_count_dice_roll_value == 1 and max_count_dice_roll_key == 2 and scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        # Wenn ein Dreierpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 3 and scoreboard[self.name]["Dreier"] == None:
            return 'Dreier'
        # Wenn ein Viererpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 4 and scoreboard[self.name]["Vierer"] == None:
            return 'Vierer'
        # Wenn ein Fünwerpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 5 and scoreboard[self.name]["Fünfer"] == None:
            return 'Fünfer'   
        # Wenn ein Sechserpaar geworfen wurde:
        elif max_count_dice_roll_value == 2 and max_count_dice_roll_key == 6 and scoreboard[self.name]["Sechser"] == None:
            return 'Sechser'
        # Wenn keine von den vorherigen fällen eintritt: geh auf Chance
        elif scoreboard[self.name]["Chance"] == None:
            return 'Chance'
        
        
        # Wenn kein Feld eingetragen werden konnte: 
        # Entscheidung welches feld gestrichen werden soll       
        
        elif scoreboard[self.name]["Einser"] == None:
            return 'Einser'
        elif scoreboard[self.name]["Zweier"] == None:
            return 'Zweier'
        elif scoreboard[self.name]["Dreier"] == None:
            return 'Dreier'
        elif scoreboard[self.name]["Vierer"] == None:
            return 'Vierer'
        elif scoreboard[self.name]["Fünfer"] == None:
            return 'Fünfer'
        elif scoreboard[self.name]["Sechser"] == None:
            return 'Sechser'
        elif scoreboard[self.name]["Dreierpasch"] == None:
            return 'Dreierpasch'
        elif scoreboard[self.name]["Full House"] == None:
            return 'Full House'
        elif scoreboard[self.name]["Viererpasch"] == None:
            return 'Viererpasch'
        elif scoreboard[self.name]["Kleine Straße"] == None:
            return 'Kleine Straße'
        elif scoreboard[self.name]["Große Straße"] == None:
            return 'Große Straße'
        elif scoreboard[self.name]["Kniffel"] == None:
            return 'Kniffel'        
        
        
        
class Falco_1(Kniffel_Player):
  def __init__(self, name):
      self.name = name
      self.current_round = 0
      self.total_rounds = 13

      # Core scoring values with priorities
      self.field_values = {
          "Kniffel": (50, 1),
          "Große Straße": (40, 2),
          "Full House": (25, 3),
          "Kleine Straße": (30, 4),
          "Viererpasch": (12, 5), # Angepasst von 0 auf 12
          "Dreierpasch": (9, 6), # Angepasst von 0 auf 9
          "Sechser": (6, 7),
          "Fünfer": (5, 8),
          "Vierer": (4, 9),
          "Dreier": (3, 10),
          "Zweier": (2, 11),
          "Einser": (1, 12),
          "Chance": (0, 13)
      }

  ####################################################################
  ### Haupt-Methoden ###
  ####################################################################
  ### decide_which_dices_to_hold - Auswahl der zu haltenen Würfel  ###
  def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
      """
      Entscheidet, welche Würfel der Spieler behalten sollte, basierend auf heuristischen Bewertungen.

      Diese Methode analysiert die aktuellen Würfel (sowohl bereits gehaltene als auch neu geworfene) und bestimmt, welche Würfel der Spieler für die nächsten Würfe behalten sollte. Das Ziel ist es, die besten Chancen auf eine hohe Punktzahl zu erzielen, indem mögliche Muster erkannt und deren erwarteter Wert berechnet werden.

      **Parameter:**
      - **self** (`Kniffel_Player`): Referenz auf die aktuelle Instanz der Klasse. In Python ist dies notwendig, um auf Methoden und Attribute der Klasse zuzugreifen.
      - **scoreboard** (`dict`): Ein Dictionary, das den aktuellen Punktestand enthält. Es zeigt, welche Felder bereits ausgefüllt wurden und welche noch frei sind.
      - **kept_dices** (`List[int]`): Eine Liste von Ganzzahlen, die die Würfelwerte darstellen, die der Spieler in den vorherigen Würfen behalten hat.
      - **dice_rolls** (`List[int]`): Eine Liste von Ganzzahlen, die die aktuellen Würfelwerte aus dem letzten Wurf darstellen.
      - **roll** (`int`): Die aktuelle Wurfnummer als Ganzzahl (0 für den ersten Wurf, 1 für den zweiten, etc.). Insgesamt sind bis zu drei Würfe erlaubt.

      **Wichtige verwendete Python-Konzepte:**
      - **Listenoperationen**: Mit dem `+` Operator können Listen zusammengeführt werden.
      - **Sets**: Mit der Funktion `set()` wird eine Menge erstellt, die nur einzigartige Elemente enthält.
      - **Kopieren von Objekten**: `copy.deepcopy()` erstellt eine tiefe Kopie eines Objekts, um unbeabsichtigte Änderungen am Original zu vermeiden.
      - **Methodenaufrufe innerhalb der Klasse**: Mit `self.method()` wird eine Methode der Klasse aufgerufen.
      - **Formatierte Strings (f-Strings)**: Erlauben die einfache Einbettung von Variablen in Strings.
      - **Lambda-Funktionen**: Anonyme Funktionen, die oft für kurze, einmalige Operationen verwendet werden.

      """
      # Kombiniere die gehaltenen Würfel und die neu geworfenen Würfel zu einer Liste aller aktuellen Würfel
      all_dice = kept_dices + dice_rolls  # '+' kombiniert zwei Listen zu einer

      # Zähle, wie oft jeder Würfelwert (1-6) in all_dice vorkommt
      counts = count_dice_numpy(all_dice)  # Nutzt eine externe Funktion zur effizienten Zählung mit NumPy

      # Erstelle ein Set aus all_dice, um doppelte Werte zu entfernen und nur einzigartige Würfelwerte zu erhalten
      dice_set = set(all_dice)  # set() erstellt eine Menge einzigartiger Elemente

      # Berechne, wie viele Würfe noch verbleiben (insgesamt 3 Würfe möglich)
      remaining_rolls = 2 - roll  # Subtrahiere die aktuelle Wurfnummer von der maximalen Anzahl an Würfen minus 1

      # Erstelle eine tiefe Kopie des Scoreboards, um das Original nicht zu verändern
      scoreboard_copy = copy.deepcopy(scoreboard)  # deepcopy kopiert alle Ebenen des Objekts

      # Analysiere den aktuellen Spielzustand basierend auf dem kopierten Scoreboard und den Würfelwerten
      game_state = self.analyze_game_state(scoreboard_copy, counts)  # Aktualisiert den Spielzustand
      self.game_state = game_state  # Speichert den Spielzustand in der Instanzvariable

      # Bewerte mögliche Muster und Strategien anhand heuristischer Methoden
      candidate_options = self.evaluate_patterns(
          dice_rolls, all_dice, counts, remaining_rolls, game_state, dice_set
      )  # Ruft eine Methode auf, die verschiedene Optionen bewertet

      # Ausgabe der Informationen für den Spieler
      print(f"\nRunde {self.current_round}, Wurf {roll+1}")  # f-String für formatierte Ausgabe
      print(f"Gehaltene Würfel: {kept_dices}, Gewürfelte Würfel: {dice_rolls}")  # Zeigt die aktuellen Würfel an
      print(f"Kandidatenoptionen:")  # Überschrift für die folgenden Optionen

      # Iteriere über die Kandidatenoptionen und gebe Details aus
      for option in candidate_options:
          # option[0]: Würfel, die gehalten werden sollen
          # option[1]: Erwarteter Wert dieser Option
          # option[2]: Beschreibendes Muster oder Strategie
          print(f"- Würfel zu halten: {option[0]}, Erwarteter Wert: {option[1]}, Muster: {option[2]}")

      # Überprüfe, ob Kandidatenoptionen vorhanden sind
      if candidate_options:
          # Wähle die Option mit dem höchsten erwarteten Wert
          chosen_option = max(candidate_options, key=lambda x: x[1])  # max() findet das Element mit dem größten x[1]
          print(f"Gewählte Aktion: Halte Würfel {chosen_option[0]} für Muster '{chosen_option[2]}'")
          return chosen_option[0]  # Gibt die Liste der zu haltenden Würfel zurück

      # Falls keine guten Optionen gefunden wurden, verwende eine Standardstrategie
      default_choice = self.default_holding_strategy(dice_rolls, game_state)  # Ruft die Standardstrategie auf
      print(f"Keine guten Optionen gefunden. Standardentscheidung: Halte Würfel {default_choice}")
      return default_choice  # Gibt die Standardauswahl der zu haltenden Würfel zurück

  ### decide_which_field_to_enter - Auswahl des zu füllenden Feldes ###
  def decide_which_field_to_enter(self, scoreboard_copy, dice_values):
      """
      Bestimmt, welches Feld im Scoreboard der Spieler basierend auf den aktuellen Würfelergebnissen ausfüllen soll.

      Diese Methode analysiert die aktuellen Würfelwerte und den aktuellen Spielzustand, um zu entscheiden, welches Feld 
      der Spieler in dieser Runde ausfüllen sollte. Sie bewertet mögliche Felder anhand ihrer potenziellen Punktwerte und wählt das Feld 
      mit dem höchsten erwarteten Wert aus. Falls keine geeigneten Felder gefunden werden, wird eine Standardentscheidung getroffen.

      Parameter:
          scoreboard_copy (dict): Eine Kopie des aktuellen Scoreboards, das die Punktstände des Spielers enthält.
          dice_values (list): Eine Liste der aktuellen Würfelwerte, die der Spieler geworfen hat.

      Rückgabewert:
          str oder None: Der Name des ausgewählten Feldes, das ausgefüllt werden soll. Gibt None zurück, wenn keine Würfelwerte vorhanden sind
                        oder keine freien Felder verfügbar sind.

      Verwendete Python-Syntax und -Konzepte:
          - Funktionen und Methoden: Definition und Aufruf von Methoden innerhalb einer Klasse.
          - Bedingte Anweisungen: Verwendung von if-else-Strukturen zur Entscheidungsfindung.
          - Listen und Dictionaries: Verarbeitung von Datenstrukturen zur Verwaltung von Würfelwerten und Feldbewertungen.
          - Schleifen: Iteration über Schlüssel-Wert-Paare in einem Dictionary.
          - F-Strings: Formatierte Zeichenketten zur Ausgabe von Informationen.
          - Funktionen aus anderen Modulen: Aufruf von extern definierten Funktionen wie count_dice_numpy.

      Beispiel:
          >>> spieler = Kniffel_Player("Max")
          >>> scoreboard = {...}  # Aktuelles Scoreboard
          >>> wurfel = [2, 3, 5, 5, 6]
          >>> ausgewaehltes_feld = spieler.decide_which_field_to_enter(scoreboard, wurfel)
          >>> print(ausgewaehltes_feld)
          "Full House"
      """
      # Überprüfen, ob es aktuelle Würfelwerte gibt
      if not dice_values:
          # Wenn keine Würfelwerte vorhanden sind, kann kein Feld ausgewählt werden
          return None

      # Zählen, wie oft jeder Würfelwert (1-6) in den aktuellen Würfeln vorkommt
      counts = count_dice_numpy(dice_values)

      # Analysieren des aktuellen Spielzustands basierend auf dem Scoreboard und den Würfelzahlen
      game_state = self.analyze_game_state(scoreboard_copy, counts)

      # Speichern des aktuellen Spielzustands in einer Instanzvariablen für späteren Gebrauch
      self.game_state = game_state

      # Bewerten der möglichen Feldoptionen basierend auf den aktuellen Würfeln und dem Spielzustand
      field_scores = self.evaluate_field_scores(dice_values, counts, game_state)

      # Ausgabe zur Nachverfolgung der Entscheidungen des Spielers
      print(f"\nEntscheidung, welches Feld zu füllen:")
      print(f"Endgültige Würfel: {dice_values}")
      print(f"Verfügbare Felder: {game_state['free_fields']}")
      print(f"Feldbewertungen:")

      # Iteration über alle bewerteten Felder und Ausgabe ihrer Punktwerte
      for field, score in field_scores.items():
          print(f"- Feld: {field}, Score: {score}")

      # Überprüfen, ob es bewertete Felder gibt
      if field_scores:
          # Auswählen des Feldes mit dem höchsten Punktwert
          chosen_field = max(field_scores.items(), key=lambda x: x[1])[0]
          print(f"Gewähltes Feld: {chosen_field}")
          return chosen_field

      # Falls keine guten Feldbewertungen vorhanden sind, eine Standardentscheidung treffen
      fallback_field = self.select_fallback_field(game_state["free_fields"])
      if fallback_field:
          print(f"Keine guten Felder. Standardentscheidung: Wähle Feld '{fallback_field}'")
          return fallback_field
      else:
          # Wenn keine freien Felder mehr verfügbar sind, keine Aktion durchführen
          print("Keine freien Felder mehr verfügbar.")
          return None

  ####################################################################
  ### Helper functions decide_which_dices_to_hold ###
  ####################################################################
  def evaluate_patterns(self, dice_rolls, all_dice, counts, remaining_rolls, game_state, dice_set):
      """
      Diese Methode bewertet die möglichen Würfelkombinationen basierend auf den aktuellen Würfelergebnissen und dem Spielzustand. 
      Sie erstellt eine Liste von Kandidaten, die die besten Optionen darstellen, um bestimmte Muster (z.B. Kniffel, Full House, Straßen) zu erzielen. 
      Dabei werden heuristische Entscheidungen getroffen, um die Würfel zu wählen, die behalten werden sollten.

      **Parameter:**
      - `dice_rolls` (Liste von int): Die aktuellen Würfelwerte, die der Spieler nach dem letzten Wurf erhalten hat.
      - `all_dice` (Liste von int): Alle Würfelwerte im Spiel, einschließlich derjenigen, die bereits gehalten werden.
      - `counts` (numpy.ndarray von int): Ein Array, das zählt, wie oft jede Würfelzahl (1 bis 6) in `all_dice` vorkommt.
      - `remaining_rolls` (int): Die Anzahl der verbleibenden Würfe, die der Spieler in dieser Runde noch hat.
      - `game_state` (Dictionary): Ein Wörterbuch, das den aktuellen Zustand des Spiels enthält, einschließlich der verfügbaren (freien) Felder und ob der Bonus im oberen Abschnitt erreichbar ist.
      - `dice_set` (Set von int): Eine Menge, die die einzigartigen Würfelwerte aus `all_dice` enthält.

      **Rückgabewert:**
      - `candidates` (Liste von Tupeln): Eine Liste von Kandidaten, wobei jeder Kandidat ein Tupel aus:
          - `dice_to_keep` (Liste von int): Die Würfelwerte, die behalten werden sollten.
          - `expected_value` (float): Der erwartete Wert oder Nutzen dieser Wahl.
          - `pattern_name` (str): Der Name des Musters, das angestrebt wird (z.B. "Kniffel", "Große Straße").

      **Beschreibung:**
      Die Methode durchläuft verschiedene mögliche Muster im Kniffel-Spiel und prüft, basierend auf den aktuellen Würfeln und dem Spielzustand, welche Muster erreichbar sind. Für jedes mögliche Muster werden Bedingungen geprüft und entsprechende Kandidaten erstellt, die dem Spieler helfen sollen, die beste Entscheidung zu treffen. Dabei werden folgende Muster berücksichtigt:

      1. **Kniffel**: Fünf gleiche Würfel.
      2. **Full House**: Eine Kombination aus einem Drilling und einem Paar.
      3. **Straßen**: Kleine Straße (vier aufeinanderfolgende Zahlen) und Große Straße (fünf aufeinanderfolgende Zahlen).
      4. **Paschs**: Dreierpasch und Viererpasch.
      5. **Oberer Bereich**: Einser bis Sechser, um den Bonus zu erreichen.
      6. **Chance**: Summe aller Würfelaugen.

      Die Methode verwendet grundlegende Python-Strukturen wie Listen, Dictionaries, Schleifen (`for`-Schleifen), Bedingungen (`if`-Statements) und Funktionen aus Bibliotheken wie `numpy` für numerische Berechnungen.

      **Beispielaufruf:**
      ```python
      candidates = self.evaluate_patterns(
          dice_rolls=[1, 2, 3],
          all_dice=[1, 2, 3, 4, 5],
          counts=np.array([1, 1, 1, 1, 1, 0]),
          remaining_rolls=2,
          game_state={"free_fields": ["Kniffel", "Full House"], "bonus_reachable": True},
          dice_set={1, 2, 3, 4, 5}
      )
      ```
      """

      # Initialisierung einer leeren Liste für die Kandidaten
      candidates = []

      # Abrufen der verfügbaren Felder aus dem Spielzustand
      free_fields = game_state["free_fields"]

      # Überprüfung auf bestimmte Muster wie Full House, kleine und große Straße
      is_full_house, has_small_straight, has_large_straight = check_patterns(counts, dice_set)

      ############################################################################
      # 1) Kniffel
      ############################################################################
      # Prüfung, ob das Feld "Kniffel" noch frei ist
      if "Kniffel" in free_fields:
          # Bestimmen der höchsten Anzahl gleicher Würfel
          max_count = np.max(counts)
          # Strategische Entscheidung basierend auf der Anzahl verbleibender Würfe
          # Wenn noch 2 Würfe übrig sind, reichen 3 gleiche Würfel
          # Wenn noch 1 Wurf übrig ist, sollten es mindestens 4 gleiche Würfel sein
          if (remaining_rolls == 2 and max_count >= 3) or (remaining_rolls == 1 and max_count >= 4):
              # Ermitteln des Würfelwertes mit der höchsten Häufigkeit
              value = get_highest_dice(counts)
              # Auswahl der Würfel, die diesen Wert haben und behalten werden sollen
              dice_to_keep = [d for d in dice_rolls if d == value]
              # Berechnung des erwarteten Wertes für den Kniffel
              expected_value = self.calculate_pattern_score(50, "Kniffel", remaining_rolls)
              # Hinzufügen des Kandidaten zur Liste
              candidates.append(
                  (dice_to_keep, expected_value, "Kniffel")
              )

      ############################################################################
      # 2) Full House (ausgelagert in eigene Methode)
      ############################################################################
      # Prüfung, ob das Feld "Full House" noch frei ist
      if "Full House" in free_fields:
          # Aufrufen der Methode zur Bewertung von Full House Szenarien
          full_house_options = self.evaluate_full_house_scenarios(
              counts, dice_rolls, all_dice, remaining_rolls, game_state
          )
          # Hinzufügen der gefundenen Optionen zu den Kandidaten
          candidates.extend(full_house_options)

      ############################################################################
      # 3) Straßen (Große / Kleine Straße)
      ############################################################################
      # Prüfung, ob die Felder für Große oder Kleine Straße noch frei sind
      if "Große Straße" in free_fields or "Kleine Straße" in free_fields:
          # Definieren der möglichen Straßenkombinationen
          straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
          # Durchlaufen der möglichen Straßen
          for straight in straights:
              # Finden der gemeinsamen Elemente zwischen der Straße und den aktuellen Würfeln
              matches = set(straight) & dice_set
              # Wenn mindestens 3 gemeinsame Zahlen vorhanden sind
              if len(matches) >= 3:
                  # Änderung: Nur eindeutige Würfelwerte behalten
                  unique_matches = []
                  for d in dice_rolls:
                      if d in matches and d not in unique_matches:
                          unique_matches.append(d)
                  if len(matches) == 5 and "Große Straße" in free_fields:
                      expected_value = self.calculate_pattern_score(40, "Große Straße", remaining_rolls)
                      candidates.append(
                          (unique_matches, expected_value, "Große Straße")
                      )
                  elif "Kleine Straße" in free_fields:
                      expected_value = self.calculate_pattern_score(30, "Kleine Straße", remaining_rolls)
                      candidates.append(
                          (unique_matches, expected_value, "Kleine Straße")
                      )

      ############################################################################
      # 4) Pasch-Felder (Dreierpasch / Viererpasch) -> Scoreboard-Felder
      ############################################################################
      # Vorhandene Logik für Felder "Dreierpasch" und "Viererpasch".
      for pasch_type in ["Viererpasch", "Dreierpasch"]:
          if pasch_type in free_fields:
              required = 4 if pasch_type == "Viererpasch" else 3
              if np.max(counts) >= required - remaining_rolls:
                  value = get_highest_dice(counts)
                  dice_to_keep = [d for d in dice_rolls if d == value]
                  expected_value = self.calculate_pattern_score(np.sum(all_dice), pasch_type, remaining_rolls)
                  candidates.append((dice_to_keep, expected_value, pasch_type))

      ############################################################################
      # 5) NEU: Erkennung von OnePair / ThreeOfAKind / FourOfAKind (unabhängig vom Feld)
      ############################################################################
      # a) FourOfAKind (4 gleiche Würfel) -> evtl. "Potential-Vierer"
      if np.max(counts) == 4:
          value = get_highest_dice(counts)
          dice_to_keep = [d for d in dice_rolls if d == value]
          # z.B. 22 als Basis, je nach Summe oder reiner Heuristik
          base_points = 22
          expected_value = self.calculate_pattern_score(base_points, "FourOfAKind", remaining_rolls)
          candidates.append((dice_to_keep, expected_value, "FourOfAKind"))

      # b) ThreeOfAKind (3 gleiche Würfel) -> evtl. "Potential-Dreier"
      elif np.max(counts) == 3:
          value = get_highest_dice(counts)
          dice_to_keep = [d for d in dice_rolls if d == value]
          # z.B. 18 als Basis
          base_points = 18
          expected_value = self.calculate_pattern_score(base_points, "ThreeOfAKind", remaining_rolls)
          candidates.append((dice_to_keep, expected_value, "ThreeOfAKind"))

      # c) OnePair (2 gleiche Würfel) -> evtl. "Potential-Pair"
      #     Gerade im 1. Wurf interessant, um auf Full House, 3er/4er etc. zu gehen.
      elif np.max(counts) == 2:
          value = get_highest_dice(counts)
          dice_to_keep = [d for d in dice_rolls if d == value]
          # Z.B. 10 als Basis
          base_points = 10
          expected_value = self.calculate_pattern_score(base_points, "OnePair", remaining_rolls)
          candidates.append((dice_to_keep, expected_value, "OnePair"))

      ############################################################################
      # 6) Oberer Bereich (Einser bis Sechser)
      ############################################################################
      if game_state["bonus_reachable"]:
          for number in range(6, 0, -1):
              field = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"][number-1]
              if field in free_fields:
                  current_count = counts[number-1]
                  if current_count >= max(2, 3 - remaining_rolls):
                      dice_to_keep = [d for d in dice_rolls if d == number]
                      # "Upper_<field>" als Pattern, damit wir Bonus-Logik in calculate_pattern_score anwenden können
                      expected_value = self.calculate_pattern_score(number * current_count, f"Upper_{field}", remaining_rolls)
                      candidates.append((dice_to_keep, expected_value, field))

      ############################################################################
      # 6) Chance
      ############################################################################
      # Prüfung, ob das Feld "Chance" noch frei ist
      if "Chance" in free_fields:
          # Berechnen der Summe aller aktuellen Würfelaugen
          total = np.sum(all_dice)
          # Berechnung des erwarteten Wertes für die Chance
          expected_value = self.calculate_pattern_score(total, "Chance", remaining_rolls)
          # Alle aktuellen Würfel werden behalten
          dice_to_keep = dice_rolls.copy()
          # Hinzufügen des Kandidaten zur Liste
          candidates.append(
              (dice_to_keep, expected_value, "Chance")
          )

      # Rückgabe der Liste der Kandidaten
      return candidates

  def evaluate_full_house_scenarios(self, counts, dice_rolls, all_dice, remaining_rolls, game_state):
      """
      Bewertet mögliche Full House Szenarien basierend auf den aktuellen Würfelergebnissen.

      **Beschreibung:**
      Diese Methode prüft verschiedene Würfelkombinationen, um festzustellen, ob ein Full House oder ähnliche Muster gebildet werden können. Sie erstellt eine Liste von Szenarien, die dem Spieler helfen sollen, die beste Strategie zu wählen, um ein Full House zu erreichen.

      **Parameter:**
      - `counts` (*numpy.ndarray von int*): Ein Array der Länge 6, das zählt, wie oft jede Augenzahl (1 bis 6) in den aktuellen Würfeln vorkommt.
      - `dice_rolls` (*List[int]*): Eine Liste der aktuellen Würfelwerte (noch nicht gehaltene Würfel).
      - `all_dice` (*List[int]*): Eine Liste aller aktuellen Würfelwerte, einschließlich der bereits gehaltenen Würfel.
      - `remaining_rolls` (*int*): Die Anzahl der verbleibenden Würfe in dieser Runde.
      - `game_state` (*dict*): Ein Wörterbuch, das den aktuellen Zustand des Spiels enthält (z.B. verfügbare Felder, Bonusinformationen).

      **Rückgabewert:**
      - `scenarios` (*List[Tuple[List[int], float, str]]*): Eine Liste von möglichen Szenarien. Jedes Szenario ist ein Tupel bestehend aus:
          - `dice_to_keep` (*List[int]*): Die Würfelwerte, die behalten werden sollen.
          - `expected_value` (*float*): Der erwartete Wert dieses Szenarios.
          - `description` (*str*): Eine beschreibende Bezeichnung des Szenarios.

      **Verwendete Python-Konzepte:**
      - **Bedingte Anweisungen (`if`-Statements)**: Zur Entscheidungsfindung basierend auf Würfelmustern.
      - **NumPy-Funktionen**: Für effiziente numerische Berechnungen und Array-Manipulationen.
      - **List Comprehensions**: Für die kompakte Erstellung von Listen.
      - **Array-Operationen mit `np.where` und `np.sort`**: Zum Finden von Indizes und Sortieren von Arrays.
      - **Kommentare**: Zur Erklärung von Codeabschnitten und Logik.

      **Details der Prüfung:**
      Die Methode untersucht folgende Szenarien:
      1. **Full House - Komplett**: Ein Drilling und ein Paar vorhanden ([3, 2]).
      2. **Vierling**: Vier gleiche Würfel vorhanden ([4, 1]).
      3. **Drilling**: Ein Drilling und zwei einzelne Würfel vorhanden ([3, 1, 1]).
      4. **Zwei Paare**: Zwei Paare und ein einzelner Würfel vorhanden ([2, 2, 1]).
      5. **Ein Paar**: Ein Paar und drei einzelne Würfel vorhanden ([2, 1, 1, 1]).

      """

      scenarios = []  # Initialisierung einer leeren Liste für die möglichen Szenarien

      # Sortieren der Zählungen in absteigender Reihenfolge, um die Würfelmuster zu erkennen
      sorted_counts = np.sort(counts)[::-1]  # Beispiel: [3, 2, 0, 0, 0, 0]

      # Szenario 1: Drilling und Paar (Full House komplett)
      if sorted_counts[0] == 3 and sorted_counts[1] == 2:
          # Finden des Index für den Drilling (Wert des Drillings)
          triple_idx = np.where(counts == 3)[0][0]
          triple_val = triple_idx + 1  # Korrektur, da Indizes bei 0 beginnen
          # Finden des Index für das Paar (Wert des Paares)
          pair_idx = np.where(counts == 2)[0][0]
          pair_val = pair_idx + 1
          # Berechnen des erwarteten Wertes für dieses Szenario
          expected_value = self.calculate_pattern_score(25, "FH_Complete", remaining_rolls)
          # Zusammenstellen der Würfel, die behalten werden sollen
          dice_to_keep = [d for d in dice_rolls if d == triple_val or d == pair_val]
          # Hinzufügen des Szenarios zur Liste
          scenarios.append(
              (dice_to_keep, expected_value, "FH_Complete")
          )

      # Szenario 2: Vierling ([4, 1])
      if sorted_counts[0] == 4:
          # Finden des Index für den Vierling (Wert des Vierlings)
          four_idx = np.where(counts == 4)[0][0]
          four_val = four_idx + 1
          # Berechnen des erwarteten Wertes für dieses Szenario
          expected_value = self.calculate_pattern_score(25, "FH_FourofaKind", remaining_rolls)
          # Zusammenstellen der Würfel, die behalten werden sollen
          dice_to_keep = [d for d in dice_rolls if d == four_val]
          # Hinzufügen des Szenarios zur Liste
          scenarios.append(
              (dice_to_keep, expected_value, "FH_FourofaKind")
          )

      # Szenario 3: Drilling ([3, 1, 1]) und noch Würfe übrig
      if sorted_counts[0] == 3 and remaining_rolls > 0:
          # Finden des Index für den Drilling
          triple_idx = np.where(counts == 3)[0][0]
          triple_val = triple_idx + 1
          # Berechnen des erwarteten Wertes für dieses Szenario
          expected_value = self.calculate_pattern_score(20, "FH_ThreeofaKind", remaining_rolls)
          # Zusammenstellen der Würfel, die behalten werden sollen
          dice_to_keep = [d for d in dice_rolls if d == triple_val]
          # Hinzufügen des Szenarios zur Liste
          scenarios.append(
              (dice_to_keep, expected_value, "FH_ThreeofaKind")
          )

      # Szenario 4: Zwei Paare ([2, 2, 1]) und noch Würfe übrig
      if sorted_counts[0] == 2 and sorted_counts[1] == 2 and remaining_rolls > 0:
          # Finden der Indizes für die Paare
          pair_indices = np.where(counts == 2)[0] + 1  # +1, um von Index auf Würfelwert zu kommen
          # Berechnen des erwarteten Wertes für dieses Szenario
          expected_value = self.calculate_pattern_score(15, "FH_TwoPairs", remaining_rolls)
          # Zusammenstellen der Würfel, die behalten werden sollen
          dice_to_keep = [d for d in dice_rolls if d in pair_indices]
          # Hinzufügen des Szenarios zur Liste
          scenarios.append(
              (dice_to_keep, expected_value, "FH_TwoPairs")
          )

      # Szenario 5: Ein Paar ([2, 1, 1, 1]) und noch Würfe übrig
      if sorted_counts[0] == 2 and remaining_rolls > 0:
          # Finden des Index für das Paar
          pair_idx = np.where(counts == 2)[0][0]
          pair_val = pair_idx + 1
          # Berechnen des erwarteten Wertes für dieses Szenario
          expected_value = self.calculate_pattern_score(10, "FH_OnePair", remaining_rolls)
          # Zusammenstellen der Würfel, die behalten werden sollen
          dice_to_keep = [d for d in dice_rolls if d == pair_val]
          # Hinzufügen des Szenarios zur Liste
          scenarios.append(
              (dice_to_keep, expected_value, "FH_OnePair")
          )

      # Rückgabe der gesammelten Szenarien
      return scenarios

  def default_holding_strategy(self, dice_rolls, game_state):
      """
      Verbessert die Standardstrategie, wenn keine klaren Muster verfügbar sind.

      **Beschreibung:**
      Diese Methode entscheidet, welche Würfel der Spieler behalten sollte, wenn keine offensichtlichen Muster oder Strategien zur Verfügung stehen. Die Strategie basiert darauf, die häufigsten Würfelwerte zu identifizieren und diese zu behalten, um die Chancen auf bessere Kombinationen in zukünftigen Würfen zu erhöhen. Wenn keine mehrfach vorkommenden Würfelwerte vorhanden sind, wird der höchste Würfelwert oder die beiden höchsten Würfelwerte behalten, um die Möglichkeit auf hohe Einzelwertungen zu maximieren.

      **Parameter:**
      - `dice_rolls` (*List[int]*): Eine Liste der aktuellen Würfelwerte, die der Spieler geworfen hat.
      - `game_state` (*dict*): Ein Wörterbuch, das den aktuellen Zustand des Spiels enthält, einschließlich Informationen wie verfügbare Felder und Bonusmöglichkeiten.

      **Rückgabewert:**
      - *List[int]*: Eine Liste der Würfelwerte, die der Spieler behalten sollte. Gibt eine leere Liste zurück, wenn keine Würfel vorhanden sind.

      **Verwendete Python-Konzepte:**
      - **NumPy-Operationen**: Verwendung von `numpy` für effiziente numerische Berechnungen.
      - **Bedingte Anweisungen (`if`-Statements)**: Zur Entscheidungsfindung basierend auf den Würfelwerten und ihrer Häufigkeit.
      - **List Comprehensions**: Für die Erstellung von Listen basierend auf bestimmten Bedingungen.

      **Details der Strategie:**
      - **Mehrfach vorkommende Würfelwerte:** Wenn mindestens zwei gleiche Würfel vorhanden sind (`max_count >= 2`), werden diese Würfel behalten. Dies erhöht die Wahrscheinlichkeit, in den nächsten Würfen Kombinationen wie Paare, Drillinge oder sogar einen Kniffel zu erreichen.
      - **Einzelne hohe Würfelwerte:** Wenn keine Würfel mehrfach vorkommen, werden die höchsten Würfelwerte behalten. Dies ist besonders nützlich, um hohe Punktzahlen in Feldern wie "Sechser" oder "Chance" zu erzielen.
      - **Flexibilität:** Die Strategie ist darauf ausgelegt, flexibel auf unterschiedliche Spielsituationen zu reagieren, insbesondere in frühen Phasen des Spiels, in denen noch viele Optionen offen sind.

      **Beispiel:**
      ```
      dice_rolls = [2, 4, 5, 5, 6]
      -> counts = [0, 1, 0, 1, 2, 1]
      -> max_count = 2 (für die Zahl 5)
      -> Rückgabe: [5, 5]
      ```
      """
      if not dice_rolls:
          return []  # Wenn keine Würfel vorhanden sind, gibt eine leere Liste zurück

      # Zähle, wie oft jeder Würfelwert (1-6) in den aktuellen Würfeln vorkommt
      counts = count_dice_numpy(dice_rolls)
      max_count = np.max(counts)  # Bestimmt die maximale Häufigkeit eines Würfelwertes
      number = np.argmax(counts) + 1  # Bestimmt den Würfelwert mit der höchsten Häufigkeit (1-basiert)

      # Verwende max_count, um die Strategie anzupassen
      if max_count >= 2:
          # Wenn es mindestens zwei gleiche Würfel gibt, halte diese
          return [d for d in dice_rolls if d == number]
      else:
          # Ansonsten halte die beiden höchsten Würfel
          sorted_dice = sorted(dice_rolls, reverse=True)
          highest_dice = sorted_dice[:2]
          return highest_dice

  ####################################################################
  ### Dynamische Anpassung der Strategie auf Basis des Spielverlauf###
  ####################################################################
  def analyze_game_state(self, scoreboard, counts):
      """
      Verbessert die Analyse des Spielzustands unter Verwendung von NumPy-Operationen mit ordnungsgemäßer Fehlerbehandlung.

      **Beschreibung:**
      Diese Methode analysiert den aktuellen Spielstand des Spielers und berechnet verschiedene Metriken, um den Fortschritt und die Punktestände zu bewerten. Sie berücksichtigt die Punktestände aller Spieler, den aktuellen Punktestand des Spielers und die verbleibenden Felder, um strategische Entscheidungen zu treffen.

      **Parameter:**
      - `scoreboard` (*dict*): Ein Wörterbuch, das die Punktestände aller Spieler enthält. Die Schlüssel sind die Spielernamen, und die Werte sind Dictionaries, die die Punktestände für jedes Feld enthalten.
      - `counts` (*numpy.ndarray von int*): Ein Array, das zählt, wie oft jede Augenzahl (1 bis 6) in den aktuellen Würfeln vorkommt.

      **Rückgabewert:**
      - *dict*: Ein Wörterbuch, das den aktuellen Zustand des Spiels enthält, einschließlich:
          - `free_fields` (*List[str]*): Eine Liste der Felder, die noch nicht ausgefüllt sind.
          - `progress` (*float*): Der Fortschritt des Spiels als Verhältnis
          - `score_diff` (*int*): Der Punktedifferenz zwischen dem Spieler und dem besten Gegner.
          - `bonus_missing` (*int*): Die Punkte, die benötigt werden, um den Bonus im oberen Bereich zu erreichen.
          - `bonus_reachable` (*bool*): Gibt an, ob der Bonus erreichbar ist.
          - `bonus_urgency` (*float*): Ein Wert, der angibt, wie dringend der Bonus erreicht werden muss.
          - `needs_high_scores` (*bool*): Gibt an, ob der Spieler hohe Punktzahlen benötigt.
          - `endgame` (*bool*): Gibt an, ob sich das Spiel im Endspiel befindet.
          - `catch_up_mode` (*bool*): Gibt an, ob der Spieler aufholen muss.
          - `catch_up_urgency` (*float*): Ein Wert, der angibt, wie dringend der Spieler aufholen muss.
          - `remaining_upper` (*List[str]*): Eine Liste der Felder im oberen Bereich, die noch nicht ausgefüllt sind.
          - `current_upper` (*int*): Die aktuelle Punktzahl im oberen Bereich.

      **Verwendete Python-Konzepte:**
      - **NumPy-Operationen**: Für effiziente Berechnungen und Array-Manipulationen.
      - **Bedingte Anweisungen (`if`-Statements)**: Zur Entscheidungsfindung basierend auf den Punkteständen.
      - **Listen- und Dictionary-Verarbeitung**: Zur Verwaltung von Punkteständen und Spielinformationen.

      **Details der Analyse:**
      Die Methode berechnet den Fortschritt des Spielers, die Punktedifferenz zu den Gegnern und die Erreichbarkeit des Bonus im oberen Bereich. Sie gibt eine umfassende Analyse des aktuellen Spielzustands zurück, die für strategische Entscheidungen verwendet werden kann.

      """
      # Berechne den Fortschritt und die Punktestände
      self.current_round = sum(1 for score in scoreboard[self.name].values()
                               if score is not None)  # Zählt die Runden, die der Spieler bereits gespielt hat
      progress = self.current_round / self.total_rounds  # Berechnet den Fortschritt als Verhältnis

      # Punktanalyse
      player_scores = np.array([
          sum(score for score in scores.values() if score is not None)  # Summiert die Punkte des Spielers
          for player, scores in scoreboard.items()
      ])
      player_index = list(scoreboard.keys()).index(self.name)  # Bestimmt den Index des aktuellen Spielers
      player_score = player_scores[player_index]  # Punktestand des aktuellen Spielers

      # Sichere Handhabung der Punktestände der Gegner
      opponent_scores = player_scores[player_scores != player_score]  # Punktestände der Gegner
      max_opponent_score = np.max(opponent_scores) if opponent_scores.size > 0 else 0  # Höchster Punktestand der Gegner
      score_diff = player_score - max_opponent_score  # Punktedifferenz zwischen dem Spieler und dem besten Gegner

      # Berechnung der Dringlichkeit, aufzuholen
      if score_diff < -20:
          catch_up_urgency = 1 + (abs(score_diff) / 40)  # Berechnet die Dringlichkeit, aufzuholen
      else:
          catch_up_urgency = 1

      upper_fields = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]  # Felder im oberen Bereich
      current_upper = sum(scoreboard[self.name][f] or 0 for f in upper_fields)  # Aktueller Punktestand im oberen Bereich
      remaining_upper = [f for f in upper_fields if scoreboard[self.name][f] is None]  # Verbleibende Felder im oberen Bereich
      bonus_missing = max(0, 63 - current_upper)  # Punkte, die benötigt werden, um den Bonus zu erreichen

      # Überprüfen, ob der Bonus erreichbar ist
      if remaining_upper:
          # 1) Berechne das Gesamt-Potenzial für alle noch freien oberen Felder
          total_potential = 0
          for field in remaining_upper:
              # Wandle Feldname ("Einser", "Zweier", etc.) in die entsprechende Zahl um
              number = {"Einser": 1, "Zweier": 2, "Dreier": 3,
                        "Vierer": 4, "Fünfer": 5, "Sechser": 6}[field]
              # Annahme: In 3 Würfen kann die Zahl bis zu 3-mal erzielt werden
              total_potential += number * 3

          # 2) Berechne den durchschnittlichen Potenzialwert pro Feld
          potential_per_field = total_potential / len(remaining_upper)

          avg_needed = bonus_missing / len(remaining_upper)
          bonus_reachable = avg_needed <= potential_per_field
      else:
          bonus_reachable = False

      # Berechnung der Bonus-Dringlichkeit
      if bonus_reachable:
          bonus_urgency = 1 + (progress * 0.5)
      else:
          bonus_urgency = 0

      # Berechnung der Bonusdringlichkeit
      bonus_urgency = 1 + (progress * 0.5) if bonus_reachable else 0
      catch_up_urgency = 1 + (abs(min(0, score_diff)) / 40)  # Dringlichkeit, aufzuholen

      # Debug-Ausgabe zur Überprüfung der Berechnungen
      print(f"progress: {progress}, current_upper: {current_upper}, bonus_missing: {bonus_missing}, "
            f"bonus_reachable: {bonus_reachable}, bonus_urgency: {bonus_urgency}, "
            f"catch_up_urgency: {catch_up_urgency}, score_diff: {score_diff}, "
            f"max_opponent_score: {max_opponent_score}, player_score: {player_score}, "
            f"opponent_score: {opponent_scores}, remaining_upper: {remaining_upper}")

      # Rückgabe des aktuellen Spielzustands
      return {
          "free_fields": [f for f, v in scoreboard[self.name].items() if v is None],  # Verfügbare Felder
          "progress": progress,  # Fortschritt des Spiels
          "score_diff": score_diff,  # Punktedifferenz
          "bonus_missing": bonus_missing,  # Fehlende Punkte für den Bonus
          "bonus_reachable": bonus_reachable,  # Ob der Bonus erreichbar ist
          "bonus_urgency": bonus_urgency,  # Dringlichkeit des Bonus
          "needs_high_scores": score_diff < -30 or progress > 0.7,  # Ob hohe Punktzahlen benötigt werden
          "endgame": progress > 0.8,  # Ob sich das Spiel im Endspiel befindet
          "catch_up_mode": score_diff < -30,  # Ob der Spieler aufholen muss
          "catch_up_urgency": catch_up_urgency,  # Dringlichkeit des Aufholens
          "remaining_upper": remaining_upper,  # Verbleibende Felder im oberen Bereich
          "current_upper": current_upper  # Aktueller Punktestand im oberen Bereich
      }

  def calculate_pattern_score(self, base_points, pattern_type, remaining_rolls):
      """
      Berechnet einen angepassten Punktwert für ein bestimmtes Würfelmuster unter Berücksichtigung verschiedener Spielfaktoren.

      Diese Methode nimmt einen Basis-Punktwert und passt ihn dynamisch an, basierend auf:
      - Dem Typ des Würfelmusters (z.B. Kniffel, Straße, Paare)
      - Der Anzahl verbleibender Würfe
      - Dem aktuellen Spielzustand (z.B. Aufholbedarf, Endspiel)
      - Der Erreichbarkeit des Bonus im oberen Bereich

      Parameter:
          base_points (int): Die Basis-Punktzahl für das Muster
          pattern_type (str): Der Typ des Würfelmusters als String.
                            Mögliche Werte sind:
                            - "Kniffel", "Große Straße", "Kleine Straße" 
                            - "FH_Complete", "FH_FourofaKind", "FH_ThreeofaKind", etc.
                            - "Viererpasch", "Dreierpasch"
                            - "Upper_..." für Felder im oberen Bereich
          remaining_rolls (int): Anzahl der verbleibenden Würfe (0-2)

      Rückgabewert:
          int: Die angepasste Punktzahl nach Anwendung aller Modifikatoren

      Beispiel:
          >>> self.calculate_pattern_score(30, "Kniffel", 1)
          38  # Basis 30 + 5 für Kniffel + weitere situationsabhängige Anpassungen
      """
      # Initialisierung der angepassten Punktzahl mit dem Basiswert
      adjusted_points = base_points

      ####################################################################
      # A) Grundwert-Anpassungen je nach Würfelmuster
      ####################################################################
      # Für jedes Muster wird ein spezifischer Bonus auf die Basispunktzahl addiert
      if pattern_type == "Kniffel":
          adjusted_points += 5  # Kniffel erhält höchsten Bonus
      elif pattern_type == "Große Straße":
          adjusted_points += 5  # Große Straße ebenfalls hoher Bonus
      elif pattern_type == "Kleine Straße":
          adjusted_points += 5  # Kleine Straße gleicher Bonus
      elif pattern_type == "FH_Complete":
          adjusted_points += 4  # Vollständiges Full House
      elif pattern_type == "FH_FourofaKind":
          adjusted_points += 1  # Vier gleiche Würfel für Full House
      elif pattern_type == "FH_ThreeofaKind":
          adjusted_points += 2  # Drei gleiche Würfel für Full House
      elif pattern_type == "FH_TwoPairs":
          adjusted_points += 3  # Zwei Paare für Full House
      elif pattern_type == "FH_OnePair":
          adjusted_points += 1  # Ein Paar für Full House

      # Spezielle Päsche aus dem Scoreboard
      elif pattern_type in ["Viererpasch"]:
          adjusted_points += 2  # Bonus für Viererpasch
      elif pattern_type in ["Dreierpasch"]:
          adjusted_points += 3  # Bonus für Dreierpasch

      # Zusätzliche Muster-Typen für die Bewertung
      elif pattern_type == "FourOfAKind":
          adjusted_points += 3  # Vier gleiche Würfel
      elif pattern_type == "ThreeOfAKind":
          adjusted_points += 2  # Drei gleiche Würfel
      elif pattern_type == "OnePair":
          adjusted_points += 1  # Ein Paar
          if remaining_rolls == 2:
              # Bei frühem Wurf aggressivere Bewertung
              adjusted_points += 2

      # Behandlung der Felder im oberen Bereich (Einser bis Sechser)
      elif pattern_type.startswith("Upper_"):
          # Keine direkte Anpassung der Punkte für obere Felder
          # Diese werden später über die Bonus-Logik behandelt
          pass

      ####################################################################
      # B) Punkteanpassung basierend auf verbleibenden Würfen
      ####################################################################
      if remaining_rolls == 0:
          # Bei letztem Wurf werden 2 Punkte abgezogen
          # Dies spiegelt wider, dass keine Verbesserungsmöglichkeit mehr besteht
          adjusted_points -= 2
      elif remaining_rolls == 2:
          # Bei noch 2 verbleibenden Würfen wird 1 Punkt addiert
          # Dies belohnt frühe gute Würfe, da noch Verbesserungspotential besteht
          adjusted_points += 1

      ####################################################################
      # C) Situationsabhängige Punkteanpassungen
      ####################################################################
      # Wenn wir im "Aufhol-Modus" sind (also hinten liegen)
      if self.game_state["catch_up_mode"]:
          adjusted_points += 5  # Aggressivere Bewertung um aufzuholen

      # Wenn wir hohe Punktzahlen benötigen
      elif self.game_state["needs_high_scores"]:
          adjusted_points += 3  # Moderate Erhöhung der Punktebewertung

      # Spezielle Anpassungen für das Spielende
      if self.game_state["endgame"]:
          if pattern_type in ["Kniffel", "Große Straße"]:
              # Diese Muster werden am Ende weniger wertvoll
              adjusted_points -= 5
          elif pattern_type == "Kleine Straße":
              # Kleine Straße wird etwas wertvoller
              adjusted_points += 2

      # Wenn hohe Punktzahlen benötigt werden
      if self.game_state["needs_high_scores"]:
          if pattern_type in ["Kniffel", "Große Straße"]:
              # Hochwertige Kombinationen werden noch wertvoller
              adjusted_points += 5
          elif pattern_type == "Kleine Straße":
              # Auch kleine Straße wird aufgewertet
              adjusted_points += 3

      # Spezielle Behandlung der oberen Felder wenn Bonus noch erreichbar ist
      if self.game_state["bonus_reachable"]:
          if pattern_type.startswith("Upper_"):
              # Erhöhter Bonus für obere Felder
              # Dies macht es attraktiver, den Bonus zu erreichen
              adjusted_points += 7

      # Zu Beginn des Spiels (erste 30%)
      if self.game_state["progress"] < 0.3:
          if pattern_type == "OnePair":
              # Paare werden früh im Spiel höher bewertet
              # Dies ermöglicht bessere Kombinationen später
              adjusted_points += 2

      ####################################################################
      # Ausgabe der Bewertungsdetails für Debugging-Zwecke
      ####################################################################
      print(f"[DEBUG] Pattern: {pattern_type}, base_points={base_points}, "
            f"remaining_rolls={remaining_rolls}, endgame={self.game_state['endgame']}, "
            f"needs_high_scores={self.game_state['needs_high_scores']}, "
            f"catch_up_mode={self.game_state['catch_up_mode']}, bonus_reachable={self.game_state['bonus_reachable']} => "
            f"adjusted_points={adjusted_points}")

      return adjusted_points

  ####################################################################
  ### Helper functions decide_which_field_to_enter ###
  ####################################################################

  def evaluate_field_scores(self, dice_values, counts, game_state):
      """
      Bewertet alle möglichen Felder mit einer heuristischen Punktbewertung.

      **Beschreibung:**
      Diese Methode analysiert die aktuellen Würfelwerte und den Spielzustand, um die Punktwerte für die verfügbaren Felder zu berechnen. Sie gibt eine Bewertung für jedes Feld zurück, basierend auf den aktuellen Würfeln und den Regeln des Spiels.

      **Parameter:**
      - `dice_values` (*List[int]*): Eine Liste der aktuellen Würfelwerte, die der Spieler geworfen hat.
      - `counts` (*numpy.ndarray von int*): Ein Array, das zählt, wie oft jede Augenzahl (1 bis 6) in den aktuellen Würfeln vorkommt.
      - `game_state` (*dict*): Ein Wörterbuch, das den aktuellen Zustand des Spiels enthält (z.B. verfügbare Felder, Bonusinformationen).

      **Rückgabewert:**
      - *dict*: Ein Wörterbuch, das die Punktwerte für die verfügbaren Felder enthält. Die Schlüssel sind die Feldnamen, und die Werte sind die entsprechenden Punktwerte.

      **Verwendete Python-Konzepte:**
      - **NumPy-Operationen**: Für effiziente Berechnungen und Array-Manipulationen.
      - **Bedingte Anweisungen (`if`-Statements)**: Zur Entscheidungsfindung basierend auf den aktuellen Würfeln.
      - **Listen- und Dictionary-Verarbeitung**: Zur Verwaltung von Punkteständen und Spielinformationen.
      - **List Comprehensions**: Für die kompakte Erstellung von Listen.

      **Details der Bewertung:**
      Die Methode bewertet die Felder im oberen Bereich (Einser bis Sechser) sowie spezielle Kombinationen wie Kniffel, Straßen und Full House. Sie gibt die Punktwerte zurück, die für strategische Entscheidungen verwendet werden können.

      """
      field_scores = {}  # Initialisierung eines leeren Dictionaries für die Feldbewertungen
      dice_set = set(dice_values)  # Erstellen einer Menge aus den geworfenen Würfeln, um doppelte Werte zu entfernen
      total = np.sum(dice_values)  # Berechnung der Gesamtsumme der geworfenen Würfel

      # Überprüfen auf bestimmte Muster wie Full House, kleine und große Straße
      is_full_house, has_small_straight, has_large_straight = check_patterns(counts, dice_set)

      # Bewertung der verfügbaren Felder
      for field in game_state["free_fields"]:
          score = 0  # Initialisierung des Punktwerts für das aktuelle Feld

          # Bewertung der oberen Sektion
          if field in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
              number = {"Einser": 1, "Zweier": 2, "Dreier": 3, 
                       "Vierer": 4, "Fünfer": 5, "Sechser": 6}[field]  # Zuordnung der Feldnamen zu den Würfelwerten
              score = counts[number-1] * number  # Berechnung des Punktwerts für das Feld

              # Anpassung des Punktwerts, wenn der Bonus erreichbar ist
              if game_state["bonus_reachable"]:
                  score += 5  # Bonusheuristik

          # Bewertung spezieller Kombinationen
          elif field == "Kniffel":
              if np.max(counts) == 5:  # Überprüfen, ob alle fünf Würfel gleich sind
                  score = 50 + 10  # Erhöhter Bonus für Kniffel

          elif field == "Große Straße":
              if has_large_straight:  # Überprüfen, ob eine große Straße vorhanden ist
                  score = 40 + 8  # Erhöhter Bonus für große Straße

          elif field == "Kleine Straße":
              if has_small_straight:  # Überprüfen, ob eine kleine Straße vorhanden ist
                  score = 30 + 5  # Bonus für kleine Straße

          elif field == "Full House":
              if is_full_house:  # Überprüfen, ob ein Full House vorhanden ist
                  score = 25 + 7  # Erhöhter Bonus für Full House

          elif field == "Viererpasch":
              if np.max(counts) >= 4:  # Überprüfen, ob mindestens vier gleiche Würfel vorhanden sind
                  score = total  # Punktwert ist die Summe aller Würfel
              else:
                  score = 0  # Oder überlegen Sie, ob Sie zumindest die Summe eintragen möchten

          elif field == "Dreierpasch":
              if np.max(counts) >= 3:  # Überprüfen, ob mindestens drei gleiche Würfel vorhanden sind
                  score = total  # Punktwert ist die Summe aller Würfel
              else:
                  score = 0  # Oder zumindest die Summe eintragen

          elif field == "Chance":
              total = np.sum(dice_values)  # Berechnung der Gesamtsumme der geworfenen Würfel
              score = total  # Punktwert ist die Summe aller Würfel

          # Wenn das Feld einen Punktwert hat, füge es dem Dictionary hinzu
          if score > 0:
              field_scores[field] = score  # Speichern des Punktwerts für das aktuelle Feld

      return field_scores  # Rückgabe der Punktwerte für die verfügbaren Felder

  def select_fallback_field(self, free_fields):
      """
      Wählt ein Feld aus, wenn keine guten Punktoptionen verfügbar sind.

      **Beschreibung:**
      Diese Methode entscheidet, welches Feld der Spieler auswählen sollte, wenn keine vorteilhaften Optionen zur Verfügung stehen. Die Strategie besteht darin, ein Feld mit niedrigem Wert zu opfern, um die Punktzahl zu maximieren.

      **Parameter:**
      - `free_fields` (*List[str]*): Eine Liste der Felder, die noch nicht ausgefüllt sind.

      **Rückgabewert:**
      - *str oder None*: Der Name des ausgewählten Feldes, das ausgefüllt werden soll. Gibt `None` zurück, wenn keine freien Felder verfügbar sind.

      **Verwendete Python-Konzepte:**
      - **Bedingte Anweisungen (`if`-Statements)**: Zur Entscheidungsfindung basierend auf den verfügbaren Feldern.
      - **Listenverarbeitung**: Zur Verwaltung der verfügbaren Felder.

      **Details der Strategie:**
      Die Methode priorisiert die Auswahl von Feldern mit niedrigem Wert, um die Punktzahl zu maximieren, wenn keine besseren Optionen vorhanden sind.

      """
      if not free_fields:
          return None  # Gibt None zurück, wenn keine freien Felder verfügbar sind

      # Versuche, ein Feld mit niedrigem Wert zu opfern
      for field in ["Einser", "Zweier", "Dreier", "Chance"]:
          if field in free_fields:
              return field  # Gibt das erste verfügbare Feld mit niedrigem Wert zurück

      # Wähle das Feld mit der niedrigsten Priorität basierend auf den Feldwerten
      return min(free_fields, key=lambda f: self.field_values[f][1])  # Gibt das Feld mit dem niedrigsten Wert zurück


class Fatih_1():
    def __init__(self, name):
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
       
        if roll == 0:
            # Beim ersten Wurf: Halte die häufigsten Würfel, wenn keine Häufung, dann halte 5 und 6
            counts = Counter(dice_rolls)
            most_common = counts.most_common()
            max_count = most_common[0][1]
            
            # Halte die häufigsten Werte (mindestens 2 gleiche Würfel)
            dices_to_keep = [dice for dice in dice_rolls if counts[dice] == max_count]
            
            # Falls keine Häufung vorhanden ist, halte alle 5 und 6
            if len(dices_to_keep) < 2:
                dices_to_keep = [dice for dice in dice_rolls if dice == 5 or dice == 6]
                
            return dices_to_keep

        elif roll == 1:
            # Beim zweiten Wurf: Halte alle Würfel, die bereits gehalten wurden
            counts = Counter(kept_dices)
            most_common = counts.most_common()
            max_count = most_common[0][1]

            # Wenn keine Häufung vorhanden ist, versuche, eine Straße oder ein Full House zu vervollständigen
            if max_count < 3:  # Keine Drillinge, Vierlinge oder Kniffel
                # Überprüfen, ob eine Kleine Straße oder Große Straße möglich ist
                unique_dice = set(kept_dices)
                if self.is_possible_straight(unique_dice):
                    return kept_dices  # Behalte alle Würfel, die zur Straße führen
                # Überprüfen, ob ein Full House möglich ist
                if self.is_possible_full_house(unique_dice):
                    return kept_dices  # Behalte alle Würfel, die zum Full House führen
            return kept_dices  # Halte alle Würfel, die schon gehalten wurden

        else:
            # Beim dritten Wurf: Halte keine Würfel mehr
            return []

    def is_possible_straight(self, unique_dice):
        # Prüfen, ob eine Kleine Straße oder große Straße möglich ist.
        # Kleine Straße: [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]
        # Große Straße: [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]
        possible_small_straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
        possible_large_straights = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]
        
        # Überprüfen, ob eine kleine Straße oder große Straße möglich ist
        for seq in possible_small_straights + possible_large_straights:
            if seq.issubset(unique_dice):
                return True
        return False

    def is_possible_full_house(self, unique_dice):
        #Prüfen, ob ein Full House möglich ist.
        # Full House ist möglich, wenn 3 gleiche und 2 gleiche Zahlen existieren
        if len(unique_dice) == 2:
            return True
        return False

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        # Eintragung der Punkte in ein Feld
        available_fields = [field for field in [
            "Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser",
            "Dreierpasch", "Viererpasch", "Full House", "Kleine Straße",
            "Große Straße", "Kniffel", "Chance"
        ] if scoreboard[self.name][field] is None]  # Nur Felder, die noch nicht belegt sind

        if not available_fields:
            return random.choice(list(scoreboard[self.name].keys()))  # Wenn alle Felder belegt sind, wähle zufällig

        # Überprüfen, ob eine der speziellen Kombinationen geworfen wurde
        counts = Counter(dice_values)
        unique_dice = set(dice_values)

        # Überprüfen auf Full House
        if len(unique_dice) == 2 and any(dice_values.count(die) == 3 for die in unique_dice):
            if "Full House" in available_fields:
                return "Full House"

        # Überprüfen auf Dreierpasch
        if any(count >= 3 for count in counts.values()):
            if "Dreierpasch" in available_fields:
                return "Dreierpasch"

        # Überprüfen auf Kleine Straße
        if any(all(x in unique_dice for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
            if "Kleine Straße" in available_fields:
                return "Kleine Straße"

        # Überprüfen auf Große Straße
        if set([1, 2, 3, 4, 5]).issubset(unique_dice) or set([2, 3, 4, 5, 6]).issubset(unique_dice):
            if "Große Straße" in available_fields:
                return "Große Straße"

        # Überprüfen auf Kniffel
        if len(unique_dice) == 1:
            if "Kniffel" in available_fields:
                return "Kniffel"

        # Wenn keine speziellen Felder gewählt werden können, wähle die bevorzugten Felder
        for field in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
            if field in available_fields:
                return field

        # Wenn keine sicheren Felder mehr übrig sind, wähle zufällig aus den verbleibenden Feldern
        return random.choice(available_fields)


class Jansen_1(Kniffel_Player):
    def __init__(self, name):
        """Name should be a string"""
        self.name = name
        self.bonus_count = 0

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' Welche Würfel werden behalten. '''
        #Dict wo Name des Feldes aus oberen Kategorie mit Zahl verknüpft wird
        upper_section = {"Einser": 1, "Zweier": 2, "Dreier": 3, "Vierer": 4, "Fünfer": 5, "Sechser": 6}
        
        #Erstellt neues Dict das Felder enthält, die noch nicht ausgefüllt sind (oberer Bereich)
        remaining_upper = {field: value for field, value in upper_section.items() if scoreboard[self.name][field] is None}
    
        #Wenn der obere Teil nicht vollständig ist, Fokus auf Bonus
        if remaining_upper:
            #Berechnet benötigten Punkte für jedes Feld
            bonus_goal = 63
            #Berechnet aktuelle Punktzahl des oberen Bereichs & .get(field,0)->Punktestand aktuelles Feld nicht ausgefüllt=0
            current_upper_score = sum(scoreboard[self.name].get(field, 0) or 0 for field in upper_section.keys())
            #Filtert verbleibenden oberen Felder, um Felder auszuwählen die helfen die 63 Punkte zu erzielen basierend auf aktuellen Punktzahl und aktuellen Würfen
            fields_needed = {field: value for field, value in remaining_upper.items() if current_upper_score + (value * dice_rolls.count(value)) < bonus_goal}
    
            #Fous auf Felder nahe dem Bonus
            if fields_needed:
                #Sucht höhsten Wert aus fields_needed und speichert ihn in target_field
                target_field = max(fields_needed, key=fields_needed.get)
                #Speichert numerischen Wert aus target_field ab
                target_value = fields_needed[target_field]
                #Sammmelt alle Würfe aus dice_roll die mit target_value übereinstimmen & Leere Liste False 
                keep_dices = [die for die in dice_rolls if die == target_value]
                if keep_dices:
                    return keep_dices
    
        #Wenn in oberen Feldern nichts möglich werden untere Felder bewertet
        #Full House
        #Erstellt Dict, wo jeder Würfelwert die Anzahl seiner Vorkommen zuordnet
        unique_counts = {die: dice_rolls.count(die) for die in set(dice_rolls)}
        #Prüft ob unique_counts eine Länge von 2 hat für Full House -> True or False
        if len(unique_counts) == 2 and (3 in unique_counts.values() and 2 in unique_counts.values()):
            return dice_rolls  #Behalte alle für ein Full House
    
        #Kleine Straße
        #Wandelt Liste dice_rolls in Menge(Set) um und sortiert von klein zu groß
        sorted_dice = sorted(set(dice_rolls))
        #Prüft ob alle Zahlen x der aktuellen Straße seq in sorted_dice enthalten sind->True or False
        if any(all(x in sorted_dice for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
            return sorted_dice
    
        #Behalte Drillinge für Dreierpasch oder Kniffel
        #Prüft ob ein Würfelwert in unique_counts mind. 3mal vorkommt
        for die, count in unique_counts.items():
            if count >= 3:
                #Gibt Liste aus die den Wert die 3mal wiederholt
                return [die] * 3
    
        #Würfel mit hohen Werten behalten in Liste; Fokus auf 5er und 6er
        return [die for die in dice_rolls if die >= 5]


    def decide_which_field_to_enter(self, scoreboard, dice_values):
        ''' Wahl des Spielers wo er Punkte eintragen möchte.'''
        upper_section = {"Einser": 1, "Zweier": 2, "Dreier": 3, "Vierer": 4, "Fünfer": 5, "Sechser": 6}
        lower_section = ["Dreierpasch", "Viererpasch", "Full House","Kleine Straße", "Große Straße", "Kniffel", "Chance"]
    
        #Priorisiert den oberen Teil um den Bonus zu sichern
        for field, value in upper_section.items():
            #Gibt Feld zurück, welches in dice_Value 3mal vorkommt und noch nicht belegt wurde
            if scoreboard[self.name][field] is None and dice_values.count(value) >= 3:
                return field

        #Höheren Felder als nächstes
        #Prüft die Länge des set(dice_value) wenn 1 und Kniffel noch frei dann fülle Kniffel aus
        if len(set(dice_values)) == 1:  # Kniffel
            if scoreboard[self.name]["Kniffel"] is None:
                return "Kniffel"

        #Wenn Länge des set(dice_values) 2, dann Möglichkeit auf Full House prüfen
        if len(set(dice_values)) == 2:
            #Erstellt eine Liste mit Häufigkeit der beiden Zahlen
            counts = [dice_values.count(value) for value in set(dice_values)]
            #Prüft ob eine Dreiergruppe und Paar in Liste enthalten und ob Full House noch frei ist
            if 3 in counts and 2 in counts and scoreboard[self.name]["Full House"] is None:
                return "Full House"

        #Kleine & Große Straße
        #Sortiert Werte aus dice_value in aufsteigender Reihenfolge
        sorted_dices = sorted(set(dice_values))
        #Länge muss mind. 4 sein, sonst ist keine Kleine Straße möglich
        if len(sorted_dices) >= 4:
            #Schleife geht alle möglichen Kleinen Straßen durch
            for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]):
                #Prüft ob alle Zahlen der möglichen Kleine  Straße in sorted_dices vorhanden ist
                if all(x in sorted_dices for x in seq):
                    if scoreboard[self.name]["Kleine Straße"] is None:
                        return "Kleine Straße"

        #Länge muss mind. 5 sein, sonst Große Straße nicht möglich und Feld muss frei sein
        if len(sorted_dices) >= 5 and scoreboard[self.name]["Große Straße"] is None:
            #Prüft Möglichkeiten einer Großen Straße in sorted_dices; .issubset(sorted_dices) prüft ob geforderte Zahlenfolge eine Teilmenge von sorted_dices ist
            if set([1, 2, 3, 4, 5]).issubset(sorted_dices) or set([2, 3, 4, 5, 6]).issubset(sorted_dices):
                return "Große Straße"

        # Dreierpasch and Viererpasch
        for dice in set(dice_values):
            #Zählt wie oft Würfelwert in dice_value vorkommt
            count = dice_values.count(dice)
            #Falls Würfelwert mind. 4 mal vorkommt und Feld leer ->Viererpasch; falls beides kommt Viererpasch priorisieren
            if count >= 4 and scoreboard[self.name]["Viererpasch"] is None:
                return "Viererpasch"
            #Falls Würfelwert mind. 3 mal vorkommt und Feld leer ->Dreierpasch
            if count >= 3 and scoreboard[self.name]["Dreierpasch"] is None:
                return "Dreierpasch"

        #Wenn Chance noch frei (None) wähle Chance
        if scoreboard[self.name]["Chance"] is None:
            return "Chance"

        #Wählt zufälliges Feld wenn nichts anderes mehr möglich
        #Erstellt eine Liste aus den oberen und unteren Feldnamen->Liste aller möglichen Kategorien
        for field in list(upper_section.keys()) + lower_section:
            #Prüft ob Feld noch nicht ausgefüllt wurde und gibt erstes mögliche Feld zurück
            if scoreboard[self.name][field] is None:
                return field

        #Kein freies Feld mehr
        raise ValueError("No available fields to enter the score.")

    def record_bonus(self, scoreboard):
        """Zeigt an wie oft der Bonus erreicht wurde."""
        upper_section_fields = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]
        upper_section_score = sum(scoreboard[self.name].get(field, 0) or 0 for field in upper_section_fields)
        #Falls Punkte in oberen Felder >= 63 dann counter +1
        if upper_section_score >= 63:
            self.bonus_count += 1


class Jansen_2():
    def __init__(self, name):
        """ Erstellt einen Spieler mit Namen und zählt, wie oft der Bonus erreicht wurde. """
        self.name = name
        self.bonus_count = 0  # Speichert wie oft der Spieler den Bonus erreicht

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        """
        Entscheidet, welche Würfel behalten werden sollen, basierend auf Wahrscheinlichkeiten.
        """
        # Bestimme beste Kategorie basierend auf aktuellen Würfeln
        target = self.determine_best_category(scoreboard, dice_rolls + kept_dices, 3 - roll)

        # Falls eine große Straße möglich ist halte passende Würfel
        if target == "Große Straße":
            needed1 = [2, 3, 4, 5, 6]  # Erste mögliche große Straße
            needed2 = [1, 2, 3, 4, 5]  # Zweite mögliche große Straße
            return [die for die in dice_rolls if die in needed1 or die in needed2] + kept_dices

        # Falls kleine Straße möglich ist halte die besten Würfel
        if target == "Kleine Straße":
            possible_sequences = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]  # Mögliche Straßen
            kept = []
            for seq in possible_sequences:
                temp_kept = [die for die in dice_rolls if die in seq]  #Prüfe welche Würfel zur Straße gehören
                if len(temp_kept) > len(kept):  #Wähle die längste mögliche Sequenz
                    kept = temp_kept
            return kept + kept_dices

        # Full House 
        if target == "Full House":
            counts = Counter(dice_rolls + kept_dices)  # Zählt anzahl Zahlen
            pair = [die for die, count in counts.items() if count == 2]  #Findet Paare
            triple = [die for die, count in counts.items() if count >= 3]  #Findet Drillinge
            if pair and triple:  # Falls sowohl ein Paar als auch ein Drilling existiert
                return pair[:2] + triple[:3]  # Behalte die besten Kombinationen
            elif triple:  #Falls nur ein Drilling vorhanden ist, versuche ein Paar zu bekommen
                return triple[:3]
            return kept_dices  

        # Falls ein oberes Feld (Einser bis Sechser) gewählt wurde, halte die passenden Würfel
        if target in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
            number = self.extract_number_from_field(target)  
            return [die for die in dice_rolls if die == number] + kept_dices  # Halte nur diese Zahl

        # Falls Dreierpasch, Viererpasch oder Kniffel -> behalte diese 
        if target in ["Dreierpasch", "Viererpasch", "Kniffel"]:
            match_count = {"Dreierpasch": 3, "Viererpasch": 4, "Kniffel": 5}[target]  
            counts = Counter(dice_rolls + kept_dices)  # Zähle, welche Augenzahlen vorkommen
            for die, count in counts.items():
                if count >= match_count:  #wenn genug gleiche Würfel da sind, halte sie
                    return [die] * count
            return kept_dices  #Falls keine passende Kombination existiert, behalte alte Würfel

        return kept_dices  # Standardfall: Keine sinnvolle Entscheidung → Behalte die alten Würfel

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        
        #Bestimmt, in welches Feld der aktuelle Wurf eingetragen werden soll.
        
        valid_fields = [field for field, score in scoreboard[self.name].items() if score is None]  # Finde leere Felder
        expected_scores = {field: self.evaluate_field(field, dice_values) for field in valid_fields}  # Berechne erwartete Punkte

        if expected_scores:
            return max(expected_scores, key=expected_scores.get)  #Wähle Feld mit der höchsten Punktzahl

        return "Chance"  #Falls keine sinnvolle Option existiert, nehme Chance

    def determine_best_category(self, scoreboard, dice_values, remaining_rolls):
       
        #Bestimmt die beste Kategorie basierend auf den aktuellen Würfeln und den verbleibenden Würfen.
        
        valid_fields = [field for field, score in scoreboard[self.name].items() if score is None]  # Noch nicht belegte Felder
        expected_scores = {field: self.evaluate_field(field, dice_values) for field in valid_fields}  # Erwartete Punktzahl berechnen

        if expected_scores:
            return max(expected_scores, key=expected_scores.get)  #wähle mit der höchsten erwarteten Punktzahl

        return "Chance"  # Falls keine andere Wahl bleibt, nehme "Chance"

    def extract_number_from_field(self, field):
       
        #Wandelt die Kategorien "Einser", "Zweier", etc. in Zahlen (1-6) um.
        
        mapping = {
            "Einser": 1, "Zweier": 2, "Dreier": 3, "Vierer": 4, "Fünfer": 5, "Sechser": 6
        }
        return mapping[field]

    def evaluate_field(self, field, dice_values):
        
        #Berechnet Punktzahl für aktuelle Würfel 
        
        match field:
            case "Einser": return dice_values.count(1)
            case "Zweier": return dice_values.count(2) * 2
            case "Dreier": return dice_values.count(3) * 3
            case "Vierer": return dice_values.count(4) * 4
            case "Fünfer": return dice_values.count(5) * 5
            case "Sechser": return dice_values.count(6) * 6
            case "Dreierpasch": return sum(dice_values) if max(Counter(dice_values).values()) >= 3 else 0
            case "Viererpasch": return sum(dice_values) if max(Counter(dice_values).values()) >= 4 else 0
            case "Full House":
                counts = Counter(dice_values).values()
                return 25 if sorted(counts) == [2, 3] else 0
            case "Kleine Straße":
                straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
                return 30 if any(all(x in dice_values for x in seq) for seq in straights) else 0
            case "Große Straße":
                return 40 if set([1, 2, 3, 4, 5]) <= set(dice_values) or set([2, 3, 4, 5, 6]) <= set(dice_values) else 0
            case "Kniffel": return 50 if len(set(dice_values)) == 1 else 0
            case "Chance": return sum(dice_values)
            case _: return 0

    def record_bonus(self, scoreboard):
        
        upper_section_fields = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]
        upper_section_score = sum(scoreboard[self.name].get(field, 0) for field in upper_section_fields)
        if upper_section_score >= 63:
            self.bonus_count += 1  # Bonus wird gezählt für simulationsstudie


class Marquardt_1(Kniffel_Player):

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        """
        Spieler 1: Diese Strategie sucht nach Zahlen, die oft vorkommen (z. B. zwei oder mehr).
        Er versucht auch, Full House oder Straßen (Zahlenreihen) zu bilden.
        """
        kept_dices_to_return = kept_dices.copy() # Kopie der Würfel, die der Spieler schon behalten hat
        dice_counts = Counter(dice_rolls) # Zählt, wie oft jede Zahl geworfen wurde.

        # Am Anfang: Behalte Zahlen, die mindestens zweimal vorkommen
        if roll == 0:
            for number, count in dice_counts.items():
                if count >= 2 and scoreboard[self.name].get(f"{number}er") is None:
                    kept_dices_to_return.extend([number] * 2)
                    return kept_dices_to_return

        # Später: Behalte nur Zahlen, die bereits gesammelt wurden
        if roll in [1, 2]:
            if kept_dices_to_return:
                kept_dices_to_return = [dice for dice in dice_rolls if dice in kept_dices_to_return]
                return kept_dices_to_return

        # Full House: Behalte zwei Paare, falls möglich
        if roll == 0 and scoreboard[self.name].get("Full House") is None:
            pairs = [number for number, count in dice_counts.items() if count >= 2]
            if len(pairs) >= 2:
                kept_dices_to_return.extend(pairs[:2] * 2)
                return kept_dices_to_return

        # Straßen: Halte Zahlen, die eine Reihe bilden
        if roll == 0 and not kept_dices_to_return:
            for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]):
                if all(x in dice_rolls for x in seq) and scoreboard[self.name].get("Kleine Straße") is None:
                    kept_dices_to_return.extend(seq)
                    return kept_dices_to_return
            for seq in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
                if all(x in dice_rolls for x in seq) and scoreboard[self.name].get("Große Straße") is None:
                    kept_dices_to_return.extend(seq)
                    return kept_dices_to_return
                
        # Falls nichts passt, bleibe bei den bereits gesammelten Zahlen
        return kept_dices_to_return

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        """
        Wählt das Feld mit den meisten Punkten aus.
        Priorisiert besondere Felder wie Full House, Kniffel und Straßen.
        """
        best_field = None
        best_score = -1   
        counts = Counter(dice_values)  # Zähle die Häufigkeit der geworfenen Zahlen
        
        # Spezialfälle: Full House, Straßen oder Kniffel
        if sorted(counts.values()) == [2, 3]:
            return "Full House"
        elif any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])):
            return "Große Straße" if len(set(dice_values)) == 5 else "Kleine Straße"
        elif len(set(dice_values)) == 1:
            return "Kniffel"


        # Suche das Feld mit der höchsten Punktzahl
        for field, value in scoreboard[self.name].items():
            if value is None:   # Nur freie Felder berücksichtigen
                score = self.calculate_field_score(field, dice_values)
                if score > best_score:
                    best_field = field
                    best_score = score

        # Wenn kein  Feld, setze Null in bestimmte Felder
        if best_field is None:
            zero_priority_fields = ["Einser", "Zweier", "Kniffel", "Viererpasch", "Große Straße"]
            for field in zero_priority_fields:
                if scoreboard[self.name].get(field) is None:
                    best_field = field
                    break

        # Fallback strategy: prioritize 1s and 2s for zero entry if no other fields are suitable
        if best_field is None:
            for number in [1, 2]:
                if scoreboard[self.name].get(f"{number}er") is None:
                    best_field = f"{number}er"
                    break

        return best_field

    def calculate_field_score(self, field, dice_values):
        """ Berechnet die Punkte für ein bestimmtes Feld, basierend auf den aktuellen Würfeln """
        match field:
            case "Einser":
                return dice_values.count(1) * 1
            case "Zweier":
                return dice_values.count(2) * 2
            case "Dreier":
                return dice_values.count(3) * 3
            case "Vierer":
                return dice_values.count(4) * 4
            case "Fünfer":
                return dice_values.count(5) * 5
            case "Sechser":
                return dice_values.count(6) * 6
            case "Dreierpasch":
                if max(Counter(dice_values).values()) >= 3:
                    return sum(dice_values)
                return 0
            case "Viererpasch":
                if max(Counter(dice_values).values()) >= 4:
                    return sum(dice_values)
                return 0
            case "Full House":
                counts = Counter(dice_values)
                if sorted(counts.values()) == [2, 3]:
                    return 25
                return 0
            case "Kleine Straße":
                if any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
                    return 30
                return 0
            case "Große Straße":
                if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values):
                    return 40
                return 0
            case "Kniffel":
                if len(set(dice_values)) == 1:
                    return 50
                return 0
            case "Chance":
                return sum(dice_values)
            case _:
                return 0


class Marquardt_2(Kniffel_Player):
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        
        """ Spieler 2: Diese Strategie fokussiert sich zuerst auf hohe Felder wie Kniffel, Full House,
        Straßen und dann auf Viererpasch oder Dreierpasch. """
        
        kept_dices_to_return = kept_dices.copy()
        dice_counts = Counter(dice_rolls)

        # Prio 6er, wenn das Feld "Sechser" noch frei ist
        if scoreboard[self.name].get("Sechser") is None:
            kept_dices_to_return.extend([6] * dice_counts.get(6, 0))

        # Kniffel Versuch
        if len(set(dice_rolls)) == 1:
            kept_dices_to_return.extend(dice_rolls)
            return kept_dices_to_return

        # kleine Strasse
        if roll == 0:
            for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]):
                if all(x in dice_rolls for x in seq) and scoreboard[self.name].get("Kleine Straße") is None:
                    kept_dices_to_return.extend(x for x in seq if x not in kept_dices_to_return)
                    return kept_dices_to_return
                
        # große Strasse
        elif roll in [1, 2]:
            for seq in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
                if all(x in dice_rolls for x in seq) and scoreboard[self.name].get("Große Straße") is None:
                    kept_dices_to_return.extend(x for x in seq if x not in kept_dices_to_return)
                    return kept_dices_to_return

        # Behalte Zahlen, die oft vorkommen (für Pasch oder Full House)
        for dice, count in dice_counts.items():
            if count >= 3 and dice not in kept_dices_to_return:
                kept_dices_to_return.extend([dice] * count)

        return kept_dices_to_return

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        """ Prio:  Kniffel, Full House und Straßen... Wählt sonst das Feld mit den meisten Punkten """
        best_field = None
        best_score = -1
        
        for field, value in scoreboard[self.name].items():
            if value is None:
                score = self.calculate_field_score(field, dice_values)
                if field == "Chance" and score <= 17.5:
                    continue  # Skip 
                if score > best_score:
                    best_field = field
                    best_score = score

        # 0 bei Notfall setzen 
        if best_field is None:
            zero_priority_fields = ["Einser", "Zweier", "Viererpasch", "Große Straße"]
            for field in zero_priority_fields:
                if scoreboard[self.name].get(field) is None:
                    best_field = field
                    break

        return best_field

    def calculate_field_score(self, field, dice_values):
        """Berechnet die Punkte für entsprechende Würfel."""
        match field:
            case "Einser":
                return dice_values.count(1) * 1
            case "Zweier":
                return dice_values.count(2) * 2
            case "Dreier":
                return dice_values.count(3) * 3
            case "Vierer":
                return dice_values.count(4) * 4
            case "Fünfer":
                return dice_values.count(5) * 5
            case "Sechser":
                return dice_values.count(6) * 6
            case "Dreierpasch":
                if max(Counter(dice_values).values()) >= 3:
                    return sum(dice_values)
                return 0
            case "Viererpasch":
                if max(Counter(dice_values).values()) >= 4:
                    return sum(dice_values)
                return 0
            case "Full House":
                counts = Counter(dice_values)
                if sorted(counts.values()) == [2, 3]:
                    return 25
                return 0
            case "Kleine Straße":
                if any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
                    return 30
                return 0
            case "Große Straße":
                if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values):
                    return 40
                return 0
            case "Kniffel":
                if len(set(dice_values)) == 1:
                    return 50
                return 0
            case "Chance":
                return sum(dice_values)
            case _:
                return 0



class Martinelli_1(Kniffel_Player):

    def __init__(self, name, learning_rate=0.1):
        """
        Erstellt einen KI-Spieler, der Monte-Carlo-Simulationen mit einer
        vereinfachten Lernkomponente kombiniert.
        
        :param name: Name des KI-Spielers
        :param learning_rate: Gewichtung, mit der neue Erkenntnisse 
                              (z.B. Erfolge/Misserfolge) in das Modell einfließen
        """
        self.name = name
        self.decision_log = []
        
        # Lernparameter: speichert "Vortlieben" (Weichtungen) für jede Kategorie.
        # Startwerte alle bei 1.0, d.h. zunächst neutral.
        self.category_preferences = {
            "Einser": 1.0,
            "Zweier": 1.0,
            "Dreier": 1.0,
            "Vierer": 1.0,
            "Fünfer": 1.0,
            "Sechser": 1.0,
            "Dreierpasch": 1.0,
            "Viererpasch": 1.0,
            "Kleine Straße": 1.0,
            "Große Straße": 1.0,
            "Full House": 1.0,
            "Kniffel": 1.0,
            "Chance": 1.0
        }
        self.learning_rate = learning_rate

    def analyze_dice(self, wuerfel_liste):
        """
        Analysiert die Würfelergebnisse (wuerfel_liste) und gibt eine Übersicht
        der erzielbaren Punkte in einem Dictionary zurück.
        """
        summe_der_wuerfel = sum(wuerfel_liste)
        anzahl_pro_auge = [wuerfel_liste.count(i) for i in range(1, 7)]

        ergebnisse = {}

        # Obere Sektion + numerische Schlüssel
        obere_kategorien = [
            ("1", "Einser"),
            ("2", "Zweier"),
            ("3", "Dreier"),
            ("4", "Vierer"),
            ("5", "Fünfer"),
            ("6", "Sechser")
        ]
        for idx, (zahlen_key, name_key) in enumerate(obere_kategorien, start=1):
            punkte = anzahl_pro_auge[idx - 1] * idx
            ergebnisse[zahlen_key] = punkte
            ergebnisse[name_key] = punkte

        # Dreierpasch / Viererpasch
        if any(anzahl >= 3 for anzahl in anzahl_pro_auge):
            ergebnisse["Dreierpasch"] = summe_der_wuerfel
        if any(anzahl >= 4 for anzahl in anzahl_pro_auge):
            ergebnisse["Viererpasch"] = summe_der_wuerfel

        # Kleine Straße
        kleine_strassen = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        if any(set(straße).issubset(wuerfel_liste) for straße in kleine_strassen):
            ergebnisse["Kleine Straße"] = 30

        # Große Straße
        if set([1, 2, 3, 4, 5]).issubset(wuerfel_liste) or set([2, 3, 4, 5, 6]).issubset(wuerfel_liste):
            ergebnisse["Große Straße"] = 40

        # Full House (3 gleiche + 2 gleiche)
        if 3 in anzahl_pro_auge and 2 in anzahl_pro_auge:
            ergebnisse["Full House"] = 25

        # Kniffel (alle 5 identisch)
        if 5 in anzahl_pro_auge:
            ergebnisse["Kniffel"] = 50

        # Chance (Summe aller Würfel)
        ergebnisse["Chance"] = summe_der_wuerfel

        return ergebnisse

    def simulate_additional_rolls(self, behaltene_wuerfel, punktetafel, anzahl_simulationen=2000):
        """
        Simuliert zukünftige Würfe (Monte-Carlo) und berechnet den
        durchschnittlich erzielbaren Punktewert.
        """
        gesamtpunkte = 0
        gueltige_simulationen = 0

        anzahl_zu_werfen = 5 - len(behaltene_wuerfel)
        for _ in range(anzahl_simulationen):
            neue_wuerfe = [random.randint(1, 6) for _ in range(anzahl_zu_werfen)]
            wuerfel_kombination = behaltene_wuerfel + neue_wuerfe

            alle_punkte = self.analyze_dice(wuerfel_kombination)
            offene_punkte = {
                kategorie: wert
                for kategorie, wert in alle_punkte.items()
                if punktetafel[self.name].get(kategorie) is None
            }

            if offene_punkte:
                # Neben dem reinen Punktewert soll auch die Präferenz berücksichtigt werden
                # Wir berechnen "effektiver Wert" = Punkte * category_preferences[kategorie]
                # und nehmen das Maximum
                effektive_werte = [
                    offene_punkte[k] * self.category_preferences.get(k, 1.0)
                    for k in offene_punkte
                ]
                gesamtpunkte += max(effektive_werte)
                gueltige_simulationen += 1

        return gesamtpunkte / gueltige_simulationen if gueltige_simulationen > 0 else 0

    def monte_carlo_strategy(self, wuerfel_liste, punktetafel, anzahl_durchlaeufe=1000):
        """
        Ermittelt mithilfe einer Monte-Carlo-Simulation + einfacher Präferenzgewichtung,
        welche Würfel am besten behalten werden sollten.
        """
        beste_strategie = None
        hoechster_erwartungswert = -float('inf')

        moegliche_kombinationen = [
            list(kombi)
            for i in range(len(wuerfel_liste) + 1)
            for kombi in itertools.combinations(wuerfel_liste, i)
        ]

        for behaltene_wuerfel in moegliche_kombinationen:
            erwartungswert = self.simulate_additional_rolls(
                behaltene_wuerfel, punktetafel, anzahl_simulationen=anzahl_durchlaeufe
            )
            if erwartungswert > hoechster_erwartungswert:
                hoechster_erwartungswert = erwartungswert
                beste_strategie = behaltene_wuerfel

        return beste_strategie, hoechster_erwartungswert

    def decide_which_dices_to_hold(self, punktetafel, bereits_behalten, wuerfel_liste, aktueller_wurf):
        """
        Entscheidet, welche Würfel nach dem aktuellen Wurf behalten werden sollen.
        """
        beste_wuerfel, bester_durchschnitt = self.monte_carlo_strategy(wuerfel_liste, punktetafel)

        self.decision_log.append({
            "aktion": "wuerfel_behalten",
            "wuerfel_liste": wuerfel_liste,
            "bereits_behalten": bereits_behalten,
            "tatsaechlich_behalten": beste_wuerfel,
            "durchschnittspunkte": bester_durchschnitt,
            "wurf_nummer": aktueller_wurf
        })

        return beste_wuerfel

    def decide_which_field_to_enter(self, punktetafel, wuerfel_werte):
        """
        Entscheidet, in welches Feld die Punkte eingetragen werden sollen,
        nutzt dabei die bisherigen Präferenzen und passt sie nach dem Wurf an.
        """
        kategorien_punkte = self.analyze_dice(wuerfel_werte)
        freie_kategorien = [
            kat for kat, pkt in punktetafel[self.name].items() if pkt is None
        ]

        # Wir wählen die Kategorie nicht nur nach erzielbaren Punkten,
        # sondern multiplizieren die Punkte mit unserer gelernten Kategorie-Präferenz.
        beste_kategorie = None
        bester_wert = -float('inf')

        for kategorie in freie_kategorien:
            reine_punkte = kategorien_punkte.get(kategorie, 0)
            # Effektiver Wert = Punkte * Präferenz
            effektiver_wert = reine_punkte * self.category_preferences.get(kategorie, 1.0)
            if effektiver_wert > bester_wert:
                bester_wert = effektiver_wert
                beste_kategorie = kategorie

        # Entscheidung protokollieren
        self.decision_log.append({
            "aktion": "feld_waehlen",
            "wuerfel_werte": wuerfel_werte,
            "ausgewaehlte_kategorie": beste_kategorie
        })

        # --- EINFACHES LERNEN ---
        # Nach Wahl der Kategorie "lernt" der Bot, ob es eine gute Wahl war:
        # Hier vereinfachen wir und gehen davon aus, dass hohe Punkte = gute Wahl.
        # Man könnte das z.B. noch mit dem Spielverlauf vergleichen (z.B. Endergebnis).
        if beste_kategorie is not None:
            erzielte_punkte = kategorien_punkte.get(beste_kategorie, 0)
            alte_praeferenz = self.category_preferences[beste_kategorie]

            # Beispiel: neue Präferenz = alte Präferenz + learning_rate * (Erfolg - alte_Präferenz)
            # "Erfolg" definieren wir hier als normalisierte Punktzahl (0 bis 1)
            erfolgswert = min(erzielte_punkte / 50.0, 1.0)  # max. 50 Punkte = Kniffel
            neue_praef = alte_praeferenz + self.learning_rate * (erfolgswert - alte_praeferenz)
            self.category_preferences[beste_kategorie] = neue_praef

        return beste_kategorie


class Martinelli_2(Kniffel_Player):
    def __init__(self, name):
        self.name = name #Erstellt KI mit Namen (self.name), für Scoreboard relevant
    #Analysiert die Würfelergebnisse und gibt eine Übersicht zurück
    def Würfel_Auswertung(self, dice_list):
        Würfel_Output = {} #Leeres Dictonary speichert mögliche Punkte für jede Kategorie
        Summe_der_Würfel= sum(dice_list) #Summe aller Würfelaugen
        count_of_dice = [dice_list.count(i) for i in range(1, 7)]#Ein Array mit der Anzahl der jeweiligen Würfel 
        for top in range(6):#Berechnung für Einser bis Sechser
            Würfel_Output["Einser"] = count_of_dice[0] * 1
            Würfel_Output["Zweier"] = count_of_dice[1] * 2
            Würfel_Output["Dreier"] = count_of_dice[2] * 3
            Würfel_Output["Vierer"] = count_of_dice[3] * 4
            Würfel_Output["Fünfer"] = count_of_dice[4] * 5
            Würfel_Output["Sechser"] = count_of_dice[5] * 6
    #Berechnung übriger Felder
        if any(count >= 3 for count in count_of_dice):#
            Würfel_Output["Dreierpasch"] = Summe_der_Würfel
        if any(count >= 4 for count in count_of_dice):
            Würfel_Output["Viererpasch"] = Summe_der_Würfel
    
        if set([1, 2, 3, 4, 5]).issubset(dice_list) or set([2, 3, 4, 5, 6]).issubset(dice_list):
            Würfel_Output["Große Straße"] = 40 #Prüft ob ein set in einem anderen set enthalten ist
    
        kleine_straße = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        if any(set(straight).issubset(dice_list) for straight in kleine_straße):
            Würfel_Output["Kleine Straße"] = 30
    
        if 3 in count_of_dice and 2 in count_of_dice:
            Würfel_Output["Full House"] = 25
    
        if 5 in count_of_dice:
            Würfel_Output["Kniffel"] = 50
    
        Würfel_Output["Chance"] = Summe_der_Würfel
    
        return Würfel_Output
    
    def simulation_zukünftiger_Würfe(self, kept_dices, scoreboard, num_simulations=2000):
    #Simuliert zukünftige Würfe, um die erwarteten Punkte für jede Möglichkeit zu berechnen.
        total_score = 0 #Gesamtscore zu Beginn
        valid_simulations = 0 #Gültige Simulationen zu Beginn
        
        for i in range(num_simulations):
            new_rolls = [random.randint(1, 6) for _ in range(5 - len(kept_dices))]
            dice_combination = kept_dices + new_rolls
            possible_scores = self.Würfel_Auswertung(dice_combination)

            possible_scores = {
                category: score for category, score in possible_scores.items()
                if scoreboard[self.name].get(category) is None}

            if possible_scores:
                total_score += max(possible_scores.values())
                valid_simulations += 1

        return total_score / valid_simulations if valid_simulations > 0 else 0
    
    #Entscheidet, welche Würfel gehalten werden sollen
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        best_dices_to_hold = [] #Zu beginn leere Liste
        best_average_score = -float('inf') #Bester Score zu beginn auf -unendlich

        #Generiert alle möglichen Kombinationen von Würfeln, die gehalten werden können
        Mögliche_Würfelkombinationen = [list(comb) for i in range(len(dice_rolls) + 1) 
                                    for comb in itertools.combinations(dice_rolls, i)]

        for held_dices in Mögliche_Würfelkombinationen:
            #Simuliert zukünftige Würfe und berechne den Durchschnittsscore
            average_score = self.simulation_zukünftiger_Würfe(held_dices, scoreboard)
            #wird immer um besten Durchschnittsscore aktualisiert
            if average_score > best_average_score:
                best_average_score = average_score
                best_dices_to_hold = held_dices

        return best_dices_to_hold
    
    #Entscheidet, in welches Feld die Punkte eingetragen werden sollen.
    def decide_which_field_to_enter(self, scoreboard, dice_values):
   
        category_points = self.Würfel_Auswertung(dice_values)
        #Greift auf alle freien Kategorien des Scoreboardes des Spielers zurück und guckt welche Kategorien none sind
        available_categories = [cat for cat, score in scoreboard[self.name].items() if score is None]
        
    
        #Priorisiert Bonusfelder
        Obere_Sektion = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]
        #Hier umgekehrt nimmt die Summe aller Kategorien aus oberer Sektion die belegt sind um Differenz zum Bonus zu bestimmen
        Bonus_Differenz = 63 - sum(scoreboard[self.name][cat] or 0 for cat in Obere_Sektion if scoreboard[self.name][cat] is not None)
        Schwierigkeits_Gewichtung = {"Kniffel":-15, "Viererpasch":-10,"Full House":-5,"Große Straße":-3}
        best_category = None #Gleiches Vorgehen
        best_score = -float('inf')
        for category in available_categories:
            category_score = category_points.get(category, 0)
            # Streicht schwerer erreichbarer Felder priorisieren
            if category_score == 0:  #Wenn keine Punkte erzielt werden können
                category_score += Schwierigkeits_Gewichtung.get(category, 0)
           
            #Priorisierung Bonusfelder, aber nur, wenn der Bonus erreichbar ist
            if category in Obere_Sektion and Bonus_Differenz > 0:
                # Gewichtung für Bonusfelder
                category_score += 10
                    #Priorisierung Viererpasch gegenüber Dreierpasch
            if category == "Viererpasch":
                category_score += 1  #Gewichtung für Viererpasch
            elif category == "Dreierpasch":
                category_score -= 5  #Verringerung für Dreierpasch
            
            #Auswahl der Kategorie mit der höchsten Punktzahl
            if category_score > best_score:
                best_score = category_score
                best_category = category
        
        return best_category


class Reibel_1(Kniffel_Player): #init wird benötigt, um Klasse zu erstelen.

    def __init__(self, name): #self verbindet Funktionen mit entspr. Klasse. bzw. Attribute der Klasse nutzen
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        if roll == 0:
            print_scoreboard(self.name, scoreboard)

        combined_dices = kept_dices + dice_rolls 
        dice_counts = Counter(combined_dices)
        repeated_values = [value for value, count in dice_counts.items() if count > 1]
        repeated_values.sort(reverse=True)
        most_common_value, most_common_count = dice_counts.most_common(1)[0]
        
        # Ab hier regelbasiert durch if/else, also unter welchen Bedingungen welche Würfel gehalten werden
        hold = []
        available_field = 0
        for field in scoreboard:
            if field is None:
                available_field+=1 # Zählt jede Runde alle offenen Felder

        if scoreboard.get(self.name).get("Große Straße") is None and (
                set(combined_dices) >= {2, 3, 4, 5, 6} or set(combined_dices) >= {1, 2, 3, 4, 5}): # set ist eine Datenstruktur, die repeated value ignoriert, damit auf Abfolge (Straßen) gegangen werden kann.
            return dice_rolls

        if scoreboard.get(self.name).get("Kleine Straße") is None and (
                set(combined_dices) >= {1, 2, 3, 4} or set(combined_dices) >= {2, 3, 4, 5} or set(combined_dices) >= {3,4,5,6}):
            return set(dice_rolls)

        if scoreboard.get(self.name).get("Full House") is None:
            if available_field == 1:
                top_two = sorted(dice_counts.items(), key=lambda x: -x[1])[:2] # top two wandelt die vorliegenden Würfel in Tupel und sortiert diese nach absteigender Reihenfolge (Meiste Anzahl bis niedrigste Anzahl); :2 zwei heißt -> ersten beiden Tupel
                hold = [die for die in combined_dices if
                        die in [top_two[0][0], top_two[1][0]] and dice_counts[die] <= 3]
                return hold
            elif scoreboard.get(self.name).get("Full House") is None and sorted(dice_counts.values()) == [2, 3]:
                return dice_rolls

        if (roll == 0 or roll == 1) and most_common_count >= 2:
            if scoreboard.get(self.name).get("Sechser") is None and 6 in repeated_values:
                hold = [die for die in dice_rolls if die == 6]
                return hold

            if scoreboard.get(self.name).get("Fünfer") is None and 5 in repeated_values:
                hold = [die for die in dice_rolls if die == 5]
                return hold

            if scoreboard.get(self.name).get("Vierer") is None and 4 in repeated_values:
                hold = [die for die in dice_rolls if die == 4]
                return hold

            if scoreboard.get(self.name).get("Dreier") is None and 3 in repeated_values:
                hold = [die for die in dice_rolls if die == 3]
                return hold

            if scoreboard.get(self.name).get("Zweier") is None and 2 in repeated_values:
                hold = [die for die in dice_rolls if die == 2]
                return hold

            if scoreboard.get(self.name).get("Einser") is None and 1 in repeated_values:
                hold = [die for die in dice_rolls if die == 1]
                return hold

        if scoreboard.get(self.name).get("Kniffel") is None and most_common_count >=3 :
            return [die for die in dice_rolls if die == most_common_value]


        if scoreboard.get(self.name).get("Viererpasch") is None and most_common_count >= 3:
            hold = [die for die in combined_dices if die == most_common_value]
            if most_common_count ==4:
                hold.append(die for die in combined_dices if die in [5,6]) # Zusätzliche Augen sollen wenn möglich 5er oder 6er sein
            return hold

        if scoreboard.get(self.name).get("Dreierpasch") is None and most_common_count >= 2:
            hold = [die for die in combined_dices if die == most_common_value ]
            if most_common_count ==3:
                hold.append(die for die in combined_dices if die in [5,6]) 
            return hold

        return []

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        dice_counts = Counter(dice_values)
        most_common = dice_counts.most_common(1)

        if most_common:
            most_common_value, most_common_count = most_common[0]

            if scoreboard.get(self.name).get("Kniffel") is None and most_common_count == 5:
                return "Kniffel"

            field_scores = {}
            if scoreboard.get(self.name).get("Sechser") is None and most_common_value == 6 and most_common_count >= 3:
                field_scores["Sechser"] = sum(die for die in dice_values if die == 6)

            if scoreboard.get(self.name).get("Fünfer") is None and most_common_value == 5 and most_common_count >= 3:
                field_scores["Fünfer"] = sum(die for die in dice_values if die == 5)

            if scoreboard.get(self.name).get("Vierer") is None and most_common_value == 4 and most_common_count >= 3:
                field_scores["Vierer"] = sum(die for die in dice_values if die == 4)

            if scoreboard.get(self.name).get("Dreier") is None and most_common_value == 3 and most_common_count >= 3:
                field_scores["Dreier"] = sum(die for die in dice_values if die == 3)

            if scoreboard.get(self.name).get("Zweier") is None and most_common_value == 2 and most_common_count >= 2:
                field_scores["Zweier"] = sum(die for die in dice_values if die == 2)

            if scoreboard.get(self.name).get("Einser") is None and most_common_value == 1 and most_common_count >= 2:
                field_scores["Einser"] = sum(die for die in dice_values if die == 1)
                
            # Im folgenden Codeabschnitt wird auf Basis der Felderwerte sortiert. Z.B. Dictionary [("Einser",2)] & [("Sechser",18)].
            # Die sorted-Funktion sortiert das dictionary so:[("Sechser",18)], [("Einser",2)], da 18 > 3.
            # x(1) ist der value aus dem dictionary, nach dem die keys sortiert werden.
            sorted_fields = sorted(field_scores.items(), key=lambda x: x[1], reverse=True)
            if sorted_fields:
                selected_field, _ = sorted_fields[0]
                print(f"Selected field: {selected_field}")
                print("\n\n")
                return selected_field
            
            # Sicherstellung, dass dictionary leer ist.
            # Wir könnten field_scores entfernen, weil wir zuvor immer Punkte vergeben, wenn etwas gewertet wurde.
            field_scores.clear()
            if scoreboard.get(self.name).get("Full House") is None and sorted(dice_counts.values()) == [2, 3]:
                field_scores["Full House"] = 25

            if scoreboard.get(self.name).get("Große Straße") is None and (set(dice_values) == {2, 3, 4, 5, 6} or set(dice_values) == {1, 2, 3, 4, 5}):
                field_scores["Große Straße"] = 40

            if scoreboard.get(self.name).get("Kleine Straße") is None and (set(dice_values) >= {1, 2, 3, 4} or set(dice_values) >= {2, 3, 4, 5} or set(dice_values) >= {3, 4, 5, 6}):
                field_scores["Kleine Straße"] = 30

            if scoreboard.get(self.name).get("Viererpasch") is None and most_common_count >= 4:
                field_scores["Viererpasch"] = sum(dice_values)

            if scoreboard.get(self.name).get("Dreierpasch") is None and most_common_count >= 3:
                field_scores["Dreierpasch"] = sum(dice_values)

            sorted_fields = sorted(field_scores.items(), key=lambda x: x[1], reverse=True) 
            if sorted_fields:
                selected_field, _ = sorted_fields[0]
                print(f"Selected field: {selected_field}")
                print("\n\n")
                return selected_field
        
        fallback_value = self.deciding_fallback_value(scoreboard)

        return fallback_value

    def deciding_fallback_value(self, scoreboard):
        if scoreboard.get(self.name).get('Chance') is None:
            return "Chance"
        if scoreboard.get(self.name).get('Kniffel') is None:
            return "Kniffel"
        if scoreboard.get(self.name).get('Viererpasch') is None:
            return "Viererpasch"
        if scoreboard.get(self.name).get("Einser") is None:
            return "Einser"
        if scoreboard.get(self.name).get('Große Straße') is None:
            return "Große Straße"
        if scoreboard.get(self.name).get("Zweier") is None:
            return "Zweier"
        if scoreboard.get(self.name).get("Dreier") is None:
            return "Dreier"
        if scoreboard.get(self.name).get("Vierer") is None:
            return "Vierer"
        if scoreboard.get(self.name).get("Fünfer") is None:
            return "Fünfer"
        if scoreboard.get(self.name).get("Sechser") is None:
            return "Sechser"
        if scoreboard.get(self.name).get('Kleine Straße') is None:
            return "Kleine Straße"
        if scoreboard.get(self.name).get('Full House') is None:
            return "Full House"
        return None


class Reibel_2(Kniffel_Player):
    def __init__(self, name):
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        if roll == 0:
            print_scoreboard(self.name, scoreboard)

        combined_dices = kept_dices + dice_rolls
        dice_counts = Counter(combined_dices)
        repeated_values = [value for value, count in dice_counts.items() if count > 1]
        repeated_values.sort(reverse=True)
        most_common_value, most_common_count = dice_counts.most_common(1)[0]

        hold = []
        available_field = 0
        for field in scoreboard:
            if field is None:
                available_field += 1

        if scoreboard.get(self.name).get("Kniffel") is None and most_common_count >= 2:
            return [die for die in dice_rolls if die == most_common_value]

        if scoreboard.get(self.name).get("Große Straße") is None and (
                set(combined_dices) >= {2, 3, 4, 5, 6} or set(combined_dices) >= {1, 2, 3, 4, 5}):
            return dice_rolls

        if scoreboard.get(self.name).get("Kleine Straße") is None and (
                set(combined_dices) >= {1, 2, 3, 4} or set(combined_dices) >= {2, 3, 4, 5} or set(combined_dices) >= {3,4,5,6}):
            return set(dice_rolls)

        if scoreboard.get(self.name).get("Full House") is None:
            if available_field == 1:
                top_two = sorted(dice_counts.items(), key=lambda x: -x[1])[:2]
                hold = [die for die in combined_dices if
                        die in [top_two[0][0], top_two[1][0]] and dice_counts[die] <= 3]
                return hold
            elif scoreboard.get(self.name).get("Full House") is None and sorted(dice_counts.values()) == [2, 3]:
                return dice_rolls

        if scoreboard.get(self.name).get("Viererpasch") is None and most_common_count >= 3:
            hold = [die for die in combined_dices if die == most_common_value]
            if most_common_count == 4:
                hold.append(die for die in combined_dices if die in [5, 6])
            return hold

        if scoreboard.get(self.name).get("Dreierpasch") is None and most_common_count >= 2:
            hold = [die for die in combined_dices if die == most_common_value]
            if most_common_count == 3:
                hold.append(die for die in combined_dices if die in [5, 6])
            return hold

        if (roll == 0 or roll == 1) and most_common_count >= 2:
            if scoreboard.get(self.name).get("Sechser") is None and 6 in repeated_values:
                hold = [die for die in dice_rolls if die == 6]
                return hold

            if scoreboard.get(self.name).get("Fünfer") is None and 5 in repeated_values:
                hold = [die for die in dice_rolls if die == 5]
                return hold

            if scoreboard.get(self.name).get("Vierer") is None and 4 in repeated_values:
                hold = [die for die in dice_rolls if die == 4]
                return hold

            if scoreboard.get(self.name).get("Dreier") is None and 3 in repeated_values:
                hold = [die for die in dice_rolls if die == 3]
                return hold

            if scoreboard.get(self.name).get("Zweier") is None and 2 in repeated_values:
                hold = [die for die in dice_rolls if die == 2]
                return hold

            if scoreboard.get(self.name).get("Einser") is None and 1 in repeated_values:
                hold = [die for die in dice_rolls if die == 1]
                return hold

        return []

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        dice_counts = Counter(dice_values)
        most_common = dice_counts.most_common(1)

        if most_common:
            most_common_value, most_common_count = most_common[0]

            if scoreboard.get(self.name).get("Kniffel") is None and most_common_count == 5:
                return "Kniffel"
        
            field_scores = {}
            if scoreboard.get(self.name).get("Full House") is None and sorted(dice_counts.values()) == [2, 3]:
                field_scores["Full House"] = 25

            if scoreboard.get(self.name).get("Große Straße") is None and (
                    set(dice_values) >= {2, 3, 4, 5, 6} or set(dice_values) >= {1, 2, 3, 4, 5}):
                field_scores["Große Straße"] = 40

            if scoreboard.get(self.name).get("Kleine Straße") is None and (
                    set(dice_values) >= {1, 2, 3, 4} or set(dice_values) >= {2, 3, 4, 5} or set(dice_values) >= {3, 4, 5, 6}):
                field_scores["Kleine Straße"] = 30
            if scoreboard.get(self.name).get("Viererpasch") is None and most_common_count >= 4:
                field_scores["Viererpasch"] = sum(dice_values)

            if scoreboard.get(self.name).get("Dreierpasch") is None and most_common_count >= 3:
                field_scores["Dreierpasch"] = sum(dice_values)

            sorted_fields = sorted(field_scores.items(), key=lambda x: x[1], reverse=True)
            if sorted_fields:
                selected_field, _ = sorted_fields[0]
                print(f"Selected field: {selected_field}")
                print("\n\n")
                return selected_field

            field_scores.clear()
            if scoreboard.get(self.name).get("Sechser") is None and most_common_value == 6 and most_common_count >= 3:
                field_scores["Sechser"] = sum(die for die in dice_values if die == 6)

            if scoreboard.get(self.name).get("Fünfer") is None and most_common_value == 5 and most_common_count >= 3:
                field_scores["Fünfer"] = sum(die for die in dice_values if die == 5)

            if scoreboard.get(self.name).get("Vierer") is None and most_common_value == 4 and most_common_count >= 3:
                field_scores["Vierer"] = sum(die for die in dice_values if die == 4)

            if scoreboard.get(self.name).get("Dreier") is None and most_common_value == 3 and most_common_count >= 3:
                field_scores["Dreier"] = sum(die for die in dice_values if die == 3)

            if scoreboard.get(self.name).get("Zweier") is None and most_common_value == 2 and most_common_count >= 2:
                field_scores["Zweier"] = sum(die for die in dice_values if die == 2)

            if scoreboard.get(self.name).get("Einser") is None and most_common_value == 1 and most_common_count >= 2:
                field_scores["Einser"] = sum(die for die in dice_values if die == 1)

            sorted_fields = sorted(field_scores.items(), key=lambda x: x[1], reverse=True)
            if sorted_fields:
                selected_field, _ = sorted_fields[0]
                print(f"Selected field: {selected_field}")
                print("\n\n")
                return selected_field

        fallback_value = self.deciding_fallback_value(scoreboard)
        if fallback_value is not None:
            print(f"Fallback field: {fallback_value}")
            print("\n\n")
        else:
            print("No field to cross, letting the game cross")
            print("\n\n")

        return fallback_value

    def deciding_fallback_value(self, scoreboard):
        if scoreboard.get(self.name).get('Chance') is None:
            return "Chance"
        if scoreboard.get(self.name).get('Viererpasch') is None:
            return "Viererpasch"
        if scoreboard.get(self.name).get("Einser") is None:
            return "Einser"
        if scoreboard.get(self.name).get('Große Straße') is None:
            return "Große Straße"
        if scoreboard.get(self.name).get("Zweier") is None:
            return "Zweier"
        if scoreboard.get(self.name).get("Dreier") is None:
            return "Dreier"
        if scoreboard.get(self.name).get("Vierer") is None:
            return "Vierer"
        if scoreboard.get(self.name).get("Fünfer") is None:
            return "Fünfer"
        if scoreboard.get(self.name).get("Sechser") is None:
            return "Sechser"
        if scoreboard.get(self.name).get('Kleine Straße') is None:
            return "Kleine Straße"
        if scoreboard.get(self.name).get('Full House') is None:
            return "Full House"
        if scoreboard.get(self.name).get('Kniffel') is None:
            return "Kniffel"

        return None

class Schmitt_1(Kniffel_Player):
    def __init__(self, name):
        "Name should be a string"
        self.name = name
        
        
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
                
    # Verhaltensweise für den ersten Wurf (roll == 0)
        if roll == 0:            
            return self.first_roll(dice_rolls, kept_dices, scoreboard)
        
    # Verhaltensweise für den zweiten Wurf (roll == 1)
        if roll == 1:           
            return self.second_roll(dice_rolls, kept_dices, scoreboard)
        
        
 # Funktion für die Verhaltensweisen beim ersten Wurf
    def first_roll(self, dice_rolls, kept_dices, scoreboard):
        
    # Dictionary mit den gewürfelten Augenzahlen als keys und deren Häufigkeit als values
        counts = {value: dice_rolls.count(value) for value in set(dice_rolls)}  
    
    # Liste der Felder im scoreboard, die noch keinen Eintrag haben
        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]

    # Augenzahlen und die dazugehörigen Strings
        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}

        print("First Roll - Dice Rolls:", dice_rolls)
        print("First Roll - Counts:", counts)

    # for-Schleife durchläuft absteigend, die für einen risikoaffinen Spieler wichtigsten Felder
        for value, count in counts.items():  # Iteriert durch alle "key-value-Paare" des dictionaries "counts"
            
        # Überprüft auf Kniffel
            if count == 5:
            
            # "any" überprüft, ob mindestens eines der Felder noch in available_fields verfügabr ist
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):

                    print("Kniffel erkannt!")
                    kept_dices = [value] * 5  
                    return kept_dices

        # Überprüft auf große Straße       
        
        # "all" stellt sicher, dass ALLE der für die "Große Straße" benötigten Werte vorhanden sind
            elif all(value in dice_rolls for value in [1, 2, 3, 4, 5]) or all(value in dice_rolls for value in [2, 3, 4, 5, 6]):  
                
                if "Große Straße" in available_fields:
                
                    print("Große Straße erkannt!")
                    kept_dices = dice_rolls
                    return kept_dices
        
        # Überprüft auf kleine Straße
            elif all(value in dice_rolls for value in [1, 2, 3, 4]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (1-4)")
                    kept_dices = [1, 2, 3, 4]  # Behalte nur die Würfel der Straße [1, 2, 3, 4]
                    return kept_dices
            
            elif all(value in dice_rolls for value in [2, 3, 4, 5]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (2-5)")
                    kept_dices = [2, 3, 4, 5]  # Behalte nur die Würfel der Straße [2, 3, 4, 5]
                    return kept_dices
            
            elif all(value in dice_rolls for value in [3, 4, 5, 6]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (3-6)")
                    kept_dices = [3, 4, 5, 6]  # Behalte nur die Würfel der Straße [3, 4, 5, 6]
                    return kept_dices


        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():                
                
                if "Full House" in available_fields:
                
                    print("Full House erkannt!")
                    kept_dices = dice_rolls
                    return kept_dices

        # Überprüft auf Viererpasch
            elif count >= 4:  
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):
                
                    print("Viererpasch erkannt!")
                    kept_dices = [value] * 4  
                    return kept_dices

        # Überprüft auf Dreierpasch
            elif count >= 3:  
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Full House", numbers[value]]):
                
                    print("Dreierpasch erkannt!")
                    kept_dices = [value] * 3  
                    return kept_dices

        
    # Überprüft auf 5er und 6er
        for value, count in counts.items():     # Neue for-Schleife, da Iteration sonst nach dem ersten gefundenen Wert stoppt
            
            if value in (5,6):
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Chance", numbers[value]]):
                    print("Überprüfe auf 5er und 6er...")
    
                # Zähle die Häufigkeiten von 6 und 5
                    count_6 = dice_rolls.count(6)
                    count_5 = dice_rolls.count(5)
    
                # Augenzahl mit größter Häufigkeit wird behalten
                    if count_6 > count_5:
                        print(f"Behalte die 6er: {count_6} mal")
                        kept_dices = [6] * count_6  
                    elif count_5 > count_6:
                        print(f"behalte die 5er: {count_5} mal")
                        kept_dices = [5] * count_5  
                    else:  # Gleich viele 5er und 6er
                        print(f"Gleiche Anzahl 5er und 6er: {count_6}. Behalte die 6er.")
                        kept_dices = [6] * count_6  # Behalte die 6er, da sie die höhere Augenzahl haben    
                    return kept_dices
            
            # Wenn keine 5er und 6er vorhanden sind, behalte Augenzahl die am häufigsten vorkommt
                elif value in (1,2,3,4):
                    
                    if numbers[value] in available_fields:                    
                        print("Überprüfe auf Augenzahlen 1 bis 4...")
                
                        highest_count = 0
                
                        if count > highest_count:
                            highest_count = count
                            print(f"Behalte die {value}er: {highest_count} mal")
                            kept_dices = [value] * highest_count
                        return kept_dices
        
    # Wenn keine Kombination gefunden wird, werden keine Würfel behalten
        print("Keine Kombination gefunden. Behalte keine Würfel.")
        kept_dices = []  
        return kept_dices
    

# Funktion für die Verhaltensweise beim zweiten Wurf    
    def second_roll(self, dice_rolls, kept_dices, scoreboard):
    
    # Liste mit kept_dices aus dem ersten Wurf und den dice_rolls aus dem zweiten Wurf
        combined_dices = kept_dices + dice_rolls    
    
    # Dictionary mit den Augenzahlen aus combined_dices als keys und deren Häufigkeit als values   
        counts = {value: combined_dices.count(value) for value in set(combined_dices)}
        
        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]

        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}
        
        print("Second Roll - Kept Dices:", kept_dices)
        print("Second Roll - Dice Rolls:", dice_rolls)
        print("Second Roll - Combined Dices:", combined_dices)
        print("Second Roll - Counts:", counts)

    # for-Schleife durchläuft absteigend, die für einen risikoaffinen Spieler wichtigsten Felder
        for value, count in counts.items():
            
        # Überprüft auf Kniffel
            if count == 5:  
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):
                
                    print("Kniffel erkannt!")
                    kept_dices = dice_rolls
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                
                
        # Überprüft auf große Straße
            elif all(value in combined_dices for value in [1, 2, 3, 4, 5]) or all(value in combined_dices for value in [2, 3, 4, 5, 6]):
                
                if "Große Straße" in available_fields:
                               
                    print("Große Straße erkannt!")
                    kept_dices = dice_rolls
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                
                
        # Überprüft auf kleine Straße
            elif all(value in combined_dices for value in [1, 2, 3, 4]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (1-4)")
                    new_dices = [value for value in [1, 2, 3, 4] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [1, 2, 3, 4]
                    kept_dices = new_dices
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                
            elif all(value in combined_dices for value in [2, 3, 4, 5]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (2-5)")
                    new_dices = [value for value in [2, 3, 4, 5] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [2, 3, 4, 5]
                    kept_dices = new_dices
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                
            elif all(value in combined_dices for value in [3, 4, 5, 6]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (3-6)")
                    new_dices = [value for value in [3, 4, 5, 6] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [3, 4, 5, 6]
                    kept_dices = new_dices
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                
                
        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():                
                
                if "Full House" in available_fields:
                
                    print("Full House erkannt!")
                    kept_dices = dice_rolls
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)
                    return kept_dices
                    
                    
        # Überprüft auf Viererpasch        
            elif count >= 4:  
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):
                
                    print("Viererpasch erkannt!")                
                    kept_dices = [value] * (4 - kept_dices.count(value))
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)                            
                    return kept_dices
                
                
        # Überprüft auf Dreierpasch   
            elif count >= 3:  
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Full House", numbers[value]]):
                
                    print("Dreierpasch erkannt!")                
                    kept_dices = [value] * (3 - kept_dices.count(value))
                    print("Behaltene Würfel aus dem zweiten Wurf:", kept_dices)                
                    return kept_dices
                
            
            
    # Überprüft auf 6er und 5er
        for value, count in counts.items():
                
            if value in (5,6) and (5 in kept_dices or 6 in kept_dices):
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Chance", numbers[value]]):
                    print("Überprüfe auf 5er und 6er...")
        
                # Zähle die Häufigkeiten von 6 und 5
                    count_6 = kept_dices.count(6)
                    count_5 = kept_dices.count(5)
        
                # Entscheide, welche Zahl behalten werden soll
                    if count_6 > count_5:
                        print(f"Behalte die 6er: {count_6} mal")
                        kept_dices = [6] * dice_rolls.count(6) 
                    elif count_5 > count_6:
                        print(f"behalte die 5er: {count_5} mal")
                        kept_dices = [5] * dice_rolls.count(5)  
                    else:  # Gleich viele 5er und 6er
                        print(f"Gleiche Anzahl 5er und 6er in Kept Dices: {count_6}. Behalte die 6er.")
                        kept_dices = [6] * dice_rolls.count(6)  # Behalte die 6er, da sie die höhere Augenzahl haben
        
                    return kept_dices
            
                elif value in (1,2,3,4):
                    
                    if numbers[value] in available_fields:
                        
                        print("Überprüfe auf Augenzahlen 1 bis 4...")
                
                        count = kept_dices.count(value)
                        highest_count = 0
                
                        if count > highest_count:
                            highest_count = count
                            print(f"Behalte die {value}er: {highest_count} mal")
                            kept_dices = [value] * dice_rolls.count(value)
                        return kept_dices
                        
                
        
        print("Keine Kombination gefunden. Behalte keine Würfel.")
        kept_dices = []  
        return kept_dices

   
    
    
                
    
    def decide_which_field_to_enter(self, scoreboard, dice_values):          
        
        counts = {value: dice_values.count(value) for value in set(dice_values)}
    
        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]
        
        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}
        
        print("Dice Values:", dice_values)
        print("Available Fields:", available_fields)
        
        for value, count in counts.items():
        
            if count == 5:
                
                if "Kniffel" in available_fields:
                    
                    print("Kniffel gefunden, Wert: 50 Punkte")      
                    return "Kniffel"
            
        # Überprüft auf große Straße
            elif all(value in dice_values for value in [1, 2, 3, 4, 5]) or all(value in dice_values for value in [2, 3, 4, 5, 6]):      # "all" überprüft die spezifische Kombination
                
                if "Große Straße" in available_fields:    
                    
                    print("Große Straße gefunden, Wert: 40 Punkte")
                    return "Große Straße"
            
        # Überprüft auf kleine Straße
            elif all(value in dice_values for value in [1,2,3,4]) or all(value in dice_values for value in [2,3,4,5]) or all(value in dice_values for value in [3,4,5,6]):
                
                if "Kleine Straße" in available_fields:
                    
                    print("Kleine Straße gefunden, Wert: 30 Punkte")
                    return "Kleine Straße"
            
        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():     # Überprüft die values (Häufigkeit eines Wertes) des dictionaries "counts"
                
                if "Full House" in available_fields: 
                    
                    print("Full House gefunden, Wert: 25 Punkte")            
                    return "Full House"
                
        # Überprüft auf Viererpasch 
            elif count >= 4:
                
                if "Viererpasch" in available_fields and sum(dice_values) >= 21:
                                    
                    print(f"Viererpasch gefunden, Wert: {sum(dice_values)} Punkte")            
                    return "Viererpasch"
                    
        # Überprüft auf Dreierpasch 
            elif count >= 3:
                
                if "Dreierpasch" in available_fields and sum(dice_values) >= 17:
                                                        
                    print(f"Dreierpasch gefunden, Wert: {sum(dice_values)} Punkte")           
                    return "Dreierpasch"
            
            
            
    # Überprüft auf oberen Teil    
        most_frequent_dice = None
        highest_count = 0
        highest_count_value = 0

        least_valuable_dice = None
        lowest_value = float('inf')  
        lowest_value_count = 0

        for value, count in counts.items():
            
            if numbers[value] in available_fields:
            
            # Augenzahl wählen, die mindestens dreimal vorkommt und am größten ist
                if  count >= 3 and count > highest_count:
                    highest_count = count
                    highest_count_value = value
                    most_frequent_dice = numbers[value]
        
            # Alternativ: Augenzahl wählen, die am kleinsten ist
                elif value < lowest_value:
                    lowest_value = value
                    lowest_value_count = count
                    least_valuable_dice = numbers[value]

    # Priorität: Zahl mit mindestens 3 Vorkommen
        if most_frequent_dice:
            print(f"{most_frequent_dice} gefunden, Wert: {highest_count * highest_count_value} Punkte")
            return most_frequent_dice

    # Wenn keine Augenzahl mindestens dreimal vorkam, Würfel mit geringster Augenzahl wählen
        if least_valuable_dice:
            print(f"{least_valuable_dice} gefunden, Wert: {lowest_value * lowest_value_count} Punkte")
            return least_valuable_dice    
    
    # Überprüft auf Chance
        if sum(dice_values) >= 20:
                       
            if "Chance" in available_fields:
                           
                print(f"Chance gefunden, Wert: {sum(dice_values)} Punkte")            
                return "Chance"
            

class Schmitt_2(Kniffel_Player):
    def __init__(self, name):
        "Name should be a string"
        self.name = name
        
        
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
               
    # Verhaltensweise für den ersten Wurf (roll == 0)
        if roll == 0:
            
            return self.first_roll(dice_rolls, kept_dices, scoreboard)
        
    # Verhaltensweise für den zweiten Wurf (roll == 1)
        if roll == 1:
            
            return self.second_roll(dice_rolls, kept_dices, scoreboard)
        
        
 # Funktion für die Verhaltensweisen beim ersten Wurf
    def first_roll(self, dice_rolls, kept_dices, scoreboard):
        
        counts = {value: dice_rolls.count(value) for value in set(dice_rolls)}  # Dictionary mit den Augenzahlen als keys und deren Häufigkeit als values
        
        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]
        
        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}
        
        print("First Roll - Dice Rolls:", dice_rolls)
        print("First Roll - Counts:", counts)

    # for-Schleife durchläuft absteigend, die für einen risikoaffinen Spieler wichtigsten Felder
        for value, count in counts.items():  # Iteriert durch alle "key-value-Paare" des dictionaries "counts"
            

        # Überprüft auf Kniffel
            if count == 5:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):       
                    
                    print("Kniffel erkannt!")
                    kept_dices = [value] * 5  
                    return kept_dices

        # Überprüft auf große Straße
            elif all(value in dice_rolls for value in [1, 2, 3, 4, 5]) or all(value in dice_rolls for value in [2, 3, 4, 5, 6]):
                
                if "Große Straße" in available_fields:
                    
                    print("Große Straße erkannt!")
                    kept_dices = dice_rolls  # Behalte alle Würfel für die große Straße
                    return kept_dices
                
        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():
            
            # Werte aus denen das Full House besteht
                values = [value for value, count in counts.items() if count in [2,3]]
            
            # Liste der Werte des Full House, die nicht mehr in available_fields sind
            # "True", wenn beide Wert des Full House NICHT mehr in available_fields sind
                unavailable_values = all(numbers[value] not in available_fields for value in values) 

                if "Full House" in available_fields and unavailable_values:     
                
                    print("Full House erkannt!")
                    kept_dices = dice_rolls
                    return kept_dices
                
        
        # Überprüft auf Viererpasch
            elif count >= 4:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):       # Prüft, ob mind. eines der Felder verfügbar ist
                
                    print("Viererpasch erkannt!")
                    kept_dices = [value] * 4  # Speichert Viererpasch in kept_dices
                    return kept_dices

        # Überprüft auf Dreierpasch
            elif count >= 3:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Full House", numbers[value]]):       # Prüft, ob mind. eines der Felder verfügbar ist
                
                    print("Dreierpasch erkannt!")
                    kept_dices = [value] * 3  # Speichert Dreierpasch in kept_dices
                    return kept_dices
        
        # Überprüft auf zwei Gleiche  
            elif count >= 2:
            
                if numbers[value] in available_fields: 
                    
                    print("Zwei Gleiche erkannt!")
                    kept_dices = [value] * count
            
        if kept_dices:
            return kept_dices

        for value, count in counts.items():

            if all(value in dice_rolls for value in [1, 2, 3, 4]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (1-4)")
                    kept_dices = [1, 2, 3, 4]  # Behalte nur die Würfel der Straße [1, 2, 3, 4]
                    return kept_dices
                
            elif all(value in dice_rolls for value in [2, 3, 4, 5]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (2-5)")
                    kept_dices = [2, 3, 4, 5]  # Behalte nur die Würfel der Straße [2, 3, 4, 5]
                    return kept_dices
                
            elif all(value in dice_rolls for value in [3, 4, 5, 6]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (3-6)")
                    kept_dices = [3, 4, 5, 6]  # Behalte nur die Würfel der Straße [3, 4, 5, 6]
                    return kept_dices
        
    # Behält kleinste Augenzahl für freies Feld im oberen Teil    
        lowest_value = float('inf')
        
        for value, count in counts.items():
            print(f"Prüfe Augenzahl {value} mit Anzahl = {count}")
            
            if numbers[value] in available_fields:
                print(f"{numbers[value]} ist in available_fields")
            
                if value < lowest_value:
                    lowest_value = value
                    print(f"Behalte Würfel mit kleinster Augenzahl: {lowest_value}er")
                    kept_dices = [lowest_value] * count
        
        if kept_dices:
            return kept_dices

    # Behält höchste Augenzahl, wenn es kein freies Feld im oberen Teil mehr gibt
        highest_value = 0
        
        for value, count in counts.items():
            print(f"Prüfe Augenzahl {value} mit Anzahl = {count}")
            
            if value > highest_value:
                highest_value = value
                print(f"Behalte Würfel mit höchster Augenzahl: {highest_value}er")
                kept_dices = [highest_value] * count
        
        if kept_dices:
            return kept_dices
                                               
    # Wenn keine Kombination gefunden wird, werden keine Würfel behalten
        print("Keine Kombination gefunden. Behalte keine Würfel.")
        kept_dices = []  
        return kept_dices
    

# Funktion für die Verhaltensweise beim zweiten Wurf    
    def second_roll(self, dice_rolls, kept_dices, scoreboard):
        
        combined_dices = kept_dices + dice_rolls
        
        counts = {value: combined_dices.count(value) for value in set(combined_dices)}  # Erstellt ein Dictionary mit den einzigartigen Werten als keys und deren Häufigkeit als values

        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]
        
        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}
        
        print("Second Roll - Kept Dices:", kept_dices)
        print("Second Roll - Dice Rolls:", dice_rolls)
        print("Second Roll - Combined Dices:", combined_dices)
        print("Second Roll - Counts:", counts)

    # for-Schleife durchläuft absteigend, die für einen risikoaffinen Spieler wichtigsten Felder
        for value, count in counts.items():  # Iteriert durch alle "key-value-Paare" des dictionaries "counts"
            

        # Überprüft auf Kniffel
            if count == 5:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):       # Prüft, ob mind. eines der Felder verfügbar ist
                    
                    print("Kniffel erkannt!")
                    kept_dices = dice_rolls  # Speichert Kniffel in kept_dices
                    return kept_dices

        # Überprüft auf große Straße
            elif all(value in dice_rolls for value in [1, 2, 3, 4, 5]) or all(value in dice_rolls for value in [2, 3, 4, 5, 6]):
                
                if "Große Straße" in available_fields:
                    
                    print("Große Straße erkannt!")
                    kept_dices = dice_rolls  # Behalte alle Würfel für die große Straße
                    return kept_dices
                
        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():

            # Werte aus denen das Full House besteht
                values = [value for value, count in counts.items() if count in [2,3]]
            # Liste der Werte des Full House, die nicht mehr in available_fields sind
                unavailable_values = all(numbers[value] not in available_fields for value in values) # Gibt "True" zurück, wenn beide Wert des Full House NICHT mehr in available_fields sind

                if "Full House" in available_fields and unavailable_values:
                
                    print("Full House erkannt!")
                    kept_dices = dice_rolls
                    return kept_dices
        
        # Überprüft auf Viererpasch
            elif count >= 4:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", numbers[value]]):       # Prüft, ob mind. eines der Felder verfügbar ist
                
                    print("Viererpasch erkannt!")
                    kept_dices = [value] * (4 - kept_dices.count(value))  # Speichert Viererpasch in kept_dices
                    return kept_dices

        # Überprüft auf Dreierpasch
            elif count >= 3:
                
                if any(field in available_fields for field in ["Kniffel", "Viererpasch", "Dreierpasch", "Full House", numbers[value]]):       # Prüft, ob mind. eines der Felder verfügbar ist
                
                    print("Dreierpasch erkannt!")
                    kept_dices = [value] * (3 - kept_dices.count(value))  # Speichert Dreierpasch in kept_dices
                    return kept_dices
        
        # Überprüft auf kleine Straße
        for value, count in counts.items():
            
            if all(value in combined_dices for value in [1, 2, 3, 4]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (1-4)")                    
                    new_dices = [value for value in [1, 2, 3, 4] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [1, 2, 3, 4]
                    kept_dices = new_dices
                    return kept_dices
                
            elif all(value in combined_dices for value in [2, 3, 4, 5]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (2-5)")
                    new_dices = [value for value in [2, 3, 4, 5] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [2, 3, 4, 5]
                    kept_dices = new_dices
                    return kept_dices
                
            elif all(value in combined_dices for value in [3, 4, 5, 6]):
                
                if any(field in available_fields for field in ["Kleine Straße", "Große Straße"]):
                
                    print("Kleine Straße erkannt! (3-6)")
                    new_dices = [value for value in [3, 4, 5, 6] if value in dice_rolls and value not in kept_dices]  # Behalte nur die Würfel der Straße [3, 4, 5, 6]
                    kept_dices = new_dices
                    return kept_dices
    
    # Überprüft auf zwei Gleiche        
        for value, count in counts.items():  # Durchlaufe alle Würfelwerte, um nach möglichen Paaren zu suchen
            
            if count >= 2:
        
            # Wenn das Feld für diesen Wert noch nicht belegt ist, behalte das Paar
                if numbers[value] in available_fields:                         
                    print("Zwei Gleiche erkannt!")
                        
                    if value in kept_dices:
                        kept_dices = [value] * (count - kept_dices.count(value))                        
                        
                    elif kept_dices == []:
                        kept_dices = [value] * count
                        
                    elif value not in kept_dices:
                        kept_dices = []
                        
        if kept_dices:
            return kept_dices
         
    # Behält kleinste Augenzahl für freies Feld im oberen Teil
        lowest_value = float('inf')
    
        for value, count in counts.items():
            
            if numbers[value] in available_fields:
                
                if value in kept_dices:
                    print(f'Behalte die {value}er')
                    kept_dices = [value] * (count - kept_dices.count(value))
            
                elif kept_dices == [] and value < lowest_value:
                    lowest_value = value
                    print(f"Behalte Würfel mit kleinster Augenzahl: {lowest_value}er")
                    kept_dices = [lowest_value] * (count - kept_dices.count(lowest_value))
                    
                elif value not in kept_dices:
                    kept_dices = []
                    
        if kept_dices:
            return kept_dices
            
    # Behält höchste Augenzahl, wenn es kein freies Feld im oberen Teil mehr gibt    
        highest_value = 0            
        
        for value, count in counts.items():
            
            if value in kept_dices:
                print(f'Behalte die {value}er')
                kept_dices = [value] * (count - kept_dices.count(value))
             
            elif kept_dices == [] and value > highest_value:                       
                highest_value = value
                print(f"Behalte Würfel mit höchster Augenzahl: {highest_value}er")
                kept_dices = [highest_value] * (count - kept_dices.count(highest_value))
            
            elif value not in kept_dices:
                kept_dices = []
            
        if kept_dices:
            return kept_dices
                
                                
    # Wenn keine Kombination gefunden wird, werden keine Würfel behalten
        print("Keine Kombination gefunden. Behalte keine Würfel.")
        kept_dices = []  
        return kept_dices

   
    def decide_which_field_to_enter(self, scoreboard, dice_values):
        
        counts = {value: dice_values.count(value) for value in set(dice_values)}
        
        available_fields = [field for field, value in scoreboard[self.name].items() if value is None]
        
        numbers = {1: "Einser", 2: "Zweier", 3: "Dreier", 4: "Vierer", 5: "Fünfer", 6: "Sechser"}
        
        print("Dice Values:", dice_values)
        print("Available Fields:", available_fields)
        
        for value, count in counts.items():
        
            if count == 5:
            
            # Berechnet die aktuelle Punktzahl des "oberen Teils"
                current_upper_score = sum(scoreboard[self.name][field] for field in numbers.values() if scoreboard[self.name][field] is not None)
                
            # Berechnet, ob der Bonus auch ohen Berücksichtigung der vier Gleichen noch erreicht werden kann
                possible_upper_score = sum(value * 3 for value in numbers.keys() if numbers[value] in available_fields) + current_upper_score
                
            # Kniffel wird nur eingetragen, wenn er im oberen Bereich nicht zwingend benötigt wird
                if possible_upper_score >= 63:
                
                    if "Kniffel" in available_fields:
                    
                        print("Kniffel gefunden, Wert: 50 Punkte")      
                        return "Kniffel"
                
                elif numbers[value] in available_fields:
                    
                    print(f"{numbers[value]} gefunden, Wert: {value * 5} Punkte")
                    return numbers[value]
                
                elif "Kniffel" in available_fields:
                
                    print("Kniffel gefunden, Wert: 50 Punkte")      
                    return "Kniffel"
        
        # Überprüft auf Viererpasch 
            elif count >= 4:
            
            # Berechnet die aktuelle Punktzahl des "oberen Teils"
                current_upper_score = sum(scoreboard[self.name][field] for field in numbers.values() if scoreboard[self.name][field] is not None)
                
            # Berechnet, ob der Bonus auch ohen Berücksichtigung der vier Gleichen noch erreicht werden kann
                possible_upper_score = sum(value * 3 for value in numbers.keys() if numbers[value] in available_fields) + current_upper_score
                
            # Viererpasch wird nur eingetragen, wenn er im oberen Bereich nicht zwingend benötigt wird und nicht zu "klein" ist
                if possible_upper_score >= 63 and sum(dice_values) > 25:
                    
                    if "Viererpasch" in available_fields:
                        
                        print(f"Viererpasch gefunden, Wert: {sum(dice_values)} Punkte")
                        return "Viererpasch"
            
            # Vier Gleiche werden im "oberen teil" eingetragen        
                elif numbers[value] in available_fields:
                    
                    print("{numbers[value]} gefunden, Wert: {value * 4} Punkte")
                    return numbers[value]
                
            # Sorgt dafür, dass ein Viererpasch eingetragen wird, wenn der "obere Teil" bereits ausgefüllt ist
                elif "Viererpasch" in available_fields:
                    
                    print(f"Viererpasch gefunden, Wert: {sum(dice_values)} Punkte")
                    return "Viererpasch"
        
        # Überprüft auf Dreierpasch 
            elif count >= 3:
                
                if numbers[value] in available_fields:
                    
                    print(f"{numbers[value]} gefunden, Wert: {value * 3} Punkte")
                    return numbers[value]
                
                elif "Dreierpasch" in available_fields:
                                                        
                    print(f"Dreierpasch gefunden, Wert: {sum(dice_values)} Punkte")           
                    return "Dreierpasch"
            
        # Überprüft auf große Straße
            elif all(value in dice_values for value in [1, 2, 3, 4, 5]) or all(value in dice_values for value in [2, 3, 4, 5, 6]):      # "all" überprüft die spezifische Kombination
                
                if "Große Straße" in available_fields:    
                    
                    print("Große Straße gefunden, Wert: 40 Punkte")
                    return "Große Straße"
            
        # Überprüft auf kleine Straße
            elif all(value in dice_values for value in [1,2,3,4]) or all(value in dice_values for value in [2,3,4,5]) or all(value in dice_values for value in [3,4,5,6]):
                
                if "Kleine Straße" in available_fields:
                    
                    print("Kleine Straße gefunden, Wert: 30 Punkte")
                    return "Kleine Straße"
            
        # Überprüft auf Full House
            elif 2 in counts.values() and 3 in counts.values():     # Überprüft die values (Häufigkeit eines Wertes) des dictionaries "counts"
                
                if "Full House" in available_fields: 
                    
                    print("Full House gefunden, Wert: 25 Punkte")            
                    return "Full House"
                
    # Überprüft auf zwei Gleiche oder weniger
        for value, count in counts.items():
            
            if count >= 2:
                
                current_upper_score = sum(scoreboard[self.name][field] for field in numbers.values() if scoreboard[self.name][field] is not None)
                updated_upper_score = value * 2 + current_upper_score
                possible_upper_score = sum(value * 3 for value in numbers.keys() if numbers[value] in available_fields and numbers[value] != value) + updated_upper_score
            
            # Zwei Gleiche werden nur im "oberen Teil" eingetragen, wenn dadurch der Bonus nicht gefährdet wird
                if possible_upper_score >= 63:
                
                    if numbers[value] in available_fields:
                    
                        print(f"Zwei Gleiche gefunden, Wert {value * 2} Punkte")
                        return numbers[value]
                            
    # Überprüft auf Chance                       
        if "Chance" in available_fields:
                           
            print(f"Chance gefunden, Wert: {sum(dice_values)} Punkte")            
            return "Chance"
    
    # Überprüft auf möglichen Eintrag im oberen Bereich, damit dort keine 0 eingetragen wird  
        for value in sorted(counts.keys()):  # Sortiert die Zahlen aufsteigend und stellt sicher, dass kleinster Wert zuerst betrachtet wird
        
        # Wird nur im "oberen Teil" eingetragen, wenn "unterer Teil" bereits ausgefüllt ist (0 Punkte "unten" besser als zu wenig Punkte "oben")
            if all(field not in available_fields for field in ["Dreierpasch", "Viererpasch", "Full House", "Kleine Straße", "Große Straße", "Kniffel"]):
            
                if numbers[value] in available_fields:
                
                    print(f"{numbers[value]} gefunden, Wert: {value * count} Punkte")
                    return numbers[value]
                
        
class Tintrup_1(Kniffel_Player):
    def __init__(self, name):
        "Name should be a string"
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' The player's choice on what dices to keep.
        Input:
        - scoreboard: A copy of the scoreboard with information about the game. 
        (see Kniffel_Game.py file)
        Type: dict
        - kept_dicess: A copy of the dice values, that are already kept from previous rolls
        Type: list
        - dice_rolls: A copy of the dice values just rolled, that have to be decided on, whether to keep or not to keep.
        Type: list
        - roll: The number of the roll. Either 0 (first roll) or 1 (second roll). After the third roll the dices are automatically kept
        Type: int

        Output:
        A list of the dice values, that want to be kept. Can also be an empty list.
        Beware: The list needs to only include valid sublists of dice_rolls. Otherwise no dices will be kept.
        '''
        # Aufrufen von Hilfsfunktionen
        WS_aktuell = self.calculate_probabilities(dice_rolls, roll, scoreboard, kept_dices) # Empfängt das Wahrscheinlichkeitsverzeichnis
        entscheidung = self.entscheidung(WS_aktuell,scoreboard) # Empfängt die Entscheidung aus der Hilfsfunktion
        kept_dices = self.Zu_Halten(dice_rolls, kept_dices, roll, entscheidung) # Empfängt die Halteliste aus der Hilfsfunktion       
        if kept_dices is None:
            kept_dices = [] # Reicht leere Liste weiter, falls kept_dices None annimmt
        # Debugging-Outputs
        # print(WS_aktuell)
        # print(f'Wurf: {roll}')
        # print(f'Gewürfelt: {dice_rolls}')      
        # print(f'Behalten: {kept_dices}')
        # print(f'Entscheidung: {entscheidung}')
        
        return kept_dices # Gibt kept_dices weiter
    
    # Hilfsfunktion WS-BErechnung 
    def calculate_probabilities(self, dice_rolls, roll, scoreboard, kept_dices):
        """
        Berechnet die Wahrscheinlichkeiten für alle relevanten Kombinationen
        basierend auf aktuellen Würfeln, gehaltenen Würfeln, verbleibenden Würfen und freien Feldern.

        Parameters
        ----------
        dice_rolls : list
            Die aktuellen Würfelwerte.
        roll : int
            Aktueller Wurf.
        scoreboard : dict
            Das aktuelle Scoreboard mit freien und belegten Feldern.
        kept_dices : list
            Würfel, die bereits gehalten wurden.

        Returns
        -------
        probabilities: dict
            Ein Dictionary mit Wahrscheinlichkeiten für relevante Kombinationen.

        """
        # Kombiniere die aktuellen Würfel mit den gehaltenen Würfeln
        all_dice = dice_rolls + kept_dices
        dice_counts = Counter(all_dice)  # Zähle alle Würfel (gehalten und aktuell)

        # Erstelle ein Dictionary für die Wahrscheinlichkeiten
        probabilities = {}
        parameter = {'1': 75.5, '2': 24.21, '3': 84.91, '4': 72.06, '5': 85.38, '6': 97.51, '3P': 42.16, '4P': 84.99, 'FH': 46.42, 'KS': 97.28, 'GS': 97.55, 'K': 84.81, 'C': 1}

        # Berechnung für Kniffel
        if scoreboard[self.name]["Kniffel"] is None:
            probabilities["Kniffel"] = self.chance_of_kniffel(dice_counts, roll, kept_dices, dice_rolls)*parameter["K"]

        # Berechnung für Full House
        if scoreboard[self.name]["Full House"] is None:
            probabilities["Full House"] = self.chance_of_full_house(dice_rolls, roll, kept_dices)*parameter["FH"]

        # Berechnung für Dreierpasch und Viererpasch
        if scoreboard[self.name]["Dreierpasch"] is None:
            probabilities["Dreierpasch"] = self.chance_of_dreierpasch(dice_counts, roll, kept_dices, dice_rolls)*parameter["3P"]
        if scoreboard[self.name]["Viererpasch"] is None:
            probabilities["Viererpasch"] = self.chance_of_viererpasch(dice_counts, roll, kept_dices, dice_rolls)*parameter["4P"]

        # Berechnung für obere Kategorie (Einser bis Sechser)
        for value in range(1, 7):
            field = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"][value - 1] # Iteration durch die Liste für die oberen Felder
            field_param = ["1","2","3","4","5","6"][value - 1]
            if scoreboard[self.name][field] is None:
                probabilities[field] = self.chance_of_upper_section(value, roll, kept_dices, dice_rolls)*parameter[field_param]

        # Berechnung für Chance (keine Wahrscheinlichkeitsberechnung nötig)
        if scoreboard[self.name]["Chance"] is None:
            probabilities["Chance"] = 0 # Immer möglich, unabhängig vom Wurf. Hier 0, um die Auswahl der Wahrscheinlichkeit nicht zu beeinflussen

        # Berechnung für kleine/große Straße
        if scoreboard[self.name]["Kleine Straße"] is None:
            probabilities["Kleine Straße"] = self.chance_of_straight("small", dice_rolls, roll, kept_dices)*parameter["KS"]
        if scoreboard[self.name]["Große Straße"] is None:
            probabilities["Große Straße"] = self.chance_of_straight("large", dice_rolls, roll, kept_dices)*parameter["GS"]

        return probabilities

    def chance_of_kniffel(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Kniffel-WS
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Kniffel.

        """
        max_count = max(dice_counts.values())  # Höchste Häufigkeit einer Augenzahl in der aktuellen Zusammensetzung
        needed = 5 - max_count # Noch benötigte Würfel um Kniffel zu erreichen
        rolls_left = 2 - roll # Verbleibende Wurfrunden
        
        #### Neue remaining_dice-Logik ##### Berichtigt die verbleibenden Würfel für die Berechnung
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0]) # Zieht gehaltene Würfel und meistvorkommende Würfel aus aktuellen Würfeln ab
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6
        GegenWS = 1 - WS
        
        if needed <= 0: 
            return 1.0  # Kniffel ist erreicht
        if needed > remaining_dice or rolls_left == 0:
            return 0.0  # Nicht genug Würfel oder Würfe übrig
        
        # Binomialverteilung
        probability = sum(
            binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
            for k in range(needed, remaining_dice + 1)
            )
        
        # Kombiniere Wahrscheinlichkeiten bei mehreren Würfen
        if rolls_left > 1:
            probability = 1 - (1 - probability) ** rolls_left
        
        return probability  # Rückgabe der berechneten Wahrscheinlichkeit
    
    def chance_of_full_house(self, dice_rolls, roll, kept_dices): # Diese Hilfsfunktion berechnet die Full House-WS
        """
        

        Parameters
        ----------
        dice_rolls : list
            Die aktuellen Würfelwerte.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.

        Returns
        -------
        combined_probability : float
            Gibt die Wahrscheinlichkeit je nach Fallunterscheidung zurück.

        """
        # Definition der üblichen Variablen
        all_dice = dice_rolls + kept_dices
        dice_counts = Counter(all_dice)
        rolls_left = 2 - roll
        remaining_dice = 5 - len(kept_dices)
        WS = 1 / 6
        GegenWS = 1 - WS

        # Erstelle ein Verzeichnis der Häufigkeiten der Augenzahlen
        Augenzahl_Verzeichnis = {num: dice_counts[num] for num in range(1, 7)}

        # Prüfe, ob ein Full House bereits vorhanden ist
        Drilling = any(count >= 3 for count in Augenzahl_Verzeichnis.values()) # Drilling, wenn eine Augenzahl schon dreimal vorkommt
        Paar = any(count >= 2 for count in Augenzahl_Verzeichnis.values() if count < 3) # Analog zu oben für Paar
        
        if Drilling and Paar == True: # Kombination für Full House erfüllt
            # print("Debug: Full House bereits vorhanden.")
            combined_probability = 1.0
            return combined_probability

        if Drilling == True and Paar == False: # Drilling vorhanden, Paar nicht.
            # Variablen
            drilling_probability = 1.0
            paar_probability = 0.0
                
            ### Spezialfall Kniffel
            # In diesem Fall wird Drilling erkannt, aber kein Paar, da gleiche Augenzahl
            
            if len(set(all_dice)) == 1:
                remaining_dice = 2 # Zwei Würfel müssen nochmal geworfen werden
                k = 2 # Beide Würfel müssen dieselbe Augenzahl zeigen
                for k in range(1, remaining_dice+1): # Berechnung der WS für das Erreichen der benötigten Kombination
                    paar_probability += binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = paar_probability
                
                if rolls_left > 1:
                    combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
                return combined_probability
                    
            else:
                Zu_Entfernen = [count for count in set(all_dice) if all_dice.count(count) >=3] # Welche Augenzahl kommt mindestens dreimal vor
                all_dice.remove(Zu_Entfernen[0]) # Entfernung dieser Augenzahl
                remaining_dice = len(all_dice)-1 # Verbleibende Würfel
                k = 1 # Eine Augenzahl fehlt noch
                paar_probability = binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = paar_probability
                
                if rolls_left > 1:
                    combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
                return combined_probability

        if Drilling == False and Paar == True: # Paar vorhanden, Drilling nicht
            drilling_probability = 0.0
            paar_probability = 1.0
            
            Zu_Entfernen = [count for count in set(all_dice) if all_dice.count(count) >=2] # Augenzahl des Paares wird entfernt
            all_dice.remove(Zu_Entfernen[0])
            
            # Fallunterscheidung: Wie viele Augenzahlen fehlen noch zu einem Drilling?
            if len(Zu_Entfernen) > 1:
                remaining_dice = 1
                k = 1
            else: 
                remaining_dice = 2
                k = 2
            
            for k in range(1, remaining_dice+1):
                drilling_probability += binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = drilling_probability
                
            if rolls_left > 1:
                combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
            return combined_probability
                
        if Drilling == False and Paar == False: # Weder noch ist vorhanden
            drilling_probability = 0.0
            paar_probability = 0.0
            
            remaining_dice_paar = 1 # Fehlender Würfel zu einem Paar
            k_paar = 1
            paar_probability = binom(remaining_dice_paar, k_paar) * (WS ** k_paar) * (GegenWS ** (remaining_dice_paar - k_paar))
            
            remaining_dice_drilling = 2 # Fehlender Würfel zu einem Drilling
            k_drilling = 2
            
            for k_drilling in range(1, remaining_dice_drilling+1):
                drilling_probability += binom(remaining_dice_drilling, k_drilling) * (WS ** k_drilling) * (GegenWS ** (remaining_dice_drilling - k_drilling))
                
            combined_probability = paar_probability + drilling_probability
            
            if rolls_left > 1:
                combined_probability = 1 - (1 - combined_probability) ** rolls_left
                
            return combined_probability
    
    def chance_of_dreierpasch(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Dreierpasch-WS
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Dreierpasch.

        """
        rolls_left = 2 - roll
        
        #### Neue remaining_dice-Logik ####
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0])
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
            
        WS = 1 / 6  
        GegenWS = 1 - WS
        
        Menge_gesuchte_Augen = max(dice_counts.values()) # Sucht meistvorhandene Augenzahl
        Anzahl_nötige_Würfel = 3 - Menge_gesuchte_Augen # Noch benötigte Würfel zum Erreichen der Augenzahl
        
        if Anzahl_nötige_Würfel <= 0: # Dreierpasch erreicht
            return 1.0
        
        elif Anzahl_nötige_Würfel > remaining_dice or rolls_left == 0: #Nicht mehr erreichbar bei zu wenigen Würfeln oder keinen Würfelrunden mehr
            return 0.0
       
        else:
            probability = sum(
                 binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                 for k in range(Anzahl_nötige_Würfel, remaining_dice + 1)
                 )
            if rolls_left > 1:  # Wahrscheinlichkeit über mehrere Würfe berücksichtigen
                probability = 1 - (1 - probability) ** rolls_left
                
            return probability 
        
            
        

    def chance_of_viererpasch(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Viererpasch-WS, Vorgehen analog zu Dreierpasch
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Viererpasch.

        """
        
        rolls_left = 2 - roll
        
        #### Neue remaining_dice-Logik ####
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0])
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6  
        GegenWS = 1 - WS
        
        Menge_gesuchte_Augen = max(dice_counts.values())
        Anzahl_nötige_Würfel = 4 - Menge_gesuchte_Augen
        
        if Anzahl_nötige_Würfel <= 0:
            return 1.0
        elif Anzahl_nötige_Würfel > remaining_dice or rolls_left == 0:
            return 0.0
        else:
            probability = sum(
                binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                for k in range(Anzahl_nötige_Würfel, remaining_dice + 1)
                )
            
            if rolls_left > 1:
                probability = 1 - (1 - probability) ** rolls_left

        return probability
    
    def chance_of_upper_section(self, value, roll, kept_dices, dice_rolls): # Hilfsfunktion für die WS-Berechnung der Kombinationen aus dem oberen Block
        """
        

        Parameters
        ----------
        value : int
            Wert für die Augenzahl aus calculate_probabilities.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability : float
            WS für die Einser bis Sechser-Kombis.

        """
        rolls_left = 2 - roll
        all_dice = dice_rolls + kept_dices
        #### Neue remaining_dice-Logik ####
        if value in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(value)
        else:
            remaining_dice = 5 - len(kept_dices)
            
        #print(f'Debug: remaining_dice: {remaining_dice}')
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6
        GegenWS = 1 - WS
        Menge_gesuchte_Augen = min(5 - all_dice.count(value),remaining_dice) # Sucht für jede Augenzahl die noch benötigte Augenzahl
        rest = sum(binom(remaining_dice,i)*(WS**i)*(GegenWS**(remaining_dice-i)) for i in range(1,Menge_gesuchte_Augen+1)) # Summe aller WS für eine Augenzahl von 1 bis 5 Würfeln für noch nicht erreichte Augenzahlen
            
        if rolls_left > 1:
            combrest = 1-(1-rest)**rolls_left
            probability = ((all_dice.count(value)+combrest)/5) # Summe aller WS geteilt für die Anzahl an Möglichkeiten (5 Wege eine Kombination zu haben...)
            return probability
        else:
            probability = ((all_dice.count(value) + rest)/5)
            return probability


    def chance_of_straight(self, straight_type, dice_rolls, roll, kept_dices):
        """
        
        Parameters
        ----------
        straight_type : str
            Art der gesuchten Straße.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        min(total_probability, 1.0)
            WS für die bestmögliche Straße.

        """
        rolls_left = 2 - roll
        all_dice = set(kept_dices + dice_rolls)
        WS = 1 / 6
        GegenWS = 1 - WS
            
        # Mögliche Straßen nach Typ klein, sonst groß
        needed_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] if straight_type == "small" else \
                           [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        
        total_probability = 0.0
        
        for straight in needed_straights:
            
            missing = [num for num in straight if num not in all_dice] # Noch fehlenden Augenzahlen je nach Straße
            in_dice_rolls = [num for num in dice_rolls if num in straight and num not in kept_dices] # Augenzahl in dice_rolls, die noch nicht in kept_dice sind aber in Straße vorkommen
            
            #### Neue remaining_dice-Logik ####
            if len(in_dice_rolls) > 0:
                remaining_dice = 5 - len(kept_dices) - len(in_dice_rolls)
            else:
                remaining_dice = 5 - len(kept_dices)
            #### ENDE Neue remaining_dice-Logik ####
            
            if len(missing) == 0: # Straße schon vorhanden
                return 1.0
            elif len(missing) <= remaining_dice and rolls_left > 0:
                prob_for_straight = sum(
                    binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                    for k in range(len(missing), remaining_dice + 1)
                    )
                prob_for_straight = 1 - (1 - prob_for_straight) ** rolls_left
                total_probability = prob_for_straight

        return min(total_probability, 1.0)  # Maximale Wahrscheinlichkeit 1.0 
    
    
    def entscheidung(self, WS_aktuell,scoreboard):
        """
        

        Parameters
        ----------
        WS_aktuell : dict
            Verzeichnis der berechneten Wahrscheinlichkeiten.

        Returns
        -------
        entscheidung : str
            Die Entscheidung für eine Kombination aus dem Verzeichnis.

        """
        entscheidung = list(WS_aktuell.keys())[list(WS_aktuell.values()).index(max(WS_aktuell.values()))] # Entscheidung für größten Wert in der Dictionary
        return entscheidung 
    
    def Zu_Halten (self, dice_rolls, kept_dices, roll, entscheidung):
        """
        

        Parameters
        ----------
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.
        entscheidung : str
            Entscheidung für eine Kombination.

        Returns
        -------
        kept_dices : list
            Würfel die gehalten werden sollen.

        """
        rolls_left = 2 - roll
        
        if entscheidung == "Einser":
            kept_dices = [x for x in dice_rolls if x == 1] # Halte Würfel nit Augenzahl 1 in allen Runden
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Zweier":
            kept_dices = [x for x in dice_rolls if x == 2] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Dreier":
            kept_dices = [x for x in dice_rolls if x == 3] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Vierer":
            kept_dices = [x for x in dice_rolls if x == 4] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Fünfer":
            kept_dices = [x for x in dice_rolls if x == 5] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Sechser":
            kept_dices = [x for x in dice_rolls if x == 6] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Dreierpasch":
            if rolls_left == 2:
                Zähler = Counter(dice_rolls)
                ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Hinzufügen zu kept_dices
                # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                if len(kept_dices) < 3: # Fall: Noch kein Dreierpasch vorhanden
                    if not kept_dices == True: # Im Fall einer leeren Liste
                        Zähler = Counter(dice_rolls)
                        ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                        Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                        Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))] # Hält höchste Anzahl an Augenwerten
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    else:
                        Zähler = Counter(kept_dices) # Zählung bereits gehaltener Würfel
                        Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]# Hält Augenzahlen die zu denen in kept_dices passen
                    return kept_dices
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                elif len(kept_dices) >=3: 
                    kept_dices = [x for x in dice_rolls if x > 3.5] # Optimierung, fall schon ein Dreierpasch vorliegt. Wir halten Würfel größer als den Erwartungswertes eines Würfels.
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
        elif entscheidung == "Viererpasch": # Vorgehen hier analog zu Dreierpasch
            if rolls_left == 2:
                Zähler = Counter(dice_rolls)
                ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                if len(kept_dices) < 4:
                    if not kept_dices == True:
                        Zähler = Counter(dice_rolls)
                        ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                        Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                        Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    else:
                        Zähler = Counter(kept_dices)
                        Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                elif len(kept_dices) >=4: 
                    kept_dices = [x for x in dice_rolls if x > 3.5] #### Optimierung vielleicht?
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
        elif entscheidung == "Full House":
            if rolls_left == 2:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                if len(set(dice_rolls)) == 1: #Spezialfall Kniffel
                    Zähler = Counter(dice_rolls) # Zählung Anzahl Augen in dice_rolls
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Entscheidung für das Halten mit dem höchsten Vorkommen
                    WieOftSchonHinzugefügt = {Zu_Halten1:0} # Erstellen einer Dictionary zum Zählen des Hinzufügens
                    for i in dice_rolls: # Schleife die so lange über dice_rolls iteriert, bis die zu haltende Augenzahl dreimal gehalten wird.
                        if i == Zu_Halten1 and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                else: # Ähnlich zu oben, nur dass hier jetzt zwei verschiedene Augenzahlen gehalten werden sollen
                    Zähler = Counter(dice_rolls)
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Erste zu haltende Augenzahl aus dem Counter
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]] # Löscht den Eintrag in der Dictionary mit der höchsten Augenzahlanzahl
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Zweite zu haltende Augenzahl aus dem Counter
                    WieOftSchonHinzugefügt = {Zu_Halten1:0,Zu_Halten2:0} # Ab hier wieder wie im oberen Fall
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices  
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                Zähler = Counter(kept_dices)
                if len(set(kept_dices)) == 2 and any(kept_dices.count(dice) == 3 for dice in kept_dices) == True: #Fall: Full House liegt schon vor
                    return kept_dices
                elif not Zähler: # Fall: Leerer Counter in Zähler
                    Zähler = Counter(dice_rolls) # Ab hier analoges Vorgehen wie in rolls_left == 2 Fall else
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    WieOftSchonHinzugefügt = {Zu_Halten1:0,Zu_Halten2:0}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices  
                elif len(Zähler) < 2: # Fall Zähler enthält nur eine Augenzahl, eine beliebige andere Augenzahl wird noch benötigt    
                    Zähler_dice_rolls = Counter(dice_rolls) 
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Augenzahl die bereits gehalten wird
                    Zu_Halten2 = list(Zähler_dice_rolls.keys())[list(Zähler_dice_rolls.values()).index(max(Zähler_dice_rolls.values()))] # Augenzahl die noch gesucht wird
                    Anzahl1 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    Anzahl2 = 0
                    WieOftSchonHinzugefügt = {Zu_Halten1:Anzahl1,Zu_Halten2:Anzahl2}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    return kept_dices
                else: # Fall zwei verschiedende Augenzahlen in kept_dices
                    Zähler = Counter(kept_dices)
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    Zähler = Counter(kept_dices)
                    Anzahl1 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Anzahl2 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    WieOftSchonHinzugefügt = {Zu_Halten1:Anzahl1,Zu_Halten2:Anzahl2}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    return kept_dices
        elif entscheidung == "Kleine Straße":
            KleineStraßen = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
            if rolls_left == 2:
                PassendeWerte = []
                for i in range(0,3):
                    PassendeWerte.append(list(set([x for x in dice_rolls if x in KleineStraßen[i]]))) # Hinzufügen passender Augenzahlen in Liste PassendeWerte für jede Straße
                BesteStraße = max(PassendeWerte, key=len) # Definition der besten Straße, eben jener bei der die meisten Augenzahlen übereinstimmen. 
                kept_dices = BesteStraße # Die Augenzahlen aus der besten Straße werden gehalten
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                FehltNoch = [] 
                for i in range(0,3):
                    FehltNoch.append([x for x in KleineStraßen[i] if x not in kept_dices]) # Fehlende Augenzahlen, die noch nicht in kept_dices sind
                FehltAmWenigsten = min(FehltNoch, key=len) # Definiert die wenigsten fehlenden Augenzahlen
                kept_dices = list(set([x for x in FehltAmWenigsten if x in dice_rolls])) # Wenigste fehlende Augenzahlen werden gehalten
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
        elif entscheidung == "Große Straße": # Vorgehen analog zu Kleine Straße
            GroßeStraßen = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
            if rolls_left == 2:
                PassendeWerte = []
                for i in range(0,2):
                    PassendeWerte.append(list(set([x for x in dice_rolls if x in GroßeStraßen[i]])))
                BesteStraße = max(PassendeWerte, key=len)
                kept_dices = BesteStraße
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                FehltNoch = []
                for i in range(0,2):
                    FehltNoch.append([x for x in GroßeStraßen[i] if x not in kept_dices])
                FehltAmWenigsten = min(FehltNoch, key=len)    
                kept_dices = list(set([x for x in FehltAmWenigsten if x in dice_rolls]))
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
        elif entscheidung == "Kniffel":
            if rolls_left == 2:
                Zähler = Counter(dice_rolls) # Zählt Anzahl der Würfelaugen
                Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die am häufigsten vorkommen
                kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfel zu kept_dices
               # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                Zähler = Counter(kept_dices) # Wir schauen welche Würfel nach Runde 2 unseren gehaltenen Würfeln entsprechen
                if not Zähler: # Fall kept_dices ist leer
                    Zähler = Counter(dice_rolls) # Zählt Anzahl der Würfelaugen
                    Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die am häufigsten vorkommen
                    kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfen von dice_rolls zu kept_dices
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                else:
                    Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die Augenzahl gehaltener Würfel entsprechen
                    kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfel werden behalten
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
    
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
        Eingabe = self.Feldeingabe(dice_values, scoreboard) # Fordert Eingabe aus Feldeingabe() an
        # print(f'Finale Werte: {dice_values}')
        # print(f'Finale Entscheidung: {Eingabe}')
        return Eingabe
    
    def Feldeingabe(self, dice_values, scoreboard):
        """
        

        Parameters
        ----------
        dice_values : list
            Alle Würfel nach allen Würfelrunden.
        scoreboard : dict
            Scorebpard des Spiels.

        Returns
        -------
        str
            Feldentscheidung.

        """
        #dice_values = [random.randint(1,6) for _ in range(0,5)]
        #print(dice_values)
        Kombination = {}
        # Passt Kombination zum Feld
        #x_er
        for i in range(1,7):
            x_er = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"][i - 1]
            if i in dice_values:
                Kombination[x_er] = True
            else:
                Kombination[x_er] = False
        #Dreierpasch
        if max(dice_values.count(dice) for dice in dice_values) >= 3:
            Kombination["Dreierpasch"] = True
        else:
            Kombination["Dreierpasch"] = False
        #Viererpasch
        if max(dice_values.count(dice) for dice in dice_values) >= 4:
            Kombination["Viererpasch"] = True
        else:
            Kombination["Viererpasch"] = False
        #Full House
        if len(set(dice_values)) == 2 and any(dice_values.count(dice) == 3 for dice in dice_values):
            Kombination["Full House"] = True
        else:
            Kombination["Full House"] = False
        #Kleine Straße
        if any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
            Kombination["Kleine Straße"] = True
        else:
            Kombination["Kleine Straße"] = False
        #Große Straße
        if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values):
            Kombination["Große Straße"] = True
        else:
            Kombination["Große Straße"] = False
        
        #Kniffel
        if len(set(dice_values)) == 1:
            Kombination["Kniffel"] = True
        else:
            Kombination["Kniffel"] = False
            
        #Regelbasiertes Eintragen wenn Kombination stimmt und Feld frei
        if scoreboard[self.name]["Kniffel"] is None and Kombination["Kniffel"] is True:
            return "Kniffel"
        elif scoreboard[self.name]["Große Straße"] is None and Kombination["Große Straße"] is True:
            return "Große Straße"
        elif scoreboard[self.name]["Kleine Straße"] is None and Kombination["Kleine Straße"] is True:
            return "Kleine Straße"
        elif scoreboard[self.name]["Full House"] is None and Kombination["Full House"] is True:
            return "Full House"
        elif scoreboard[self.name]["Sechser"] is None and Kombination["Sechser"] is True and dice_values.count(6) >=3:
            return "Sechser"
        elif scoreboard[self.name]["Fünfer"] is None and Kombination["Fünfer"] is True and dice_values.count(5) >=3:
            return "Fünfer"
        elif scoreboard[self.name]["Vierer"] is None and Kombination["Vierer"] is True and dice_values.count(4) >=3:
            return "Vierer"
        elif scoreboard[self.name]["Dreier"] is None and Kombination["Dreier"] is True and dice_values.count(3) >=3:
            return "Dreier"
        elif scoreboard[self.name]["Zweier"] is None and Kombination["Zweier"] is True and dice_values.count(2) >=3:
            return "Zweier"
        elif scoreboard[self.name]["Einser"] is None and Kombination["Einser"] is True and dice_values.count(1) >=3:
            return "Einser"
        elif scoreboard[self.name]["Viererpasch"] is None and Kombination["Viererpasch"] is True:
            return "Viererpasch"
        elif scoreboard[self.name]["Dreierpasch"] is None and Kombination["Dreierpasch"] is True:
            return "Dreierpasch"
        elif scoreboard[self.name]["Sechser"] is None and Kombination["Sechser"] is True:
            return "Sechser"
        elif scoreboard[self.name]["Fünfer"] is None and Kombination["Fünfer"] is True:
            return "Fünfer"
        elif scoreboard[self.name]["Vierer"] is None and Kombination["Vierer"] is True:
            return "Vierer"
        elif scoreboard[self.name]["Dreier"] is None and Kombination["Dreier"] is True:
            return "Dreier"
        elif scoreboard[self.name]["Zweier"] is None and Kombination["Zweier"] is True:
            return "Zweier"
        elif scoreboard[self.name]["Einser"] is None and Kombination["Einser"] is True:
            return "Einser"
        else:
            return "Chance"
        
        
 
from collections import Counter
from scipy.special import binom

class Tintrup_2(Kniffel_Player):
    def __init__(self, name):
        "Name should be a string"
        self.name = name

    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' The player's choice on what dices to keep.
        Input:
        - scoreboard: A copy of the scoreboard with information about the game. 
        (see Kniffel_Game.py file)
        Type: dict
        - kept_dicess: A copy of the dice values, that are already kept from previous rolls
        Type: list
        - dice_rolls: A copy of the dice values just rolled, that have to be decided on, whether to keep or not to keep.
        Type: list
        - roll: The number of the roll. Either 0 (first roll) or 1 (second roll). After the third roll the dices are automatically kept
        Type: int

        Output:
        A list of the dice values, that want to be kept. Can also be an empty list.
        Beware: The list needs to only include valid sublists of dice_rolls. Otherwise no dices will be kept.
        '''
        # Aufrufen von Hilfsfunktionen
        WS_aktuell = self.calculate_probabilities(dice_rolls, roll, scoreboard, kept_dices) # Empfängt das Wahrscheinlichkeitsverzeichnis
        entscheidung = self.entscheidung(WS_aktuell) # Empfängt die Entscheidung aus der Hilfsfunktion
        kept_dices = self.Zu_Halten(dice_rolls, kept_dices, roll, entscheidung) # Empfängt die Halteliste aus der Hilfsfunktion       
        if kept_dices is None:
            kept_dices = [] # Reicht leere Liste weiter, falls kept_dices None annimmt
        # Debugging-Outputs
        # print(WS_aktuell)
        # print(f'Wurf: {roll}')
        # print(f'Gewürfelt: {dice_rolls}')      
        # print(f'Behalten: {kept_dices}')
        # print(f'Entscheidung: {entscheidung}')
        
        return kept_dices # Gibt kept_dices weiter
    
    # Hilfsfunktion WS-BErechnung 
    def calculate_probabilities(self, dice_rolls, roll, scoreboard, kept_dices):
        """
        Berechnet die Wahrscheinlichkeiten für alle relevanten Kombinationen
        basierend auf aktuellen Würfeln, gehaltenen Würfeln, verbleibenden Würfen und freien Feldern.

        Parameters
        ----------
        dice_rolls : list
            Die aktuellen Würfelwerte.
        roll : int
            Aktueller Wurf.
        scoreboard : dict
            Das aktuelle Scoreboard mit freien und belegten Feldern.
        kept_dices : list
            Würfel, die bereits gehalten wurden.

        Returns
        -------
        probabilities: dict
            Ein Dictionary mit Wahrscheinlichkeiten für relevante Kombinationen.

        """
        # Kombiniere die aktuellen Würfel mit den gehaltenen Würfeln
        all_dice = dice_rolls + kept_dices
        dice_counts = Counter(all_dice)  # Zähle alle Würfel (gehalten und aktuell)

        # Erstelle ein Dictionary für die Wahrscheinlichkeiten
        probabilities = {} 

        # Berechnung für Kniffel
        if scoreboard[self.name]["Kniffel"] is None:
            probabilities["Kniffel"] = self.chance_of_kniffel(dice_counts, roll, kept_dices, dice_rolls)

        # Berechnung für Full House
        if scoreboard[self.name]["Full House"] is None:
            probabilities["Full House"] = self.chance_of_full_house(dice_rolls, roll, kept_dices)

        # Berechnung für Dreierpasch und Viererpasch
        if scoreboard[self.name]["Dreierpasch"] is None:
            probabilities["Dreierpasch"] = self.chance_of_dreierpasch(dice_counts, roll, kept_dices, dice_rolls)
        if scoreboard[self.name]["Viererpasch"] is None:
            probabilities["Viererpasch"] = self.chance_of_viererpasch(dice_counts, roll, kept_dices, dice_rolls)

        # Berechnung für obere Kategorie (Einser bis Sechser)
        for value in range(1, 7):
            field = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"][value - 1] # Iteration durch die Liste für die oberen Felder
            if scoreboard[self.name][field] is None:
                probabilities[field] = self.chance_of_upper_section(value, roll, kept_dices, dice_rolls)

        # Berechnung für Chance (keine Wahrscheinlichkeitsberechnung nötig)
        if scoreboard[self.name]["Chance"] is None:
            probabilities["Chance"] = 0 # Immer möglich, unabhängig vom Wurf. Hier 0, um die Auswahl der Wahrscheinlichkeit nicht zu beeinflussen

        # Berechnung für kleine/große Straße
        if scoreboard[self.name]["Kleine Straße"] is None:
            probabilities["Kleine Straße"] = self.chance_of_straight("small", dice_rolls, roll, kept_dices)
        if scoreboard[self.name]["Große Straße"] is None:
            probabilities["Große Straße"] = self.chance_of_straight("large", dice_rolls, roll, kept_dices)

        return probabilities # Gibt probabilities weiter

    def chance_of_kniffel(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Kniffel-WS
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Kniffel.

        """
        max_count = max(dice_counts.values())  # Höchste Häufigkeit einer Augenzahl in der aktuellen Zusammensetzung
        needed = 5 - max_count # Noch benötigte Würfel um Kniffel zu erreichen
        rolls_left = 2 - roll # Verbleibende Wurfrunden
        
        #### Neue remaining_dice-Logik ##### Berichtigt die verbleibenden Würfel für die Berechnung
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0]) # Zieht gehaltene Würfel und meistvorkommende Würfel aus aktuellen Würfeln ab
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6
        GegenWS = 1 - WS
        
        if needed <= 0: 
            return 1.0  # Kniffel ist erreicht
        if needed > remaining_dice or rolls_left == 0:
            return 0.0  # Nicht genug Würfel oder Würfe übrig
        
        # Binomialverteilung
        probability = sum(
            binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
            for k in range(needed, remaining_dice + 1)
            )
        
        # Kombiniere Wahrscheinlichkeiten bei mehreren Würfen
        if rolls_left > 1:
            probability = 1 - (1 - probability) ** rolls_left
        
        return probability  # Rückgabe der berechneten Wahrscheinlichkeit
    
    def chance_of_full_house(self, dice_rolls, roll, kept_dices): # Diese Hilfsfunktion berechnet die Full House-WS
        """
        Parameters
        ----------
        dice_rolls : list
            Die aktuellen Würfelwerte.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.

        Returns
        -------
        combined_probability : float
            Gibt die Wahrscheinlichkeit je nach Fallunterscheidung zurück.

        """
        # Definition der üblichen Variablen
        all_dice = dice_rolls + kept_dices
        dice_counts = Counter(all_dice)
        rolls_left = 2 - roll
        remaining_dice = 5 - len(kept_dices)
        WS = 1 / 6
        GegenWS = 1 - WS

        # Erstelle ein Verzeichnis der Häufigkeiten der Augenzahlen
        Augenzahl_Verzeichnis = {num: dice_counts[num] for num in range(1, 7)}

        # Prüfe, ob ein Full House bereits vorhanden ist
        Drilling = any(count >= 3 for count in Augenzahl_Verzeichnis.values()) # Drilling, wenn eine Augenzahl schon dreimal vorkommt
        Paar = any(count >= 2 for count in Augenzahl_Verzeichnis.values() if count < 3) # Analog zu oben für Paar
        
        if Drilling and Paar == True: # Kombination für Full House erfüllt
            # print("Debug: Full House bereits vorhanden.")
            combined_probability = 1.0
            return combined_probability

        if Drilling == True and Paar == False: # Drilling vorhanden, Paar nicht.
            # Variablen
            drilling_probability = 1.0
            paar_probability = 0.0
                
            ### Spezialfall Kniffel
            # In diesem Fall wird Drilling erkannt, aber kein Paar, da gleiche Augenzahl
            
            if len(set(all_dice)) == 1:
                remaining_dice = 2 # Zwei Würfel müssen nochmal geworfen werden
                k = 2 # Beide Würfel müssen dieselbe Augenzahl zeigen
                for k in range(1, remaining_dice+1): # Berechnung der WS für das Erreichen der benötigten Kombination
                    paar_probability += binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = paar_probability
                
                if rolls_left > 1:
                    combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
                return combined_probability
                    
            else:
                Zu_Entfernen = [count for count in set(all_dice) if all_dice.count(count) >=3] # Welche Augenzahl kommt mindestens dreimal vor
                all_dice.remove(Zu_Entfernen[0]) # Entfernung dieser Augenzahl
                remaining_dice = len(all_dice)-1 # Verbleibende Würfel
                k = 1 # Eine Augenzahl fehlt noch
                paar_probability = binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = paar_probability
                
                if rolls_left > 1:
                    combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
                return combined_probability

        if Drilling == False and Paar == True: # Paar vorhanden, Drilling nicht
            drilling_probability = 0.0
            paar_probability = 1.0
            
            Zu_Entfernen = [count for count in set(all_dice) if all_dice.count(count) >=2] # Augenzahl des Paares wird entfernt
            all_dice.remove(Zu_Entfernen[0])
            
            # Fallunterscheidung: Wie viele Augenzahlen fehlen noch zu einem Drilling?
            if len(Zu_Entfernen) > 1:
                remaining_dice = 1
                k = 1
            else: 
                remaining_dice = 2
                k = 2
            
            for k in range(1, remaining_dice+1):
                drilling_probability += binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                combined_probability = drilling_probability
                
            if rolls_left > 1:
                combined_probability = 1 - (1 - combined_probability) ** rolls_left
                    
            return combined_probability
                
        if Drilling == False and Paar == False: # Weder noch ist vorhanden
            drilling_probability = 0.0
            paar_probability = 0.0
            
            remaining_dice_paar = 1 # Fehlender Würfel zu einem Paar
            k_paar = 1
            paar_probability = binom(remaining_dice_paar, k_paar) * (WS ** k_paar) * (GegenWS ** (remaining_dice_paar - k_paar))
            
            remaining_dice_drilling = 2 # Fehlender Würfel zu einem Drilling
            k_drilling = 2
            
            for k_drilling in range(1, remaining_dice_drilling+1):
                drilling_probability += binom(remaining_dice_drilling, k_drilling) * (WS ** k_drilling) * (GegenWS ** (remaining_dice_drilling - k_drilling))
                
            combined_probability = paar_probability + drilling_probability
            
            if rolls_left > 1:
                combined_probability = 1 - (1 - combined_probability) ** rolls_left
                
            return combined_probability
                
    
    def chance_of_dreierpasch(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Dreierpasch-WS
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Dreierpasch.

        """
        rolls_left = 2 - roll
        
        #### Neue remaining_dice-Logik ####
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0])
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
            
        WS = 1 / 6  
        GegenWS = 1 - WS
        
        Menge_gesuchte_Augen = max(dice_counts.values()) # Sucht meistvorhandene Augenzahl
        Anzahl_nötige_Würfel = 3 - Menge_gesuchte_Augen # Noch benötigte Würfel zum Erreichen der Augenzahl
        
        if Anzahl_nötige_Würfel <= 0: # Dreierpasch erreicht
            return 1.0
        
        elif Anzahl_nötige_Würfel > remaining_dice or rolls_left == 0: #Nicht mehr erreichbar bei zu wenigen Würfeln oder keinen Würfelrunden mehr
            return 0.0
       
        else:
            probability = sum(
                 binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                 for k in range(Anzahl_nötige_Würfel, remaining_dice + 1)
                 )
            if rolls_left > 1:  # Wahrscheinlichkeit über mehrere Würfe berücksichtigen
                probability = 1 - (1 - probability) ** rolls_left
                
            return probability 
        
            
        

    def chance_of_viererpasch(self, dice_counts, roll, kept_dices, dice_rolls): # Diese Hilfsfunktion berechnet die Viererpasch-WS, Vorgehen analog zu Dreierpasch
        """
        Parameters
        ----------
        dice_counts : counter
            Zählung aller Würfel (gehalten und aktuell).
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability: float
            Wahrscheinlichkeit für Viererpasch.

        """
        
        rolls_left = 2 - roll
        
        #### Neue remaining_dice-Logik ####
        if dice_counts.most_common(1)[0][0] in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(dice_counts.most_common(1)[0][0])
        else:
            remaining_dice = 5 - len(kept_dices)
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6  
        GegenWS = 1 - WS
        
        Menge_gesuchte_Augen = max(dice_counts.values())
        Anzahl_nötige_Würfel = 4 - Menge_gesuchte_Augen
        
        if Anzahl_nötige_Würfel <= 0:
            return 1.0
        elif Anzahl_nötige_Würfel > remaining_dice or rolls_left == 0:
            return 0.0
        else:
            probability = sum(
                binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                for k in range(Anzahl_nötige_Würfel, remaining_dice + 1)
                )
            
            if rolls_left > 1:
                probability = 1 - (1 - probability) ** rolls_left

        return probability
    
    def chance_of_upper_section(self, value, roll, kept_dices, dice_rolls): # Hilfsfunktion für die WS-Berechnung der Kombinationen aus dem oberen Block
        """
        Parameters
        ----------
        value : int
            Wert für die Augenzahl aus calculate_probabilities.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        probability : float
            WS für die Einser bis Sechser-Kombis.

        """
        rolls_left = 2 - roll
        all_dice = dice_rolls + kept_dices
        #### Neue remaining_dice-Logik ####
        if value in dice_rolls:
            remaining_dice = 5 - len(kept_dices) - dice_rolls.count(value)
        else:
            remaining_dice = 5 - len(kept_dices)
            
        #print(f'Debug: remaining_dice: {remaining_dice}')
        #### ENDE Neue remaining_dice-Logik ####
        
        WS = 1 / 6
        GegenWS = 1 - WS
        Menge_gesuchte_Augen = min(5 - all_dice.count(value),remaining_dice) # Sucht für jede Augenzahl die noch benötigte Augenzahl
        rest = sum(binom(remaining_dice,i)*(WS**i)*(GegenWS**(remaining_dice-i)) for i in range(1,Menge_gesuchte_Augen+1)) # Summe aller WS für eine Augenzahl von 1 bis 5 Würfeln für noch nicht erreichte Augenzahlen
            
        if rolls_left > 1:
            combrest = 1-(1-rest)**rolls_left
            probability = ((all_dice.count(value)+combrest)/5) # Summe aller WS geteilt für die Anzahl an Möglichkeiten (5 Wege eine Kombination zu haben...)
            return probability
        else:
            probability = ((all_dice.count(value) + rest)/5)
            return probability


    def chance_of_straight(self, straight_type, dice_rolls, roll, kept_dices):
        """
        
        Parameters
        ----------
        straight_type : str
            Art der gesuchten Straße.
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.

        Returns
        -------
        min(total_probability, 1.0)
            WS für die bestmögliche Straße.

        """
        rolls_left = 2 - roll
        all_dice = set(kept_dices + dice_rolls)
        WS = 1 / 6
        GegenWS = 1 - WS
            
        # Mögliche Straßen nach Typ klein, sonst groß
        needed_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] if straight_type == "small" else \
                           [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        
        total_probability = 0.0
        
        for straight in needed_straights:
            
            missing = [num for num in straight if num not in all_dice] # Noch fehlenden Augenzahlen je nach Straße
            in_dice_rolls = [num for num in dice_rolls if num in straight and num not in kept_dices] # Augenzahl in dice_rolls, die noch nicht in kept_dice sind aber in Straße vorkommen
            
            #### Neue remaining_dice-Logik ####
            if len(in_dice_rolls) > 0:
                remaining_dice = 5 - len(kept_dices) - len(in_dice_rolls)
            else:
                remaining_dice = 5 - len(kept_dices)
            #### ENDE Neue remaining_dice-Logik ####
            
            if len(missing) == 0: # Straße schon vorhanden
                return 1.0
            elif len(missing) <= remaining_dice and rolls_left > 0:
                prob_for_straight = sum(
                    binom(remaining_dice, k) * (WS ** k) * (GegenWS ** (remaining_dice - k))
                    for k in range(len(missing), remaining_dice + 1)
                    )
                prob_for_straight = 1 - (1 - prob_for_straight) ** rolls_left
                total_probability = prob_for_straight

        return min(total_probability, 1.0)  # Maximale Wahrscheinlichkeit 1.0 
    
    
    def entscheidung(self, WS_aktuell):
        """
        Parameters
        ----------
        WS_aktuell : dict
            Verzeichnis der berechneten Wahrscheinlichkeiten.

        Returns
        -------
        entscheidung : str
            Die Entscheidung für eine Kombination aus dem Verzeichnis.

        """
        entscheidung = list(WS_aktuell.keys())[list(WS_aktuell.values()).index(max(WS_aktuell.values()))] # Entscheidung für größten Wert in der Dictionary
        return entscheidung
    
    def Zu_Halten (self, dice_rolls, kept_dices, roll, entscheidung):
        """
        

        Parameters
        ----------
        roll : int
            Aktueller Wurf.
        kept_dices : list
            Würfel, die bereits gehalten wurden.
        dice_rolls : list
            Die aktuellen Würfelwerte.
        entscheidung : str
            Entscheidung für eine Kombination.

        Returns
        -------
        kept_dices : list
            Würfel die gehalten werden sollen.

        """
        rolls_left = 2 - roll
        
        if entscheidung == "Einser":
            kept_dices = [x for x in dice_rolls if x == 1] # Halte Würfel nit Augenzahl 1 in allen Runden
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Zweier":
            kept_dices = [x for x in dice_rolls if x == 2] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Dreier":
            kept_dices = [x for x in dice_rolls if x == 3] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Vierer":
            kept_dices = [x for x in dice_rolls if x == 4] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Fünfer":
            kept_dices = [x for x in dice_rolls if x == 5] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Sechser":
            kept_dices = [x for x in dice_rolls if x == 6] # Analog zu Fall Einser
            #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
            return kept_dices
        elif entscheidung == "Dreierpasch":
            if rolls_left == 2:
                Zähler = Counter(dice_rolls)
                ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Hinzufügen zu kept_dices
                # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                if len(kept_dices) < 3: # Fall: Noch kein Dreierpasch vorhanden
                    if not kept_dices == True: # Im Fall einer leeren Liste
                        Zähler = Counter(dice_rolls)
                        ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                        Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                        Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))] # Hält höchste Anzahl an Augenwerten
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    else:
                        Zähler = Counter(kept_dices) # Zählung bereits gehaltener Würfel
                        Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]# Hält Augenzahlen die zu denen in kept_dices passen
                    return kept_dices
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                elif len(kept_dices) >=3: 
                    kept_dices = [x for x in dice_rolls if x > 3.5] # Optimierung, fall schon ein Dreierpasch vorliegt. Wir halten Würfel größer als den Erwartungswertes eines Würfels.
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
        elif entscheidung == "Viererpasch": # Vorgehen hier analog zu Dreierpasch
            if rolls_left == 2:
                Zähler = Counter(dice_rolls)
                ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                if len(kept_dices) < 4:
                    if not kept_dices == True:
                        Zähler = Counter(dice_rolls)
                        ZählerWertAugenzahl = {key: key*value for key,value in Zähler.items()}
                        Auswahl = {key: value*ZählerWertAugenzahl[key] for key,value in Zähler.items()}
                        Zu_Halten = list(Auswahl.keys())[list(Auswahl.values()).index(max(Auswahl.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    else:
                        Zähler = Counter(kept_dices)
                        Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                        kept_dices = [x for x in dice_rolls if x == Zu_Halten]
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                elif len(kept_dices) >=4: 
                    kept_dices = [x for x in dice_rolls if x > 3.5] #### Optimierung vielleicht?
                    # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
        elif entscheidung == "Full House":
            if rolls_left == 2:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                if len(set(dice_rolls)) == 1: #Spezialfall Kniffel
                    Zähler = Counter(dice_rolls) # Zählung Anzahl Augen in dice_rolls
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Entscheidung für das Halten mit dem höchsten Vorkommen
                    WieOftSchonHinzugefügt = {Zu_Halten1:0} # Erstellen einer Dictionary zum Zählen des Hinzufügens
                    for i in dice_rolls: # Schleife die so lange über dice_rolls iteriert, bis die zu haltende Augenzahl dreimal gehalten wird.
                        if i == Zu_Halten1 and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                else: # Ähnlich zu oben, nur dass hier jetzt zwei verschiedene Augenzahlen gehalten werden sollen
                    Zähler = Counter(dice_rolls)
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Erste zu haltende Augenzahl aus dem Counter
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]] # Löscht den Eintrag in der Dictionary mit der höchsten Augenzahlanzahl
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Zweite zu haltende Augenzahl aus dem Counter
                    WieOftSchonHinzugefügt = {Zu_Halten1:0,Zu_Halten2:0} # Ab hier wieder wie im oberen Fall
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices  
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                Zähler = Counter(kept_dices)
                if len(set(kept_dices)) == 2 and any(kept_dices.count(dice) == 3 for dice in kept_dices) == True: #Fall: Full House liegt schon vor
                    return kept_dices
                elif not Zähler: # Fall: Leerer Counter in Zähler
                    Zähler = Counter(dice_rolls) # Ab hier analoges Vorgehen wie in rolls_left == 2 Fall else
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    WieOftSchonHinzugefügt = {Zu_Halten1:0,Zu_Halten2:0}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices  
                elif len(Zähler) < 2: # Fall Zähler enthält nur eine Augenzahl, eine beliebige andere Augenzahl wird noch benötigt    
                    Zähler_dice_rolls = Counter(dice_rolls) 
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Augenzahl die bereits gehalten wird
                    Zu_Halten2 = list(Zähler_dice_rolls.keys())[list(Zähler_dice_rolls.values()).index(max(Zähler_dice_rolls.values()))] # Augenzahl die noch gesucht wird
                    Anzahl1 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    Anzahl2 = 0
                    WieOftSchonHinzugefügt = {Zu_Halten1:Anzahl1,Zu_Halten2:Anzahl2}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    return kept_dices
                else: # Fall zwei verschiedende Augenzahlen in kept_dices
                    Zähler = Counter(kept_dices)
                    Zu_Halten1 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Zu_Halten2 = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]
                    Zähler = Counter(kept_dices)
                    Anzahl1 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    del Zähler[list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))]]
                    Anzahl2 = list(Zähler.values())[list(Zähler.values()).index(max(Zähler.values()))]
                    WieOftSchonHinzugefügt = {Zu_Halten1:Anzahl1,Zu_Halten2:Anzahl2}
                    for i in dice_rolls:
                        if (i == Zu_Halten1 or i == Zu_Halten2) and WieOftSchonHinzugefügt[i] < 3:
                            kept_dices.append(i)
                            WieOftSchonHinzugefügt[i] += 1
                    return kept_dices
        elif entscheidung == "Kleine Straße":
            KleineStraßen = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
            if rolls_left == 2:
                PassendeWerte = []
                for i in range(0,3):
                    PassendeWerte.append(list(set([x for x in dice_rolls if x in KleineStraßen[i]]))) # Hinzufügen passender Augenzahlen in Liste PassendeWerte für jede Straße
                BesteStraße = max(PassendeWerte, key=len) # Definition der besten Straße, eben jener bei der die meisten Augenzahlen übereinstimmen. 
                kept_dices = BesteStraße # Die Augenzahlen aus der besten Straße werden gehalten
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                FehltNoch = [] 
                for i in range(0,3):
                    FehltNoch.append([x for x in KleineStraßen[i] if x not in kept_dices]) # Fehlende Augenzahlen, die noch nicht in kept_dices sind
                FehltAmWenigsten = min(FehltNoch, key=len) # Definiert die wenigsten fehlenden Augenzahlen
                kept_dices = list(set([x for x in FehltAmWenigsten if x in dice_rolls])) # Wenigste fehlende Augenzahlen werden gehalten
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
        elif entscheidung == "Große Straße": # Vorgehen analog zu Kleine Straße
            GroßeStraßen = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
            if rolls_left == 2:
                PassendeWerte = []
                for i in range(0,2):
                    PassendeWerte.append(list(set([x for x in dice_rolls if x in GroßeStraßen[i]])))
                BesteStraße = max(PassendeWerte, key=len)
                kept_dices = BesteStraße
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                FehltNoch = []
                for i in range(0,2):
                    FehltNoch.append([x for x in GroßeStraßen[i] if x not in kept_dices])
                FehltAmWenigsten = min(FehltNoch, key=len)    
                kept_dices = list(set([x for x in FehltAmWenigsten if x in dice_rolls]))
                #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
        elif entscheidung == "Kniffel":
            if rolls_left == 2:
                Zähler = Counter(dice_rolls) # Zählt Anzahl der Würfelaugen
                Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die am häufigsten vorkommen
                kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfel zu kept_dices
               # print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                return kept_dices
            if rolls_left == 1:
                # print(f'Wurf: {roll}')
                # print(f'Gewürfelt: {dice_rolls}')      
                # print(f'Behalten: {kept_dices}')
                # print(f'Entscheidung: {entscheidung}')
                Zähler = Counter(kept_dices) # Wir schauen welche Würfel nach Runde 2 unseren gehaltenen Würfeln entsprechen
                if not Zähler: # Fall kept_dices ist leer
                    Zähler = Counter(dice_rolls) # Zählt Anzahl der Würfelaugen
                    Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die am häufigsten vorkommen
                    kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfen von dice_rolls zu kept_dices
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
                else:
                    Zu_Halten = list(Zähler.keys())[list(Zähler.values()).index(max(Zähler.values()))] # Solche Würfel halten, die Augenzahl gehaltener Würfel entsprechen
                    kept_dices = [x for x in dice_rolls if x == Zu_Halten] # Passende Würfel werden behalten
                    #print(f'Debug: Entscheidung{entscheidung} -> Behalten {kept_dices}')
                    return kept_dices
    
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
        Eingabe = self.Feldeingabe(dice_values, scoreboard) # Fordert Eingabe aus Feldeingabe() an
        # print(f'Finale Werte: {dice_values}')
        # print(f'Finale Entscheidung: {Eingabe}')
        return Eingabe
    
    def Feldeingabe(self, dice_values, scoreboard):
        """
        Parameters
        ----------
        dice_values : list
            Alle Würfel nach allen Würfelrunden.
        scoreboard : dict
            Scorebpard des Spiels.

        Returns
        -------
        str
            Feldentscheidung.

        """
        #dice_values = [random.randint(1,6) for _ in range(0,5)]
        #print(dice_values)
        Kombination = {}
        # Passt Kombination zum Feld
        #x_er
        for i in range(1,7):
            x_er = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"][i - 1]
            if i in dice_values:
                Kombination[x_er] = True
            else:
                Kombination[x_er] = False
        #Dreierpasch
        if max(dice_values.count(dice) for dice in dice_values) >= 3:
            Kombination["Dreierpasch"] = True
        else:
            Kombination["Dreierpasch"] = False
        #Viererpasch
        if max(dice_values.count(dice) for dice in dice_values) >= 4:
            Kombination["Viererpasch"] = True
        else:
            Kombination["Viererpasch"] = False
        #Full House
        if len(set(dice_values)) == 2 and any(dice_values.count(dice) == 3 for dice in dice_values):
            Kombination["Full House"] = True
        else:
            Kombination["Full House"] = False
        #Kleine Straße
        if any(all(x in dice_values for x in seq) for seq in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
            Kombination["Kleine Straße"] = True
        else:
            Kombination["Kleine Straße"] = False
        #Große Straße
        if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values):
            Kombination["Große Straße"] = True
        else:
            Kombination["Große Straße"] = False
        #Kniffel
        if len(set(dice_values)) == 1:
            Kombination["Kniffel"] = True
        else:
            Kombination["Kniffel"] = False
            
        #Regelbasiertes Eintragen wenn Kombination stimmt und Feld frei
        if scoreboard[self.name]["Kniffel"] is None and Kombination["Kniffel"] is True:
            return "Kniffel"
        elif scoreboard[self.name]["Große Straße"] is None and Kombination["Große Straße"] is True:
            return "Große Straße"
        elif scoreboard[self.name]["Kleine Straße"] is None and Kombination["Kleine Straße"] is True:
            return "Kleine Straße"
        elif scoreboard[self.name]["Full House"] is None and Kombination["Full House"] is True:
            return "Full House"
        elif scoreboard[self.name]["Sechser"] is None and Kombination["Sechser"] is True and dice_values.count(6) >=3:
            return "Sechser"
        elif scoreboard[self.name]["Fünfer"] is None and Kombination["Fünfer"] is True and dice_values.count(5) >=3:
            return "Fünfer"
        elif scoreboard[self.name]["Vierer"] is None and Kombination["Vierer"] is True and dice_values.count(4) >=3:
            return "Vierer"
        elif scoreboard[self.name]["Dreier"] is None and Kombination["Dreier"] is True and dice_values.count(3) >=3:
            return "Dreier"
        elif scoreboard[self.name]["Zweier"] is None and Kombination["Zweier"] is True and dice_values.count(2) >=3:
            return "Zweier"
        elif scoreboard[self.name]["Einser"] is None and Kombination["Einser"] is True and dice_values.count(1) >=3:
            return "Einser"
        elif scoreboard[self.name]["Viererpasch"] is None and Kombination["Viererpasch"] is True:
            return "Viererpasch"
        elif scoreboard[self.name]["Dreierpasch"] is None and Kombination["Dreierpasch"] is True:
            return "Dreierpasch"
        elif scoreboard[self.name]["Sechser"] is None and Kombination["Sechser"] is True:
            return "Sechser"
        elif scoreboard[self.name]["Fünfer"] is None and Kombination["Fünfer"] is True:
            return "Fünfer"
        elif scoreboard[self.name]["Vierer"] is None and Kombination["Vierer"] is True:
            return "Vierer"
        elif scoreboard[self.name]["Dreier"] is None and Kombination["Dreier"] is True:
            return "Dreier"
        elif scoreboard[self.name]["Zweier"] is None and Kombination["Zweier"] is True:
            return "Zweier"
        elif scoreboard[self.name]["Einser"] is None and Kombination["Einser"] is True:
            return "Einser"
        else:
            return "Chance"
        

class Withram_1(Kniffel_Player):
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' Entscheidet, welche Würfel Sam behalten möchte. '''
        if not dice_rolls:  # Falls keine Würfel geworfen wurden
            return []  # Keine Würfel zu behalten

        current_dices = dice_rolls + kept_dices
        possible_scores = self.calculate_scores(current_dices)  # Punktzahlen berechnen

        # Prüft spezielle Felder wie Kniffel, Große Straße oder Full House
        for field in ["Kniffel", "Große Straße", "Full House"]:
            if possible_scores[field] > 0 and scoreboard[self.name].get(field) is None:
                return dice_rolls  # Alle Würfel behalten

        # Prüft, ob eine kleine Straße vorliegt
        if possible_scores["Kleine Straße"] > 0 and scoreboard[self.name].get("Kleine Straße") is None:
            return self.find_dices_for_small_street(dice_rolls, kept_dices, current_dices)
             
        # Zählt die Häufigkeit jeder Zahl
        counts = {}
        for dice in current_dices:
            counts[dice] = current_dices.count(dice)


         # Wählt die Zahl mit der höchsten Häufigkeit, bei Gleichstand die größere Zahl
        target = max(counts, key=lambda dice: (counts[dice], dice))
         
         # Ausnahme: Alle Felder, für die die Zahl zählen kann, sind belegt
        number_to_field = {
                 1:"Einser",
                 2:"Zweier",
                 3:"Dreier",
                 4:"Vierer",
                 5:"Fünfer",
                 6:"Sechser"}
                 
        if scoreboard[self.name].get(number_to_field[target]) is not None and \
        all(scoreboard[self.name].get(field) is not None for field in ["Dreierpasch", "Viererpasch","Chance"]):
    
                 # Wenn alle Felder, die für die Zahl relevant sein kann, belegt sind, wähle die nächst häufigere Zahl
                 # Finde das nächst häufigere Zahlenfeld, das noch nicht belegt ist
                 for next_target in sorted(counts, key=lambda dice: (-counts[dice], dice)):
                     if number_to_field.get(next_target) is not None and \
                        scoreboard[self.name].get(number_to_field[next_target]) is None:
                        target = next_target
                        break
                     
         
        return [dice for dice in dice_rolls if dice == target]

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        ''' Anders als Sam fokussiert sich Bob auf die obere Hälfte der Felder, um den Bonus von 35 Punkten zu erhalten '''
        possible_scores = self.calculate_scores(dice_values)  # Mögliche Punkte berechnen

        
        # Falls Kniffel vorliegt, Kniffel wählen     
        if scoreboard[self.name].get("Kniffel") is None and possible_scores["Kniffel"] > 0 :
            return "Kniffel"
        
        # Wenn eine Zahl mindestens 3 mal vorliegt das relevante Zahlenfeld wählen
        for field in ["Einser","Zweier","Dreier","Vierer","Fünfer","Sechser"]:
            field_to_number = {
                "Einser": 1,
                "Zweier": 2,
                "Dreier": 3,
                "Vierer": 4,
                "Fünfer": 5,
                "Sechser": 6
            }                        
            if scoreboard[self.name].get(field) is None and dice_values.count(field_to_number[field]) >= 3:  # Wenn die Zahl mindestens 3 mal vorkommt
                return field  


        # Ansonsten das Feld wählen, was die meisten Punkte bringt    
        for field, score in sorted(possible_scores.items(), key=lambda x: -x[1]):
            if scoreboard[self.name].get(field) is None:  # Wenn das Feld noch nicht ausgefüllt ist
            
                # Überprüfen, ob alle verbleibenden Felder 0 Punkte haben (gegen Ende)
                remaining_fields = [field for field, score in possible_scores.items() if scoreboard[self.name].get(field) is None]
                if all(possible_scores[field] == 0 for field in remaining_fields):
                    # Wenn alle belegbaren Felder 0 Punkte haben, in der festgelegten Reihenfolge auswählen
                    preferred_order = [
                        "Kniffel", "Große Straße", "Viererpasch", "Dreierpasch", "Kleine Straße", \
                            "Full House","Einser","Zweier", "Dreier" , "Vierer", "Fünfer", "Sechser"
                    ]
                    for preferred_field in preferred_order:
                        if preferred_field in remaining_fields:
                            return preferred_field
                else:
                    return field

class Withram_2(Kniffel_Player):
    def decide_which_dices_to_hold(self, scoreboard, kept_dices, dice_rolls, roll):
        ''' Entscheidet, welche Würfel Sam behalten möchte. '''
        if not dice_rolls:  # Falls keine Würfel geworfen wurden
            return []  # Keine Würfel zu behalten

        current_dices = dice_rolls + kept_dices        
        possible_scores = self.calculate_scores(current_dices)  # Punktzahlen berechnen

        # Prüft spezielle Felder wie Kniffel, Große Straße oder Full House
        for field in ["Kniffel", "Große Straße", "Full House"]:
            if possible_scores[field] > 0 and scoreboard[self.name].get(field) is None:
                return dice_rolls  # Alle Würfel behalten

        # Prüft, ob eine kleine Straße vorliegt
        if possible_scores["Kleine Straße"] > 0 and scoreboard[self.name].get("Kleine Straße") is None:
            return self.find_dices_for_small_street(dice_rolls, kept_dices, current_dices)

        # Prüft, ob eine große Straße vorbereitet werden kann, wenn die kleine Straße bereits vergeben ist
        if scoreboard[self.name].get("Große Straße") is None:
            if all(num in current_dices for num in [2, 3, 4, 5]):
                # Würfel für eine große Straße wählen, falls sinnvoll
                return [dice for dice in set(dice_rolls) if dice in [2, 3, 4, 5] and dice not in kept_dices]
        
        # Zählt die Häufigkeit jeder Zahl
        counts = {}
        for dice in current_dices:
            counts[dice] = current_dices.count(dice)

        # Wählt die Zahl mit der höchsten Häufigkeit, bei Gleichstand die größere Zahl
        target = max(counts, key=lambda dice: (counts[dice], dice))
        
        # Ausnahme: Alle Felder, für die die Zahl zählen kann, sind belegt
        number_to_field = {
                1:"Einser",
                2:"Zweier",
                3:"Dreier",
                4:"Vierer",
                5:"Fünfer",
                6:"Sechser"}
                
        if scoreboard[self.name].get(number_to_field[target]) is not None and \
        all(scoreboard[self.name].get(field) is not None for field in ["Dreierpasch", "Viererpasch", "Chance"]):
        # Wenn alle Felder, die für die Zahl relevant sind, belegt sind, wähle die nächst häufigere Zahl
        # Finde das nächst häufigere Zahlenfeld, das noch nicht belegt ist
            for next_target in sorted(counts, key=lambda dice: (-counts[dice], dice)):
                if number_to_field.get(next_target) is not None and \
                   scoreboard[self.name].get(number_to_field[next_target]) is None:
                   target = next_target
                   break
                    
        
        return [dice for dice in dice_rolls if dice == target]

    def decide_which_field_to_enter(self, scoreboard, dice_values):
        ''' Sam fokussiert sich auf die unteren Felder des Scoreboards, um dort möglichst viele Punkte zu erhalten'''
        
        possible_scores = self.calculate_scores(dice_values)  # Mögliche Punkte berechnen

        
        # Spezialfelder priorisiert auswählen
        # Hinweis: Große und kleine Straßen müssen nicht extra geprüft werden
        for field in ["Kniffel","Full House","Viererpasch"]:
            if scoreboard[self.name].get(field) is None and possible_scores[field] > 0 :
                return field
        
        
        # Wenn eine Zahl mindestens 3 mal vorliegt das relevante Zahlenfeld wählen
        for field in ["Einser","Zweier","Dreier","Vierer","Fünfer","Sechser"]:
            field_to_number = {
                "Einser": 1,
                "Zweier": 2,
                "Dreier": 3,
                "Vierer": 4,
                "Fünfer": 5,
                "Sechser": 6
            }                        
            if scoreboard[self.name].get(field) is None and dice_values.count(field_to_number[field]) >= 3:  # Wenn die Zahl mindestens 3 mal vorkommt
                return field           
        
       # Ansonsten das Feld wählen, was die meisten Punkte bringt 
        for field, score in sorted(possible_scores.items(), key=lambda x: -x[1]):
            if scoreboard[self.name].get(field) is None:  # Wenn das Feld noch nicht ausgefüllt ist 
            
                # Überprüfen, ob alle verbleibenden Felder 0 Punkte haben (gegen Ende)
                remaining_fields = [field for field, score in possible_scores.items() if scoreboard[self.name].get(field) is None]
                if all(possible_scores[field] == 0 for field in remaining_fields):
                    # Wenn alle belegbaren Felder 0 Punkte haben, in der festgelegten Reihenfolge auswählen
                    preferred_order = [
                       "Einser", "Kniffel", "Große Straße", "Viererpasch","Zweier", 
                       "Dreier", "Dreierpasch", "Kleine Straße", "Full House", "Vierer", "Fünfer", "Sechser"
                   ]
                    for preferred_field in preferred_order:
                        if preferred_field in remaining_fields:
                            return preferred_field
                else:
                    return field  
      






        
  
                
                
                
                
                
                
                
                
    