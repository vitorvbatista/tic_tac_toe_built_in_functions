# Set two global variables. They'll change during this game
global first_player
global second_player
global base_matrix


class PlayingGame:  # Set class 'playing game'. It contains all functions that will be used

    def __init__(self) -> None:  # __init__ won't be used since we'll have functions calling each other
        pass

    @staticmethod
    def start_game():  # This function will start this game, showing the coordinates matrix and a welcome message
        global base_matrix

        base_matrix = [
            '0', '1', '2',
            '3', '4', '5',
            '6', '7', '8']

        matrix = [
            '-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']

        print('Welcome to Tic tac toe! Developed only with built-in functions\n'
              'This game is based on coordinates/positions like this: \n',
              base_matrix[:3],
              '\n',
              base_matrix[3:6],
              '\n', base_matrix[6:10], '\n',
              'So write your position in the console and defeat your opponent!', '\n',
              matrix[:3],
              '\n',
              matrix[3:6],
              '\n', matrix[6:10])

        return matrix

    @staticmethod
    def move(matrix, player):  # This function represents the movement made by the player
        global first_player
        first_player = player
        print(first_player)

        pos = input("What is your move? Write down you position (0 -> 8) \n")  # Position in matrix requested by user
        if pos.isdigit():
            pos = int(pos)
        else:
            print("This position is not valid! Please write down a correct position (0 -> 8) ")
            PlayingGame.move(matrix, first_player)  # If position has already been filled, return to function 'move'

        letter = input('Now, write down your letter (x or o) \n').upper()  # Letter X or O to fill matrix

        try:
            if int(pos) in range(0, 9):  # Check if position is an integer (serving as coordinate to fill matrix)
                pass
            else:
                print("Your position doesn't match what's needed")
                return PlayingGame.move(matrix, first_player)

        except ValueError:  # If position isn't integer, this code will return a message and go back to function 'move'
            print("Are you sure ", str(pos), "is a number?")
            PlayingGame.move(matrix, first_player)

        if "X" in letter or "O" in letter:
            # Check if letter correspond to X or O. If it doesn't, it'll go back to 'move'
            pass
        else:
            print("Your letter doesn't match what's needed, write down your letter (x or o)")
            return PlayingGame.move(matrix, first_player)

        movement_already_made = PlayingGame.check_movement(matrix, pos)
        # Check if movement was made
        # If it wasn't, it'll go back to function 'move'
        if movement_already_made:
            print("Position has already been filled!")
            return PlayingGame.move(matrix, first_player)
        else:
            # Checking if the game was a draw
            PlayingGame.draw(base_matrix)

            # If all parameters are correct, it'll go to 'write' function, to fill position with requested letter
            PlayingGame.write(matrix, letter=letter, pos=pos, player=player)

    @staticmethod
    def draw(temp_matrix):
        temp_matrix.pop(0)
        total_positions = len(temp_matrix)

        if total_positions == 0:
            print("There's a draw in this game!")
            exit()
        else:
            return temp_matrix

    @staticmethod
    def write(matrix, letter, pos, player):  # Write movement inside matrix
        matrix[pos] = letter

        print(matrix[:3],
              '\n',
              matrix[3:6],
              '\n', matrix[6:10])

        winner = PlayingGame.check_winner(matrix)  # First,through function 'check_winner' we'll check possible winner

        if winner:
            print('Congratulations', player, 'you won this game!')
            exit()
        else:
            # If this code can't find a winner it will turn player and next it'll go back to function 'move' to continue
            changed_player = PlayingGame.change_player()
            PlayingGame.move(matrix, changed_player)

    @staticmethod
    def check_movement(matrix, position):
        # Check if position was already filled and return a flag
        if matrix[position] == '-':
            result = False
        else:
            result = True
        return result

    @staticmethod
    def check_winner(matrix):
        # Check possible winner
        # Since we're working with matrix, we have to manipulate all coordinates through lists and analyse all of them
        # All 'if' and 'elif' blocks will verify different conditions to confirm winner. If positive it'll result True
        first_column = [matrix[0], matrix[3], matrix[6]]
        second_column = [matrix[1], matrix[4], matrix[7]]
        third_column = [matrix[2], matrix[5], matrix[8]]
        first_diagonal = [matrix[0], matrix[4], matrix[8]]
        second_diagonal = [matrix[3], matrix[5], matrix[7]]

        # analysing first line
        if matrix[0] == matrix[1] == matrix[2] and matrix[:3] != ['-', '-', '-']:
            result = True

        # analysing second line
        elif matrix[3] == matrix[4] == matrix[5] and matrix[3:6] != ['-', '-', '-']:
            result = True

        # analysing third line
        elif matrix[6] == matrix[7] == matrix[8] and matrix[6:10] != ['-', '-', '-']:
            result = True

        # analysing first column
        elif matrix[0] == matrix[3] == matrix[6] and first_column != ['-', '-', '-']:
            result = True

        # analysing second column
        elif matrix[1] == matrix[4] == matrix[7] and second_column != ['-', '-', '-']:
            result = True

        # analysing third column
        elif matrix[2] == matrix[5] == matrix[8] and third_column != ['-', '-', '-']:
            result = True

        # analysing first_diagonal
        elif matrix[0] == matrix[4] == matrix[8] and first_diagonal != ['-', '-', '-']:
            result = True

        # analysing second_diagonal
        elif matrix[3] == matrix[5] == matrix[7] and second_diagonal != ['-', '-', '-']:
            result = True

        else:
            result = False
        return result

    @staticmethod
    def change_player():
        # Intends to turn players after a movement
        global first_player
        global second_player

        temp = first_player
        first_player = second_player
        second_player = temp

        return first_player


if __name__ == "__main__":
    initial_matrix = PlayingGame.start_game()

    first_player = input("Who's gonna be player one (X) ?")
    second_player = input("Who's gonna be player two (O) ?")

    PlayingGame.move(initial_matrix, first_player)
