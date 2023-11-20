import random


def rng(max):
    random_number = random.randint(0, max - 1)
    return random_number


def initialize():
    deck = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A', '12A', '13A',
            '1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B', '10B', '11B', '12B', '13B',
            '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D']
    return deck


def remove(array, index):
    array.remove(index)
    return array


def play(deck,card):
    size = len(deck)
    rng_index = rng(size)
    current_card = deck[rng_index]
    if card == '':
        card = current_card
    else:
        highLow = input('The next card will be Higher / Lower than your card : (H/L)')
    print(f'Current card : {card}')
    if card != '':
        print(f'You draw : {current_card}')
    deck = remove(deck, current_card)
    return deck


if __name__ == '__main__':
    print('start')
    currentDeck = []
    choose = ''
    yourCard = ''
    while choose != 'N':
        choose = input("Do You want to play? (Y/N)")

        if choose == 'Y':
            if len(currentDeck) == 0:
                currentDeck = initialize()
                print(currentDeck)
            play(currentDeck, yourCard)
            print(currentDeck)
        elif choose == 'N':
            print('You have finished the game. Thank You!!')
        else:
            print('Please choose Y or N')
