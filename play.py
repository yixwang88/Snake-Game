"""
This is the main program for the snake game.
"""

import time
from gui import Gui
from room import Room
from snake import Snake
from apple import Apple
from position import Position

def collides(p, positions):
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False

def hit_extra_wall(position, extra_wall_list):
    result = collides(position, extra_wall_list)
    return result

def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()
        extra_wall_list = [Position(gui.get_width() // 3, gui.get_height() // 3),
            Position(gui.get_width() // 3, gui.get_height() // 3 +1),
            Position(gui.get_width() // 3, gui.get_height() // 3 +2),
            Position(gui.get_width() // 3, gui.get_height() // 3 +3),
            Position(gui.get_width() // 3, gui.get_height() // 3 +4),
            Position(gui.get_width() // 3, gui.get_height() // 3 +5),
            Position(gui.get_width() // 3, gui.get_height() // 3 +6),
            Position(gui.get_width() // 3, gui.get_height() // 3 +7)
        ]


        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "CYAN")
        snake = Snake(gui.get_width() // 2, gui.get_height() // 2)
        apple = Apple(gui, snake.position)
        score = 0
        ti = 1
        apple2 = None


        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        while continuePlaying:

            # Get a key press from the user
            c = gui.get_keypress()
            # Do something with the key press
            if c == 'q':
                break
            #     do something if the user wants to quit
            elif c == "KEY_UP":
                snake.change_direction("KEY_UP")
            #   do something depending on what was pressed,
            #     e.g. you may want to change the direction of the snake
            elif c == "KEY_DOWN":
                snake.change_direction("KEY_DOWN")

            elif c == "KEY_LEFT":
                snake.change_direction("KEY_LEFT")

            elif c == "KEY_RIGHT":
                snake.change_direction("KEY_RIGHT")
            #     do something else

            # Add your code to move the snake
            # around the screen here.
            snake.move()

            # The redraw part of the game. First clear the screen
            gui.clear()

            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui,score)
            apple.draw(gui)
            if apple2 != None:
                apple2.draw(gui)
            snake.draw(gui)
            gui.draw_text("贪吃蛇 Your Score is: " + str(score), ((gui.get_width())//2)-10, 1, "BLACK", "WHITE")

            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here
            #吃苹果 eating apple
            if apple.hit_snake(gui, snake.position) == True:
                score += 10
                apple = Apple(gui, snake.position)
                snake.grow()
                ti -= 0.1
                if ti < 0.1:
                    ti = 0.1


            #extra apple
            if score >= 60 and apple2 == None:
                apple2 = Apple(gui, snake.position)

            if apple2 != None and apple2.hit_snake(gui, snake.position) == True:
                score += 10
                apple2 = Apple(gui, snake.position)
                snake.grow()
                ti -= 0.1
                if ti < 0.1:
                    ti = 0.1

            #撞墙 hit wall
            if snake.position[0].get_x() == (gui.get_width())-1 or snake.position[0].get_x() == 0:
                break
            elif snake.position[0].get_y() == (gui.get_height())-1 or snake.position[0].get_y() == 0:
                break

            extra_wall = False
            if score >=50:
                if hit_extra_wall(snake.position[0], extra_wall_list) == True:
                    extra_wall = True
            if extra_wall == True:
                break

            #撞尾巴 hit body
            tail_hit = False
            for i in range(1,len(snake.position)):
                if snake.position[0].get_x() == snake.position[i].get_x() and snake.position[0].get_y() == snake.position[i].get_y():
                    tail_hit = True
            if tail_hit == True:
                break

            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(ti)


    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e

    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    gui.quit()
    print("Your score is: " + str(score))

    # The game has ended since we broke out of the main loop
    # Display the user's score here


if __name__ == "__main__":
    main()
