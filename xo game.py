check = True


def print_bord(bord):
    print(bord['7'] + '|' + bord['8'] + '|' + bord['9'])
    print('+-+-')
    print(bord['4'] + '|' + bord['5'] + '|' + bord['6'])
    print('+-+-')
    print(bord['1'] + '|' + bord['2'] + '|' + bord['3'])


def main():
    theBord = {
        '7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '
    }
    turn = 'x'
    count = 0

    for _ in range(10):
        print_bord(theBord)
        print(f'the turn with : {turn}\n')
        move = input('where you need to play :  ')
        if move not in theBord.keys():
            print('pleas inter number only form 1 to 9 . ...')
            continue

        if theBord[move] == ' ':
            theBord[move] = turn
            count += 1
        else:
            print('the place you inter is filled.\n Mov To witch Place')
            continue
        if count >= 5:  # check if player win
            if theBord['7'] == theBord['8'] == theBord['9'] != ' ' \
                    or theBord['4'] == theBord['5'] == theBord['6'] != ' ' \
                    or theBord['4'] == theBord['5'] == theBord['6'] != ' ' \
                    or theBord['1'] == theBord['2'] == theBord['3'] != ' ' \
                    or theBord['7'] == theBord['4'] == theBord['1'] != ' ' \
                    or theBord['8'] == theBord['5'] == theBord['2'] != ' ' \
                    or theBord['9'] == theBord['6'] == theBord['3'] != ' ' \
                    or theBord['9'] == theBord['5'] == theBord['1'] != ' ' \
                    or theBord['7'] == theBord['5'] == theBord['3'] != ' ':
                print_bord(theBord)
                print(f"Game over the winner is {turn}")
                break
        # if player do all moves and no one win
        if count == 9:
            print("\nGAme Over.\n ")
        # When the first user do his move then we need to change
        # the value of "turn" variable to the other player
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'


if __name__ == '__main__':
    while True:
        main()
        inp = input('if you need to play agine inter y if you need to exit press eny key :> ')
        if inp == 'y':
            continue
        else:
            break
