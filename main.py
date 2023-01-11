import time
from tkinter import *
from random import randint

MAX_HAND_VALUE = 21

gui = Tk()
cards = ["d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "djack", "dqueen", "dking", "dace", "h2", "h3", "h4",
         "h5", "h6", "h7", "h8", "h9", "h10", "hjack", "hqueen", "hking", "hace", "c2", "c3", "c4", "c5", "c6", "c7",
         "c8", "c9", "c10", "cjack", "cqueen", "cking", "cace", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10",
         "sjack", "squeen", "sking", "sace"]


class Player:
    def __init__(self, isDealer):
        self.hand = []
        self.isDealer = isDealer
        self.total = 0
        self.bust = False

    def drawRandomCard(self):
        global drawn_cards

        if len(drawn_cards) == 52:
            drawn_cards = []

        card = cards[randint(0, 51)]

        while card in drawn_cards:
            card = cards[randint(0, 51)]

        self.hand.append(card)
        drawn_cards.append(card)

        self.increment_points()

    def increment_points(self):
        if len(self.hand[-1][1:]) == 1:
            self.total += int(self.hand[-1][1:])
        elif len(self.hand[-1][1:]) == 3:  # Calculate ace value
            if self.total + 11 > MAX_HAND_VALUE:
                self.total += 1
            else:
                self.total += 11
        else:
            self.total += 10

        if self.total > MAX_HAND_VALUE:
            self.bust = True

    def get_suit(self, index):
        card = self.hand[index]

        if card[0] == "d":
            return "diamonds"
        elif card[0] == "h":
            return "hearts"
        elif card[0] == "c":
            return "clubs"
        else:
            return "spades"

    def describeDrawnCard(self):
        suit = self.get_suit(-1)

        if not self.isDealer:
            print("you have picked up a " + self.hand[-1][1:] + " of " + suit)
        else:
            if len(self.hand) == 1:
                print("the dealer picked up a " + self.hand[-1][1:] + " of " + suit)
            else:
                print("the dealer picked up a card")
                time.sleep(1)

    def describeHand(self):
        for i, card in enumerate(self.hand):
            suit = self.get_suit(i)
            print("the dealer had a " + dealer.hand[i][1:] + " of " + suit)
            time.sleep(1)

    def reset(self):
        self.__init__(self.isDealer)


player = Player(False)
dealer = Player(True)

drawn_cards = []
points = 0
hand_length = 0
counter = 0


def hit():
    player.drawRandomCard()
    player.describeDrawnCard()

    if player.bust:
        print("you've gone bust")
        dealer.describeHand(False)


def dealer_playing():
    if len(dealer.hand) == 2 and dealer.total == MAX_HAND_VALUE:  # If dealer has blackjack
        print("the dealer has a blackjack")
    while dealer.total < 17 and not dealer.bust:
        dealer.drawRandomCard()
        dealer.describeDrawnCard()


def stand():
    dealer_playing()

    dealer.describeHand()
    if player.total > dealer.total or dealer.bust:
        print("you beat the dealer")
    else:
        print("the dealer beat you whith a " + str(dealer.total))

    for _ in range(3):
        print()


# butons
button1 = Button(gui, text="hit", height=3, width=4, bg='green', command=lambda: hit())
button1.grid(column=0, row=0)
button2 = Button(gui, text="stand", height=3, width=4, bg='green', command=lambda: stand())
button2.grid(column=1, row=0)
button3 = Button(gui, text="double down", height=3, width=10, bg='green')
button3.grid(column=2, row=0)
button4 = Button(gui, text="surrender", height=3, width=7, bg='green')
button4.grid(column=3, row=0)
button5 = Button(gui, text="new game", height=3, width=7, bg='green', command=lambda: initialiseGame())
button5.grid(column=4, row=0)


def initialiseGame():
    player.reset()
    dealer.reset()

    for i in range(2):  # Initialise game
        player.drawRandomCard()
        dealer.drawRandomCard()

        player.describeDrawnCard()
        dealer.describeDrawnCard()


initialiseGame()

gui.mainloop()
