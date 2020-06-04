from random import choice
def game():
    with open ('wordlist.txt', 'r') as f:
        wordlist = f.read().split('\n')

    word_of_the_game = choice(wordlist)


    word_len = len(word_of_the_game)
    blank_word=['_ ']*word_len
    print(''.join(blank_word))

    bad_letters=[]
    while True:
        if '_ ' not in blank_word:
            print(f"You won! The word was:  {''.join(blank_word)}")
            game()

        guess_letter = input('guess a letter        ')
        if guess_letter in word_of_the_game:
            print('Good!')
            for i in range(len(word_of_the_game)):
                if word_of_the_game[i] == guess_letter:
                    blank_word[i] = guess_letter
        else:
            bad_letters.append(' '+guess_letter+' ')
        print('your word:   '+''.join(blank_word))
        print('bad letters : '+''.join(bad_letters))

game()