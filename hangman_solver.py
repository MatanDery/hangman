from collections import Counter



def init_wordlist(word_len):
    with open ('wordlist.txt', 'r') as f:
        wordlist=f.readlines()
        match_wordlist=[]
        for word in wordlist:
            if len(word.rstrip()) == word_len:
                match_wordlist.append(word.rstrip())
        return match_wordlist

def calc_most_likely_letter(wordlist, solved_letters):
    wordlist = ''.join(wordlist)
    counts = Counter(wordlist)
    return counts.most_common()[len(solved_letters)][0]

def correct_letter_position(letter, blank_word):
    ocs = input(f'How Many Times "{letter}" Appears?')
    try:
        ocs = int(ocs)
    except ValueError:
        print('Enter a number Please')
        correct_letter_position(letter, blank_word)
    print(''.join(blank_word))
    for i in range(ocs):
        index  = input(f"Enter index of letter 1 - {len(blank_word)}")
        try:
            index = int(index)
        except ValueError:
            print('Enter a number Please')

        if index < 1 or index > len(blank_word) or blank_word[index-1] != '_ ':
            print('Ileagal!! please enter a leagal index!!!')
            print('retry')
            correct_letter_position(letter, blank_word)
        blank_word[index-1] = letter
        print(''.join(blank_word))
    return blank_word





def filter_not_letter(wordlist, letter):
    n_wordlist =[]
    for word in wordlist:
        if letter not in word:
            n_wordlist.append(word)
    return n_wordlist

def filter_yes_letter(wordlist, letter):
    n_wordlist =[]
    for word in wordlist:
        if letter in word:
            n_wordlist.append(word)
    return n_wordlist


def guessing(guess_letter):
    correct = input(f"My letter is '{guess_letter}' is it correct? y/n        ")
    if correct !='y' and correct != 'n':
        print('only enter y or n!')
        guessing(guess_letter)
    return correct == 'y'

def game():
    word_len = input("Enter length of word          ")
    try:
        word_len = int(word_len)
    except ValueError :
        print('Please Enter A Number!')
        game()

    blank_word=['_ ']*word_len
    print(''.join(blank_word))


    wordlist=init_wordlist(word_len)

    solved_letters=[]
    while True:
        if len(wordlist) == 1:
            print(f"Your Word Is:  {wordlist[0]}")
        if len(wordlist) == 0:
            print(f"Your Word Doesnt Exist!!!")

        guess_letter = calc_most_likely_letter(wordlist, solved_letters)
        correct = guessing(guess_letter)

        if correct:
            blank_word = correct_letter_position(guess_letter, blank_word)
            print(blank_word)
            solved_letters.append(guess_letter)
            wordlist = filter_yes_letter(wordlist, guess_letter)
        else:
            wordlist = filter_not_letter(wordlist, guess_letter)
















game()