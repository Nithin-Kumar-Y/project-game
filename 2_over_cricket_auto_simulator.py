import random
print("welcome to Cricket Game")
class cricket_simulator:
    user_team = input("Enter your team name: ")
    gpt_team = "GPT Team"
    overs = 2
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
    # Decide who is batting first
    if user_choice == "bat" or gpt_choice == "bowl":
        # User is batting first
        score1 = 0                  
        wickets1 = 0
        for over_wise in range(overs):
            for ball in range(1, 7):
                runs = random.choice([0, 1, 2, 3, 4, 5, 6, 'W'])
                if runs == 'W':
                    wickets1 +=1
                    if wickets1 == 2:
                        print("W (All out!!)")
                        break
                else:
                    score1 +=runs
                print(runs, end=' ')
            print()  # New line after each over
            if wickets1 == 2:
                break
        print(f"{user_team} scored {score1}/{wickets1} in {over_wise}.{ball if wickets1 < 2 else ball}")
        print(f"----------{gpt_team} need {score1 +1} to win----------")

        # GPT is batting second
        score2 = 0
        wickets2 = 0
        for over_wise in range(overs):
            for balls in range(1, 7):
                runs = random.choice([0, 1, 2, 3, 4, 5, 6, 'W'])
                if runs == 'W':
                    wickets2 +=1
                    if wickets2 == 2:
                        print("W (All out!!)")
                        break
                else:
                    score2 +=runs
                    if score2 > score1:
                        break
                print(runs, end=' ')
            print()  # New line after each over
            if wickets2 == 2 or score2 > score1:
                break
            print(runs, end=' ')
        print()  # New line after each over
        if score1> score2:
            print(f"{gpt_team} has scored {score2}/{wickets2} in {over_wise}.{ball if wickets2 < 2 else ball}")
            print(f"-----{user_team} won by {score1- score2} runs-----")
        elif score1 < score2:
            print(f"{gpt_team} has chase in {over_wise}.{ball}")
            print(f"scored {score2}/{wickets2} in {over_wise}.{ball if wickets2 < 2 else ball}")
            print(f"-------{gpt_team} won by {score2 - score1} runs-------")
        else:
            print("Match Tied!!!")
    else:
        # GPT is batting first
        score1 = 0
        wickets1 = 0
        for over_wise in range(overs):
            for balls in range(1, 7):
                runs = random.choice([0, 1, 2, 3, 4, 5, 6, 'W'])
                if runs == 'W':
                    wickets1 += 1
                    if wickets1 == 2:
                        print("W (All out!!)")

                        break
                else:
                    score1 += runs
                print(runs, end=' ')
            print()  # New line after each over
        print(f"{gpt_team} has scored {score1}/{wickets1} in {over_wise}.{balls if wickets1 < 2 else balls}")
        print(f"-----{user_team} need {score1 +1} to win-----")

        # User is batting second
        score2 = 0
        wickets2 = 0
        for over_wise in range(overs):
            for balls in range(1, 7):
                runs = random.choice([0, 1, 2, 3, 4, 5, 6, 'W'])
                if runs == 'W':
                    wickets2 +=1
                    if wickets2 == 2:
                        print("W (All out!!)")
                        break
                
                else:
                    score2 += runs
                    if score2 > score1:
                        break
                print(runs, end=' ')
            print()  # New line after each over
            if wickets2 == 2 or score2 > score1:
                break
        if score1 > score2:
            print(f"{user_team} scored {score2}/{wickets2} in {over_wise}.{balls if wickets2 < 2 else balls}")
            print(f"-------{gpt_team} won by {score1 - score2} runs-------")
        elif score1 < score2:
            print(f"{user_team} has chase in {over_wise}.{balls}")
            print(f"scored {score2}/{wickets2} in {over_wise}.{balls if wickets2 < 2 else balls}")
            print(f"-------{user_team} has won by {2 - wickets2} runs-------")
        else:
            print("Match Tied!!!")

cricket_simulator