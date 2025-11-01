import random
import time

print("Welcome to NRI Cricket Simulator")

overs = 2

def team_up():
    print("You VS GPT-team cricket")
    user_team = input("Enter name of your team: ")
    print(f"So, it's {user_team} VS Mighty Australia")

    user_players = []
    for i in range(1, 12):
        player = input(f"Enter the player {i}: ")
        user_players.append(player)

    user_bowlers = []
    print("Select 5 bowlers from your playing XI")
    while len(user_bowlers) < 5:
        bowler = input("Enter bowler name: ")
        if bowler in user_players and bowler not in user_bowlers:
            user_bowlers.append(bowler)
        else:
            print("Retry bowler name.")

    gpt_team = "Mighty Australia"
    gpt_players = [
        "David Warner", "Travis Head", "Mitchell Marsh", "Marnus Labuschagne",
        "Ricky Ponting", "Tim David", "Marcus Stoinis", "Pat Cummins",
        "Mitchell Starc", "Adam Zampa", "Josh Hazlewood"
    ]
    gpt_bowlers = ["Marcus Stoinis", "Pat Cummins", "Mitchell Starc", "Josh Hazlewood", "Adam Zampa"]

    template = {
        "total_matches_played": 0, 
        "total_outs": 0,
        "total_runs_scored": 0,
        "total_balls_faced": 0, 
        "total_fours": 0, 
        "total_sixers": 0,
        "total_boundaries": 0,
        "total_balls_bowled": 0, 
        "total_overs_bowled": 0, 
        "total_wickets_taken": 0, 
        "total_dot_balls_bowled": 0,
        "total_economy": 0, 
        "total_performance_score":0
    }

    user_stats = {p: template.copy() for p in user_players}
    gpt_stats = {p: template.copy() for p in gpt_players}

    return user_team, gpt_team, user_players, gpt_players, user_stats, gpt_stats, user_bowlers, gpt_bowlers

template_keys = "runs_scored", "balls_faced", "fours", "sixers", "boundaries", "balls_bowled", "overs_bowled", "wickets_taken", "dot_balls","economy", "performance_score"

def toss(user_team, gpt_team, user_players, gpt_players, user_bowlers, gpt_bowlers, user_series, gpt_series):
    print(f"Toss time!! {user_team} vs {gpt_team}")
    toss_call = input("Enter the call (heads/tails): ").lower()
    toss_output = random.choice(["heads", "tails"])

    user_choice = ""
    gpt_choice = ""

    user_match = {p: {"runs_scored": 0, "balls_faced": 0, "wickets_taken": 0, "balls_bowled": 0,
                      "runs_conceded": 0, "economy": 0, "fours": 0, "sixers": 0, "boundaries": 0, "dotballs": 0}
                  for p in user_players}
    gpt_match = {p: {"runs_scored": 0, "balls_faced": 0, "wickets_taken": 0, "balls_bowled": 0,
                     "runs_conceded": 0, "economy": 0, "fours": 0, "sixers": 0, "boundaries": 0, "dotballs": 0}
                 for p in gpt_players}

    if toss_call == toss_output:
        print(f"You won the toss ({toss_output})!")
        user_choice = input("Do you want to bat or bowl? (bat/bowl): ").lower()
    else:
        gpt_choice = random.choice(["bat", "bowl"])
        print(f"You lost the toss. {gpt_team} chose to {gpt_choice}.")

    if user_choice == "bat" or gpt_choice == "bowl":
        batting_team, bowling_team = user_team, gpt_team
        batting_players, bowling_players = user_players, gpt_players
        batting_match, bowling_match = user_match, gpt_match
        batting_series, bowling_series = user_series, gpt_series
        bowling_bowlers, batting_bowlers = gpt_bowlers, user_bowlers
    else:
        batting_team, bowling_team = gpt_team, user_team
        batting_players, bowling_players = gpt_players, user_players
        batting_match, bowling_match = gpt_match, user_match
        batting_series, bowling_series = gpt_series, user_series
        bowling_bowlers, batting_bowlers = user_bowlers, gpt_bowlers

    return batting_team, bowling_team, batting_players, bowling_players, batting_match, bowling_match, bowling_bowlers,batting_bowlers, batting_series, bowling_series


def innings(batting_team, bowling_team, batting_players, bowling_players,
            batting_match, bowling_match, bowling_bowlers,
            batting_series, bowling_series, chasing=False, target=None):
    score = 0
    wickets = 0
    striker_index = 0
    non_striker_index = 1
    bowler_index = 0

    print(f"\n{batting_team} batting lineup: {', '.join(batting_players)}")
    time.sleep(1)

    for over in range(overs):
        if chasing and target is not None and score > target:
            print(f"{batting_team} has chased the target successfully!")
            return score, wickets

        bowler = bowling_bowlers[bowler_index % len(bowling_bowlers)]
        bowler_index += 1
        print(f"\nOver {over + 1}: {bowler} to bowl")

        for ball in range(1, 7):
            runs = random.choices([0, 1, 2, 3, 4, 6, 'W'],
                                  weights=[10, 15, 15, 5, 20, 10, 10])[0]

            if runs == 'W':
                wickets += 1
                out_player = batting_players[striker_index]
                print(f"\n{out_player} is OUT!")
                batting_match[out_player]["balls_faced"] += 1
                batting_series[out_player]["total_balls_faced"] += 1
                bowling_match[bowler]["wickets_taken"] += 1
                bowling_series[bowler]["total_wickets_taken"] += 1

                if wickets == len(batting_players) - 1:
                    print("All out!")
                    return score, wickets

                next_index = max(striker_index, non_striker_index) + 1
                if next_index < len(batting_players):
                    striker_index = next_index
                    print(f"Next player: {batting_players[striker_index]}")
                else:
                    print("No players left.")
                    return score, wickets

            else:
                score += runs
                batting_match[batting_players[striker_index]]["runs_scored"] += runs
                batting_series[batting_players[striker_index]]["total_runs_scored"] += runs
                batting_match[batting_players[striker_index]]["balls_faced"] += 1
                batting_series[batting_players[striker_index]]["total_balls_faced"] += 1

                bowling_match[bowler]["balls_bowled"] += 1
                bowling_series[bowler]["total_balls_bowled"] += 1
                bowling_match[bowler]["runs_conceded"] += runs

                if runs == 4:
                    batting_match[batting_players[striker_index]]["fours"] += 1
                    batting_series[batting_players[striker_index]]["total_fours"] += 1
                    batting_match[batting_players[striker_index]]["boundaries"] += 1
                    batting_series[batting_players[striker_index]]["total_boundaries"] += 1

                if runs == 6:
                    batting_match[batting_players[striker_index]]["sixers"] += 1
                    batting_series[batting_players[striker_index]]["total_sixers"] += 1
                    batting_match[batting_players[striker_index]]["boundaries"] += 1
                    batting_series[batting_players[striker_index]]["total_boundaries"] += 1

                if runs == 0:
                    bowling_match[bowler]["dotballs"] += 1
                    bowling_series[bowler]["total_dot_balls_bowled"] += 1

                if runs % 2 == 1:
                    striker_index, non_striker_index = non_striker_index, striker_index

                if chasing and target is not None and score >= target:
                    print(runs)
                    print(f"\nTarget achieved! {batting_team} wins by {10 - wickets} wickets.")
                    return score, wickets

            print(runs, end=' ')
        print(f"\nEnd of Over {over + 1}: {score}/{wickets}")
        striker_index, non_striker_index = non_striker_index, striker_index
        input("Press Enter for next over...")

    return score, wickets


def match_call(matches, user_team_series,gpt_team_series):
    user_team, gpt_team, user_players, gpt_players, user_series, gpt_series, user_bowlers, gpt_bowlers = team_up()
    print(f"________________{user_team} VS {gpt_team}____________")
    batting_team, bowling_team, batting_players, bowling_players, batting_match, bowling_match, bowling_bowlers,batting_bowlers, batting_series, bowling_series = toss(
        user_team, gpt_team, user_players, gpt_players, user_bowlers, gpt_bowlers, user_series, gpt_series
    )

    score1, wickets1 = innings(batting_team, bowling_team, batting_players, bowling_players,
                               batting_match, bowling_match, bowling_bowlers,
                               batting_series, bowling_series)

    target = score1 + 1
    print(f"{bowling_team} need {target} runs to win from {overs} overs")
    score2, wickets2 = innings(bowling_team, batting_team, bowling_players, batting_players,
                               bowling_match, batting_match, batting_bowlers,
                               bowling_series, batting_series, chasing=True, target=target)

    if score1 > score2:
        print(f"{batting_team} wins by {score1 - score2} runs.")
        if batting_team == user_team:
            user_team_series +=1
            return user_team, user_team_series, gpt_team_series, user_team, gpt_team
        else:
            gpt_team_series +=1
            return gpt_team, user_team_series, gpt_team_series, user_team, gpt_team
    elif score2 >= target:
        print(f"{bowling_team} wins by {10 - wickets2} wickets.")
        if bowling_team == user_team:
            user_team_series +=1
            return user_team, user_team_series, gpt_team_series, user_team, gpt_team
        else:
            gpt_team_series +=1
            return gpt_team, user_team_series, gpt_team_series, user_team, gpt_team
    else:
        print("Match Draw")
        user_team_series += 0.5
        gpt_team_series += 0.5
        return None, user_team_series, gpt_team_series, user_team, gpt_team
    
def series_call():
    matches = int(input("Enter the number of matches you want in this series: "))
    user_team_series, gpt_team_series = 0,0
    for i in range(1, matches+1):
        print(f"___________Match {i}________________")
        match_winner, user_team_series, gpt_team_series, user_team, gpt_team = match_call(matches, user_team_series, gpt_team_series)
        ### Series team scorecard
        if user_team_series > gpt_team_series:
            lead = f"{user_team_series} - {gpt_team_series}"
            print(f"{user_team} lead the series of {matches} by {lead}")
        elif user_team_series < gpt_team_series:
            lead = f"{gpt_team_series} - {user_team_series}" 
            print(f"{gpt_team} lead the series of {matches} by {lead}")
        else:
            lead = None
            if user_team_series and gpt_team_series == 0:
                lead = f"{user_team_series} - {gpt_team_series}"
                print("Series in tie Yet!!")
            else:
                lead = f"{user_team_series} - {gpt_team_series}"
                print(f"Series is Draw of {user_team_series} each")

    winner = user_team if user_team_series > gpt_team_series else gpt_team if gpt_team_series > user_team_series else "Draw"
    return winner

winner_of_the_series = series_call()
print(f"{winner_of_the_series} won the series!!! CONGRATULATIONS TO {winner_of_the_series}")
