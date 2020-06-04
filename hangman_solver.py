from collections import Counter



def init_wordlist(word_len):
    with open ('wordlist.txt', 'r') as f:
        wordlist=f.readlines()
        match_wordlist=[]
        for word in wordlist:
            if len(word.rstrip()) == word_len:
                match_wordlist.append(word.rstrip())
        return match_wordlist

# def calc_most_likely_letter(wordlist, solved_letters):   simple calc
#     wordlist = ''.join(wordlist)
#     counts = Counter(wordlist)
#     return counts.most_common()[len(solved_letters)][0]

def calc_most_likely_letter(wordlist, blank_word, solved_letters):
    tmp_wordlist=''
    for i in range(len(blank_word)):
        if blank_word[i] == '_ ':
            for word in wordlist:
                tmp_wordlist += word[i]
    counts = Counter(tmp_wordlist)
    for i in range(len(solved_letters)+1):
        if counts.most_common()[i][0] not in solved_letters:
            return counts.most_common()[i][0]


def num_of_repeats(letter, blank_word):
    ocs = input(f'How Many Times "{letter}" Appears?    ')
    try:
        ocs = int(ocs)
    except ValueError:
        print('Enter a number Please')
        ocs = num_of_repeats(letter, blank_word)
    if ocs > blank_word.count("_ "):
        print('Impossible try again')
        ocs = num_of_repeats(letter, blank_word)
    return ocs

def index_of_correct_letter(blank_word):
    index = input(f"Enter index of letter 1 - {len(blank_word)}    ")
    try:
        index = int(index)
    except ValueError:
        print('Enter a number Please')
        index = index_of_correct_letter(blank_word)

    if index < 1 or index > len(blank_word) or blank_word[index - 1] != '_ ':
        print('Ileagal!! please enter a leagal index!!!')
        print('retry')
        index = index_of_correct_letter(blank_word)
    return index


def correct_letter_position(letter, blank_word):
    ocs = num_of_repeats(letter, blank_word)
    print(''.join(blank_word))
    for i in range(ocs):
        index = index_of_correct_letter(blank_word)

        blank_word[index-1] = letter
        print(''.join(blank_word))
    return blank_word


def filter_not_letter(wordlist, letter):
    n_wordlist =[]
    for word in wordlist:
        if letter not in word:
            n_wordlist.append(word)
    return n_wordlist

def filter_yes_letter(wordlist, blank_word, guess_letter):
    n_wordlist =[]
    for i in range(len(blank_word)):
        if blank_word[i] == guess_letter:
            for word in wordlist:
                if word[i] == guess_letter:
                    n_wordlist.append(word)
    return n_wordlist


def guessing(guess_letter):
    correct = input(f"My letter is '{guess_letter}' is it correct? y/n        ")
    if correct !='y' and correct != 'n':
        print('only enter y or n!')
        correct = guessing(guess_letter)
    return (correct == 'y' or correct == True)

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
        if '_ ' not in  blank_word:
            print(f"Your Word Is:  {''.join(blank_word)}")
            game()

        if len(wordlist) == 0:
            print(f"Your Word Doesnt Exist!!!")

        guess_letter = calc_most_likely_letter(wordlist, blank_word,solved_letters)
        correct = guessing(guess_letter)

        if correct:
            blank_word = correct_letter_position(guess_letter, blank_word)
            print(''.join(blank_word))
            solved_letters.append(guess_letter)
            wordlist = filter_yes_letter(wordlist, blank_word , guess_letter)
        else:
            wordlist = filter_not_letter(wordlist, guess_letter)

game()