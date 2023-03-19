from art import logo, vs
from game_data import data
import random
from os import clear


# optimize account data into text
def name_format(account):
    """Takes the account data and returns the printable format"""
    # for A option
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}. ")


# print logo from art module
print(logo)
# variable for Score
score = 0
# checking game is true until wrong answer
game_should_continue = True
# generate options of instagram profiles.
second_account = random.choice(data)


# make the game repeatable
while game_should_continue:
    # move second account value to first account value.
    first_account = second_account
    second_account = random.choice(data)
    if first_account == second_account:
        second_account = random.choice(data)
    
    # check answer function
    def check_answer(guess, a_followers , b_followers):
        """Use if statment to check if user is correct or not."""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"
    
    
    
    # call first phase to see
    print(f"Compare A: {name_format(first_account)}.")
    print(vs)
    print(f"Compare B: {name_format(second_account)}.")
    
    #ask user for a guess option.
    guess = input("Which account has more follower? Type 'A' or 'B' : ").lower()
    
    ## get follower count of each account.
    a_follower_count = first_account["follower_count"]
    b_follower_count = second_account["follower_count"]
    
    ## Use if statment to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between rounds.
    clear()
    
    #print logo after clear the screen.
    print(logo)
    
    # give user feedback on their guess.
    if is_correct:
        # score keeping
        score += 1
        print(f"You're Right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, wrong answer. Final score: {score}")

