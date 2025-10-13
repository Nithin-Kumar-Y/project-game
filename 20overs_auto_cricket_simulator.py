print("Welcome to partial aggresive cricket simulator")
import random
import time

user_team = input("Enter your team name: ")
user_players = []
for i in range(1, 12):
    player_name = input(f"Enter the name of player {i}: ")
    user_players.append(player_name)
gpt_team = "GPT AUSTRALIA"
gpt_players = ["David Warner", "Steve Smith", "Marnus Labuschagne", "Glenn Maxwell","McGarth", "Pat Cummins", "Mitchell Starc", "Adam Zampa", "Marcus Stoinis", "Josh Hazlewood", "Tim David"]
overs = 20
print(f"Toss time!! {user_team} vs {gpt_team}")
toss_call = input("Enter the call (heads / tails): ").lower()
toss_output = random.choice(["heads", "tails"])
user_choice  = ""
gpt_choice = ""
if toss_call == toss_output:
    print(f"You won the toss!! {toss_output}")
    user_choice = input("Do you want to bat first or bowl first (bat/ bowl): ").lower()
else:
    gpt_choice = random.choice(["bat", "bowl"])
    print(f"You loss the toss. {gpt_team} choose to {gpt_choice} ")
user_players_score = {player: 0 for player in user_players}
gpt_players_score = {player: 0 for player in gpt_players}
# Decide who is batting first
def innings(batting_team, bowling_team):
    if batting_team == user_team:
        batting_players = user_players
        bowling_players = gpt_players
        batting_players_score = user_players_score
    else:
        batting_players = gpt_players
        bowling_players = user_players
        batting_players_score = gpt_players_score
    score = 0
    wickets = 0
    striker_index = 0
    non_striker_index = 1
    bowler_index = 2
    print(f"{batting_team} players: {', '.join(batting_players)}")
    print(f"{bowling_team} players: {', '.join(bowling_players)}")
    time.sleep(2)
    for over_wise in range(overs):
        print(f"Over {over_wise + 1}:")
        bowler = bowling_players[bowler_index % len(bowling_players)]
        print(f"{bowler} is bowling")
        for ball in range(1, 7):
            runs = random.choices([0, 1, 2, 3, 4, 5, 6, 'W'], weights=[10, 15, 15, 10, 20, 2, 15, 13])[0]
            if runs == 'W':
                wickets +=1
                out_player = batting_players[striker_index]
                print(f"{out_player} is out!")
                striker_index += 1
                print(f"{out_player} scored {batting_players_score[out_player]} runs")
                print(f"Wicket! {wickets} down")
                print(f"Next player is {batting_players[striker_index] if striker_index < len(batting_players) else 'No more players'}")
                time.sleep(1)
                if wickets == 10 or striker_index >= len(batting_players):
                    return score, wickets

            else:
                score +=runs
                batting_players_score[batting_players[striker_index]] += runs
                if runs % 2 == 1:
                    striker_index, non_striker_index = non_striker_index, striker_index
            print(runs, end=' ')
            time.sleep(1)
        print(f"score after {over_wise +1 } is {score}/{wickets}")  # New line after each over
        bowler_index += 1
        striker_index, non_striker_index = non_striker_index, striker_index
        if wickets == 10 or striker_index >= len(batting_players):
            break
    return score, wickets
if user_choice == "bat" or gpt_choice == "bowl":
    print(f"{user_team} is batting first")
    score1, wickets1 = innings(user_team, gpt_team)
    print(f"{user_team} scored {score1}/{wickets1}")
    print(f"----------{gpt_team} need {score1 +1} to win----------")
    time.sleep(2)
    print(f"{gpt_team} is batting second")
    score2, wickets2 = innings(gpt_team, user_team)
    print(f"{gpt_team} scored {score2}/{wickets2}")
    print("Match Result:")
    time.sleep(2)
    if score1 > score2:
        print(f"{user_team} wins by {score1 - score2} runs")
    elif score2 > score1:
        print(f"{gpt_team} wins by {10 - wickets2} wickets")
    else:
        print("It's a tie!")
    print(f"{user_team} players scores: {user_players_score}")
    print(f"{gpt_team} players scores: {gpt_players_score}")
else:
    print(f"{gpt_team} is batting first")
    score1, wickets1 = innings(gpt_team, user_team)
    print(f"{gpt_team} scored {score1}/{wickets1}")
    print(f"----------{user_team} need {score1 +1} to win----------")
    time.sleep(2)
    print(f"{user_team} is batting second")
    score2, wickets2 = innings(user_team, gpt_team)
    print(f"{user_team} scored {score2}/{wickets2}")
    print("Match Result:")
    time.sleep(2)
    if score1 > score2:
        print(f"{gpt_team} wins by {score1 - score2} runs")
    elif score2 > score1:
        print(f"{user_team} wins by {10 - wickets2} wickets")
    else:
        print("It's a tie!")
    print(f"{user_team} players scores: {user_players_score}")
    print(f"{gpt_team} players scores: {gpt_players_score}")

## May have some bugs 
## will be fix later