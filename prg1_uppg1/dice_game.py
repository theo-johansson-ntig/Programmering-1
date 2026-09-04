import random
import time

dice_sides = 6
goal = 21
sleep_time = 3

actions_msg = "1) Roll die | 2) Stand"
blackjack_msg = "Blackjack! You win!"
bust_msg = "Bust! You lose!"
current_msg = "Current: {}"
goal_msg = "\nGoal: {}"
invalid_msg = "\nInvalid action!"
roll_msg = "\nYou rolled a {}!"
stand_msg = "\nYour final score is {}.\nYou were {} away from {}."

def dice_throw():
    return random.randint(1, dice_sides)

def diff(goal, total):
    if goal - total < 0:
        return True
    elif goal - total == 0:
        return "Blackjack"
    else:
        return False
    
def end_msg(string):
    print(string)
    time.sleep(sleep_time)


while True:
    total = 0
    while True:
        print(goal_msg.format(goal))
        print(current_msg.format(total))
        print(actions_msg)
        action = input("")

        if action == "1":
            roll = dice_throw()
            total += roll
            print(roll_msg.format(roll))
            if diff(goal, total) == "Blackjack":
                print(blackjack_msg)
                time.sleep(3)
                break
            elif diff(goal, total):
                print(bust_msg)
                time.sleep(3)
                break
            time.sleep(1)
            continue

        elif action == "2":
            print(stand_msg.format(total, goal-total, goal))
            time.sleep(3)
            break

        else:
            print(invalid_msg)
            time.sleep(1)
            continue