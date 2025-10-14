print("Welcome to partial aggresive cricket simulator")
import random
import time

user_team = input("Enter your team name: ")
user_players = []
for i in range(1, 12):
    player_name = input(f"Enter the name of player {i}: ")
    user_players.append(player_name)
gpt_team = "Mighty Australia"
gpt_players = ["David Warner", "Steve Smith", "Marnus Labuschagne", "Glenn Maxwell","Tim David", "Marcus Stoinis", "Pat Cummins", "Adam Zampa", "Josh Hazlewood", "Mitchell Starc", "McGarth"]
overs = 14
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
# Initialize player stats
user_player_stats = {player: {"runs_score": 0, "balls_faced": 0, "wickets_taken": 0, "balls_bowled": 0, "runs_conceded": 0} for player in user_players}
gpt_player_stats = {player: {"runs_score": 0, "balls_faced": 0, "wickets_taken": 0, "balls_bowled": 0, "runs_conceded": 0} for player in gpt_players}
# Decide who is batting first
def innings(batting_team, bowling_team):
    if batting_team == user_team:
        batting_team = user_team
        bowling_team = gpt_team
        batting_players = user_players
        bowling_players = gpt_players
        batting_stats = user_player_stats
        bowling_stats = gpt_player_stats
    else:
        batting_players = gpt_players
        bowling_players = user_players
        batting_team = gpt_team
        bowling_team = user_team
        batting_stats = gpt_player_stats
        bowling_stats = user_player_stats
    score = 0
    wickets = 0
    striker_index = 0
    non_striker_index = 1
    bowler_index = 8
    print(f"{batting_team} players: {', '.join(batting_players)}")
    print(f"{bowling_team} players: {', '.join(bowling_players)}")
    time.sleep(2)
    for over_wise in range(overs):
        print(f"Over {over_wise + 1}:")
        bowler = bowling_players[bowler_index % len(bowling_players)]
        print(f"{bowler} is bowling")
        for ball in range(1, 7):
            runs = random.choices([0, 1, 2, 3, 4, 5, 6, 'W'], weights=[10, 15, 15, 10, 20, 2, 15, 13])[0]
            bowling_stats[bowler]["balls_bowled"]+=1
            if runs == 'W':
                wickets +=1
                bowling_stats[bowler]["wickets_taken"]+=1
                out_player = batting_players[striker_index]
                batting_stats[out_player]["balls_faced"] += 1
                print(f"\n{out_player} is out!")
                print(f'{out_player} scored {batting_stats[out_player]["runs_score"]} runs')
                print(f"Wicket! {wickets} down")
                striker_index += 1
                print(f"Next player is {batting_players[striker_index] if striker_index < len(batting_players) else 'No more players'}")
                time.sleep(2)
                if wickets == 10 or striker_index >= len(batting_players):
                    return score, wickets

            else:
                score +=runs
                bowling_stats[bowler]["runs_conceded"] += runs
                batting_stats[batting_players[striker_index]]["runs_score"] += runs
                batting_stats[batting_players[striker_index]]["balls_faced"] += 1
                if runs % 2 == 1:
                    striker_index, non_striker_index = non_striker_index, striker_index
            print(runs, end=' ')
            time.sleep(1)
        print(f"score after {over_wise +1 } over is {score}/{wickets}")  # New line after each over
        bowler_index += 1
        striker_index, non_striker_index = non_striker_index, striker_index
        if wickets == 10 or striker_index >= len(batting_players):
            break
    return score, wickets
if user_choice == "bat" or gpt_choice == "bowl":
    print(f"{user_team} is batting first")
    score1, wickets1 = innings(user_team, gpt_team)
    batting_first_team = user_team
    batting_first_team_players_score = {players: stats["runs_score"] for players, stats in user_player_stats.items() if stats["balls_faced"] > 0}
    user_players_score = batting_first_team_players_score
    batting_first_score = f"{score1}/{wickets1}"
    print(f"{user_team} scored {batting_first_score}")
    print(f"----------{gpt_team} need {score1 +1} to win----------")
    time.sleep(2)
    print(f"{gpt_team} is batting second")
    score2, wickets2 = innings(gpt_team, user_team)
    batting_second_team = gpt_team
    batting_second_team_players_score = {players: stats["runs_score"] for players, stats in gpt_player_stats.items() if stats["balls_faced"]> 0}
    gpt_players_score = batting_second_team_players_score
    batting_second_score = f"{score2}/{wickets2}"
    print(f"{batting_second_team} scored {batting_second_score}")
else:
    print(f"{gpt_team} is batting first")
    score1, wickets1 = innings(gpt_team, user_team)
    batting_first_team = gpt_team
    batting_first_team_players_score = {players: stats["runs_score"] for players, stats in gpt_player_stats.items() if stats["balls_faced"] > 0}
    gpt_players_score = batting_first_team_players_score
    print(batting_first_team_players_score)
    batting_first_score = f"{score1}/{wickets1}"
    print(f"{gpt_team} scored {batting_first_score}")
    print(f"----------{user_team} need {score1 +1} to win----------")
    time.sleep(2)
    print(f"{user_team} is batting second")
    score2, wickets2 = innings(user_team, gpt_team)
    batting_second_team = user_team
    batting_second_team_players_score = {players: stats["runs_score"] for players,stats in user_player_stats.items() if stats["balls_faced"] > 0}
    user_players_score = batting_second_team_players_score
    print(batting_second_team_players_score)
    batting_second_score = f"{score2}/{wickets2}"
    print(f"{batting_second_team} scored {batting_second_score}")
time.sleep(2)
print("Match Result:")
if score1 > score2:
    print(f"{batting_first_team} wins by {score1 - score2} runs")
elif score2 > score1:
    print(f"{batting_second_team} wins by {score2 - score1} runs")
else:
    print("It's a tie!")
time.sleep(2)
print("match Summary")
print(f"\n {batting_second_team} innings\t\t\t {score1}/{wickets1}   Overs: {overs}"
      f"\n {'Player':<20}{'Runs':<10}{'Balls':<10}"
      + "\n" + "-"*40 + f"\n" + "\n".join([f"{player:<20}{stats['runs_score']:<10}{stats['balls_faced']:<10}" for player, stats in (user_player_stats if batting_first_team else None).items() if stats["balls_faced"] > 0]) + "\n" + "-"*40 
      + "\n ")
print(f"\n {batting_first_team} innings\t\t\t {score2}/{wickets2}   Overs: {overs}"
      f"\n {'Player':<20}{'Runs':<10}{'Balls':<10}"
      + "\n" + "-"*40 + f"\n" + "\n".join([f"{player:<20}{stats['runs_score']:<10}{stats['balls_faced']:<10}" for player, stats in (gpt_player_stats if batting_second_team else None).items() if stats["balls_faced"] > 0]) + "\n" + "-"*40)  
print(f"\n {batting_second_team} Bowling\t\t\t Overs: {overs}"
      f"\n {'Player':<20}{'Wickets':<10}{'Runs Conceded':<15}{'Balls Bowled':<15}"
      + "\n" + "-"*60 + f"\n" + "\n".join([f"{player:<20}{stats['wickets_taken']:<10}{stats['runs_conceded']:<15}{stats['balls_bowled']:<15}" for player, stats in (user_player_stats if batting_second_team == user_team else gpt_player_stats).items() if stats["balls_bowled"] > 0]) + "\n" + "-"*60)
print(f"\n {batting_first_team} Bowling\t\t\t Overs: {overs}"
        f"\n {'Player':<20}{'Wickets':<10}{'Runs Conceded':<15}{'Balls Bowled':<15}"
        + "\n" + "-"*60 + f"\n" + "\n".join([f"{player:<20}{stats['wickets_taken']:<10}{stats['runs_conceded']:<15}{stats['balls_bowled']:<15}" for player, stats in (gpt_player_stats if batting_first_team == gpt_team else user_player_stats).items() if stats["balls_bowled"] > 0]) + "\n" + "-"*60)
print("Well Played!!")
print("Player of the match: ")
if batting_first_team == user_team:
    print(f"{max(user_players_score, key=user_players_score.get) if score1 > score2 else max(gpt_players_score, key=gpt_players_score.get)}")
else:
    print(f"{max(user_players_score, key=user_players_score.get) if score2 > score1 else max(gpt_players_score, key=gpt_players_score.get)}")
print("Thanks for playing the game")
## only bug is to stop the match when target is reached
## will be fix later