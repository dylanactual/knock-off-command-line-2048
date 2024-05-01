import logic

mat = logic.start_game()
state = 0
print("Welcome to knock off 2084")
print("please input using standard wasd and the enter key to control the game")
print("---------------------------------------------")
logic.display(mat)

while state == 0:
    direction = input("Enter direction: ")
    if direction == 'w' or direction == "W":
        mat, state = logic.w(mat)
    elif direction == 'a' or direction == 'A':
        mat, state = logic.a(mat)
    elif direction == 's' or direction == 'S':
        mat, state = logic.s(mat)
    elif direction == 'd' or direction == 'D':
        mat, state = logic.d(mat)
    else: print("Bad input, please try again")
    logic.display(mat)
if state == 1: print("GAME OVER")
else: print("CONGRATULATIONS YOU WIN")
