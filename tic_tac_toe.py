#!/usr/bin/env python
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
#
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
#
#     player1 = input("Please pick a marker 'X' or 'O'")
#
# Note that input() takes in a string. If you need an integer value, use
#
#     position = int(input('Please enter a number'))
#
# <br>To clear the screen between moves:
#
#     from IPython.display import clear_output
#     clear_output()
#
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
#
#     print('\n'*100)
#
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**



test_board = ['#','1','2','3','4','5','6','7','8','9']
list_dplayers = [{'player':'1','marker':'$','turn':'n'},{'player':'2','marker':'$','turn':'n'}] #list of dictionaries of players
glb_play_mark = ['','','']
iplayer =''

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    print(' ',board[1], '|', board[2],'|', board[3])
    print('____________')
    print(' ',board[4], '|', board[5],'|', board[6])
    print('____________')
    print(' ',board[7], '|', board[8],'|', board[9])
    pass


# In[ ]:


#display_board(test_board)


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[ ]:


def player_input():
    if glb_play_mark[2] != 'Game Over':
        try:
            #display_board(test_board)
            pl_input = int(input(f'Player {glb_play_mark[0]} Enter a number between 1 and 9 to place your {glb_play_mark[1]}: '))
            while pl_input > 9 or pl_input < 0:
                print('\nTry again')
                pl_input = int(input('\nEnter a number between 1 and 9 : '))
            return pl_input
            print(pl_input)
        except:
            print('\nDid not enter a number')
            player_input()
    else:
        return False


# In[ ]:


#player_input()


# **TEST Step 2:** run the function to make sure it returns the desired output

# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker
    #print(board[position])
    #display_board(board)
    test_board = board
    return test_board
    pass


# In[ ]:


#place_marker(test_board,'X',2)


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[ ]:


def win_check(play, mark):
    win_combo = ['123','147','159','456','789','258','369','357']
    #print(board[::]
    board = test_board
    sChk = []
    i = -1
    for xo in board:
        i += 1
        if xo == mark:
            sChk.append(str(i))

    #print(sChk)

    #for n in test_board:
     #   print(f'{test_board.index(n)}  and {n}')
    j = 0
    for n in win_combo:
        #print(f'This is win combo: {n}')
        if j == 3:
            break
        j = 0
        for m in sChk:
            #print(f'This is each char in sChk: {m}')
            if m in n:
                j += 1
                #print(f'This is count of matching char in win combo: {j}')
    #print(f'This is final count of matching char in win combo: {j}')

    if j == 3:
        glb_play_mark[2] = 'Game Over'
        print(f'Player {play} has won. The {mark}{mark}s wins')
        return True
    else:
        return False


# In[ ]:


#test_board = ['#','X','X','X','4','5','6','7','8','9']
#win_check(1,'O')


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[ ]:


import random
def choose_first():
    x = random.randint(1,2)
    print(f'Player {x} is going first, would you like to be X or O')
    pmark = input(f'Please enter X or O: ').lower()
    while pmark != 'x' and pmark != 'o':
        pmark = input(f'Please enter X or O: ').lower()

    y = 0
    for n in list_dplayers:
        if n['player'] == str(x):
            list_dplayers[y]['marker'] = pmark.upper()
            list_dplayers[y]['turn'] = 'Y'
        else:
            list_dplayers[y]['turn'] = 'N'
            if pmark == 'x':
                list_dplayers[y]['marker'] = 'O'
            else:
                list_dplayers[y]['marker'] = 'X'
        y += 1
    #current_player[1] = pmark.upper()
    glb_play_mark[0] = str(x)
    glb_play_mark[1] = pmark
    #print(list_dplayers)
    #return 123
    #return random.randint(1,2)
    #print(x)



# In[ ]:


#choose_first()


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[ ]:


def space_filled(board, position):
    #return True if position is filled with either X or O
    if board[position] == 'X' or board[position] == 'O':
        return True
    else:
        return False


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[ ]:


def full_board(board):
    x = 0
    y = 0
    while x < len(board)-1:
        x += 1
        if space_filled(board, x) == True:
            y += 1
    #print(f'board spaces count: {y}')
    if y == 9:
        glb_play_mark[2] = 'Full Board'
        print('The board is full.')
        return True
    else:
        return False


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[ ]:


def player_choice(board, player, iplayer):
    if full_board(test_board) == False:
        #print(player)
        marker = ''
        for n in player:
            if n['turn'] == 'Y':
                marker = n['marker']
                iplayer = n['player']

        for m in list_dplayers:
            m['turn'] = 'N'
            if m['player'] != iplayer:
                #print(iplayer)
                #print(m['player'])
                m['turn'] = 'Y'

        #print(glb_play_mark)

        glb_play_mark[0] = iplayer
        glb_play_mark[1] = marker

        #print(glb_play_mark)

        pl_input = player_input()
        if space_filled(board, pl_input) == False:
            #print(player[0])

            place_marker(board, marker, pl_input)
            #print(iplayer, '  ', marker)
            if win_check(iplayer, marker) == True:

                return True
        else:
            print(f'Position entered is already filled \nTry again')

            for n in player:
                if n['turn'] == 'Y':
                    marker = n['marker']
                    iplayer = n['player']

            for m in list_dplayers:
                m['turn'] = 'N'
                if m['player'] != iplayer:
                    #print(iplayer)
                    #print(m['player'])
                    m['turn'] = 'Y'

            #print(glb_play_mark)

            glb_play_mark[0] = iplayer
            glb_play_mark[1] = marker

            #print(glb_play_mark)

# In[ ]:

#player_choice(test_board, list_dplayers)

# In[ ]:


def reset_game():
    x = 1
    while x < len(test_board):
        test_board[x] = str(x)
        x += 1
    x = 0
    while x < len(list_dplayers):
        list_dplayers[x]['marker'] = '$'
        list_dplayers[x]['turn'] = 'n'
        x += 1
    x = 0
    while x < len(glb_play_mark):
        glb_play_mark[x] = ''
        x += 1
    iplayer = ''

    return True


# In[ ]:


#reset_game()

# In[ ]:

def main_game():

    while glb_play_mark[2] != 'Game Over' and glb_play_mark[2] != 'Full Board':
        if full_board(test_board) == True:
            break
        #print(glb_play_mark)
        player_choice(test_board, list_dplayers, iplayer)
        display_board(test_board)
    result = input('Would you like to play again? Enter y or n: ')
    result = result.lower()
    if result == 'y':
        reset_game()
        choose_first()

        display_board(test_board)
        #print(list_dplayers)
        #print(glb_play_mark)

        main_game()
    else:
        print('Thank You for Playing')


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**
print('Welcome to Tic Tac Toe!')

choose_first()
main_game()
