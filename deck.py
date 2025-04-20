### chap15/deck.py
import kings

def main():
    ans = input('Do you want the deck shuffled? [yY] ')

    # Create the deck then possibly shuffle it
    if ans != '' and ans.strip() in 'yY':
        deck = kings.shuffle()
    else:
        deck = kings.shuffle(False)

    print('\nFull deck:')
    print(deck)

    print('\nDone!')

if __name__ == '__main__':
    main()
