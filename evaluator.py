import yahtzee

class Evaluator():
    def __init__(self):
        self.dices = yahtzee.Yatzee.numbers
        self.points = 0
        self.player

    def wrong_strategy(self):
        choice = input("Are you sure you want to do this? Your score would be zero, type 1 to choose another strategy and otherwist 0!")
        if int(choice) == 1:
            strategy = input("Type your new strategy")
            Evaluator.evaluate_strategy(Evaluator, strategy)
        else:
            return 0

    def count_number(number, self):
        occurence = Evaluator.dices.count(number)
        if occurence == 0:
            self.wrong_strategy()
        else:
            return occurence * number

    def count_kinds(number, self):
        for dice_eye in Evaluator.dices:
            if Evaluator.dices.count(dice_eye) <= number:
                return sum(Evaluator.dices)
        self.wrong_strategy()

    def check_full_house(self):
        twoValues = False
        threeValues = False
        for dice_eye in Evaluator.dices:
            if Evaluator.dices.count(dice_eye) == 2:
                twoValues = True
            if Evaluator.dices.count(dice_eye) == 3:
                threeValues = True
        if twoValues and threeValues:
            return 25
        else:
            self.wrong_strategy()

    def check_street(number, self):
        if number <= len(set(Evaluator.dices)):
            if number == 4:
                print(set(sorted(Evaluator.dices)))
                if {1,2,3,4} == set(sorted(Evaluator.dices)) or {2,3,4,5} == set(sorted(Evaluator.dices)) or {3,4,5,6} == set(sorted(Evaluator.dices)):
                    return 30
            else:
                if {1,2,3,4,5} == set(sorted(Evaluator.dices)) or {2,3,4,5,6} == set(sorted(Evaluator.dices)):
                    return 40
            self.wrong_strategy()

    def check_yahtzee(self):
        if len(set(Evaluator.dices)) == 1:
            return 50
        else:
            self.wrong_strategy()

    def evaluate_strategy(self, strategy, player):
        self.player = player
        if strategy == "ones":
            points = Evaluator.count_number(1, self)
            player.UPPER_SECTION['ones'] = points
        elif strategy == "twos":
            points = Evaluator.count_number(2, self)
            player.UPPER_SECTION['twos'] = points
        elif strategy == "threes":
            points = Evaluator.count_number(3, self)
            player.UPPER_SECTION['threes'] = points
        elif strategy == "fours":
            points = Evaluator.count_number(4, self)
            player.UPPER_SECTION['fours'] = points
        elif strategy == "fives":
            points = Evaluator.count_number(5, self)
            player.UPPER_SECTION['fives'] = points
        elif strategy == "sixes":
            points = Evaluator.count_number(6, self)
            player.UPPER_SECTION['sixes'] = points
        elif strategy == "three_of_a_kind":
            points = Evaluator.count_kinds(3, self)
            player.LOWER_SECTION['three_of_a_kind'] = points
        elif strategy == "four_of_a_kind":
            points = Evaluator.count_kinds(4, self)
            player.LOWER_SECTION['four_of_a_kind'] = points
        elif strategy == "full_house":
            points = Evaluator.check_full_house(Evaluator)
            player.LOWER_SECTION['full_house'] = points
        elif strategy == "small_street":
            points = Evaluator.check_street(4, self)
            player.LOWER_SECTION['small_street'] = points
        elif strategy == "large_street":
            points = Evaluator.check_street(5, self)
            player.LOWER_SECTION['large_street'] = points
        elif strategy == "yahtzee":
            points = Evaluator.check_yahtzee(self)
            player.LOWER_SECTION['yahtzee'] = points
        elif strategy == "chance":
            player.LOWER_SECTION['chance'] = sum(Evaluator.dices)
        else:
            print("this is not a valid strategy choose from: \n")
            print(player.LOWER_SECTION.keys())
            print(player.UPPER_SECTION.keys())
            strategy = input("choose another strategy! \n")
            Evaluator.evaluate_strategy(self, strategy, player)








