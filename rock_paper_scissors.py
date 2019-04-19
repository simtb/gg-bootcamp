import random

if __name__ == "__main__":

    print("Pick Rock(r) or Paper(p) or Scissors(s):")
    user_move = input()

    complete_name = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:

        possible_moves = ["r", "p", "s"]
        computer_move = possible_moves[random.randint(0, 2)]

        if computer_move == "r" and user_move == "s":
            print(f"I win! {complete_name.get(computer_move)} beats {complete_name.get(user_move)}")
            break

        if computer_move == "s" and user_move == "p":
            print(f"I win! {complete_name.get(computer_move)} beats {complete_name.get(user_move)}")
            break

        if computer_move == "p" and user_move == "r":
            print(f"I win! {complete_name.get(computer_move)} beats {complete_name.get(user_move)}")
            break

        if user_move == "r" and computer_move == "s":
            print(f"You win! {complete_name.get(user_move)} beats {complete_name.get(computer_move)}")
            break

        if user_move == "s" and computer_move == "p":
            print(f"You win! {complete_name.get(user_move)} beats {complete_name.get(computer_move)}")
            break

        if user_move == "p" and computer_move == "r":
            print(f"You win! {complete_name.get(user_move)} beats {complete_name.get(computer_move)}")
            break

        print(f"it's a tie! I picked {complete_name.get(computer_move)} and you picked {complete_name.get(user_move)}")
        print("Pick again Rock(r) or Paper(p) or Scissors(s):")
        user_move = input()