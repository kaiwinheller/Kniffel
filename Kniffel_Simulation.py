import Kniffel_Game
import Kniffel_Player

if __name__ == '__main__':
    # Player 1
    player_1 = Kniffel_Player.Kniffel_Player_2('Seb')
    # Player 2
    player_2 = Kniffel_Player.Kniffel_Player('Tom')

    wincounter = [0,0]
    # Create Game
    game = Kniffel_Game.Kniffel_Game([player_1, player_2])
    for game_iteration in range(10000):
        scoreboard = game.simulate_one_game()
        if game.evaluate_score(scoreboard, player_1) > game.evaluate_score(scoreboard, player_2):
            wincounter[0] += 1
        elif game.evaluate_score(scoreboard, player_1) < game.evaluate_score(scoreboard, player_2):
            wincounter[1] += 1
        else:
            print('We have a tie')
    print(f'{player_1.name} won {wincounter[0]} times while {player_2.name} won {wincounter[1]} times!')