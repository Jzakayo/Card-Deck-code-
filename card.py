#Justine Moturi
#purpose : card class file
#date: 19/10/2022

class Card:
    #creates adresses for the parameters
    def __init__(self, number, type):
        self.number = number
        self.type = type
        #assigns numbers
        if self.number in range(1,10):
            self.number = number
        elif self.number == 11:
            self.number =  "Jack"
        elif self.number == 12:
            self.number = "Queen"
        elif self.number == 13:
            self.number =  "King"

        # assign cards types
        if self.type == 1:
            self.type = "Clubs"
        elif self.type == 2:
            self.type = "Spades"
        elif self.type == 3:
            self.type = "Diamonds"
        elif self.type == 4:
            self.type = "Hearts"

        #Returns card type and number as a string

    def __str__ (self):
        to_print = str(self.number) + " of " + str(self.type)
        return to_print
