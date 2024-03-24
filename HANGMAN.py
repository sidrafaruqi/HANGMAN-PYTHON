available_words=open('words.txt')
word=available_words.read()
words_=word.split()

import random
random_word=random.choice(words_)


import time
word_len=len(random_word)


letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def game():
    s=[] #for same letters
    guesses = 6  # for guesses
    warnings = 3  # for warnings
    total=0  # for score
    highscore=0  # for highest score
    print()
    print('               (๑¯◡¯๑)→  HANGMAN! ⟵(๑¯◡¯๑) ')
    print('            ======================================')
    name = input('ENTER YOUR NAME: ')
    print('HI!', name, 'I am thinking of a word that is', word_len, 'letters long ;)')
    print('YOU HAVE',warnings,'WARNINGS !!! ┏(＾0＾)┛')
    print('____________')
    print()
    print('Available letters: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    time.sleep(1) #for a better sequential printing
    guessing= ['_ ' for i in range(word_len)]
     # for guesses to be filled in
    

    while True:
        print(''.join(guessing))
        print('YOUR GUEESES: ', guesses)
        guess_ = input('GUESS A LETTER: ')
        guess_=guess_.lower()
        print()
        time.sleep(1)

        if len(guess_)>1:  # if user enter more than 1 letter
            print('Enter only (ノ^_^)ノ  ONE letter! ')
            print('-----------------------------')
        elif guess_ in s:  # s is the empty list,where letters entered will be stored to check the repeated letters entered
            if warnings==0:
                guesses-=1
                print('You have 0 WARNINGS left so u loose 1 GUESS .·´¯`(>▂<)´¯`·.')
            else:
                warnings-=1
                print('You have ALREADY ENTERED this letter (ಠ_ಠ)')
                print('------------------------------------')
                print('You have', warnings, 'warnings left!')

        elif guess_ in random_word:
            print('GOOD GUESS!')
            print('============')
            print()
            for i in range(len(random_word)):
                if guess_ == random_word[i]:  # if the guess entered is in the random_word
                    guessing[i] = guess_  # index of the guess in random_word
                print(guessing[i],end='')  # it is to print the list in which guess of correct word is being entered in the form of a string
            print()

        elif guess_ not in random_word:
            if guess_ in 'aeiou':
                guesses -= 2
                print('OOPSIE!',guess_,'is not in the word .·´¯`(>▂<)´¯`·. ')
                print('. . . . . . . . . . . . . . . . . . . . . . . . . . . .')
            elif not guess_.isalpha() : #if the input is any other entree than an alphabet
                if warnings == 0:
                    guesses -= 1
                    print('You have 0 WARNINGS left so u loose 1 GUESS ¯\(◉‿◉)/¯')
                    print('-------------------------------------------')
                else:
                    warnings -= 1
                    print('Enter a (ノ^_^)ノ  VALID letter')
                    print('You have', warnings, 'warnings left')
                    print('. . . . . . . . . . . . . . . . . . . . ')
            else:
                guesses -= 1
                print("OOPSIE! that's a WRONG letter .·´¯`(ಥ╭╮ಥ)´¯`·.")
                print('-----------------------------')
                time.sleep(0.5)
                print()
        s.append(guess_)

        if guesses == 1: #for the printing of the man
            print('''
             +━━━━━━━━━+
             |         |
             |      (˘･_･˘)
             |     ¯¯¯\|/¯¯¯      
             |         |
             |        /|
             |       /   
             |
             **** 
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)
        if guesses == 2:
            print('''
             +━━━━━━━━━+
             |         |
             |      (˘･_･˘)
             |     ¯¯¯\|/¯¯¯      
             |         |
             |         |
             |       
             |
             ****
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)
        if guesses == 3:
            print('''
             +━━━━━━━━━+
             |         |
             |      (˘･_･˘)
             |     ¯¯¯\|      
             |         |
             |         |
             |       
             |
             **** 
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)
        if guesses == 4:
            print('''
             +━━━━━━━━━+
             |         |
             |      (˘･_･˘)
             |         |     
             |         |
             |         |
             |       
             |
             ****
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)
        if guesses == 5:
            print('''
             +━━━━━━━━━+
             |         |
             |      (˘･_･˘)
             |           
             |         
             |         
             |       
             |
             ****
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)
        if guesses == 6: #for the printing of the man
            print('''
             +━━━━━━━━━+
             |         |
             |      
             |           
             |         
             |         
             |       
             |
             ****
             ━━━━━━━━━━━━''')
            print()
            time.sleep(0.5)


        if '_ ' not in guessing:
            print()
            print('♪┌|∵|┘♪ CONGRATULATIONS AND CELEBRATION!!! ♪└|∵|┐♪')
            print('-------------------------')
            time.sleep(0.5)

            count = set() #to save the unique letters only
            for b in random_word:
                count.add(b)
            ul = (len(count))
            total=guesses * ul

            with open('high_score.txt', 'r') as hs:
                hs_file = hs.read()
                if hs_file.count("=")>0:
                    file_split=hs_file.split("=")
                    highscore=int(file_split[1]) #index:1 stores the high score

            if total>highscore:
                print('Yay new High Score! Total: ', total)
                print(':::::::::::::::::::::::::::::::::::::::')
                with open('high_score.txt', 'w') as hs:
                    hs.write(name + '=' + str(total))
                break
            else:
                print('DEAR', name.upper(), 'YOUR TOTAL SCORE IS', total)
                print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
                break


        if guesses <= 0:
            print('Ran out of guesses. YOU LOSE! (╯°□°）╯︵┻━┻')
            print('***********')
            print('The correct word was (｡◕‿◕｡)━☞', random_word.upper() )
            print('''
                +━━━━━━━━━+
                |         |
                |      (˘･_･˘)
                |     ¯¯¯\|/¯¯¯      
                |         |
                |        /|\\ 
                |       /   \\
                |
                ****
                ━━━━━━━━━━━━''')
            print()
            a = input('IF YOU WANT TO PLAY AGAIN PRESS 1 OR PRESS ANY OTHER KEY: ') #allows the user to play again if he loses
            if a == '1':
                game()
            else:
                break



        elif guess_ in letter:
            letter.remove(guess_)
            time.sleep(0.5)
            print('Available letters: ', end='')
            for i in range(0, len(letter)):
                print(letter[i].upper(), end=' ') #print available letters as a string
            print()
            print('________________')

    available_words.close()

def start():
    print('                  WELCOME TO HANGMAN!')
    print('                 ====================')
    time.sleep(1)
    p = input(
        'FOR PLAYING THE GAME PRESS 1:\n==============================\nTO ACCESS THE ADMINISTRATIVE INTERFACE PRESS 2:\n===============================================\n')
    if p =='1':
            game()

    if p=='2':
        def administrator():
            print(' WELCOME TO THE ADMINISTRATIVE INTERFACE!')
            print('==========================================')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            print('*********')

            def choice():
                with open('me.txt') as admin:
                    admin = admin.read()
                    admin = admin.split()
                    if username == admin[0] and password == admin[1]: #checks for the admin and password from the file
                        print('''What do you want to do?
                         1) Add a new word to the game 
                         2) Reset the highscore
                         3) Return back to play the game
                         4) Any key to exit or stop''')
                        a = input('Select your option: ')
                        print('===================')
                        if a == '1':
                            word = input('enter your word: ')
                            word = " " + word
                            word = word.lower() #coverts the word into lowercase letters
                            f = open('words.txt', 'a')
                            f.write(word)
                            f.close()
                            print('YOUR WORD HAS BEEN ADDED TO THE LIST :D')
                            print('=========================================')
                            choice()
                        elif a == '2':
                            with open('high_score.txt', 'w') as reset:
                                print('Your highscore has been reset!')
                                choice()

                        elif a == '3':
                            game()

                        else:
                            print('STOPPING THE APPLICATION.')

                    else:
                        print("You have entered a wrong USERNAME or PASSWORD.")
                        time.sleep(2)

            choice ()

        administrator()

start()
