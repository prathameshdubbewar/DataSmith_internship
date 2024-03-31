def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age >= 18:
            print("You can vote.")
        else:
            print("You cannot  vote")
    except ValueError:
        print("Invalid input Please enter age as an integer.")

check_voting_eligibility()
