from fight import Fight

if __name__ == "__main__":
    fight = Fight()
    actions = fight.simulate()

    for action in actions:
        print(action)
