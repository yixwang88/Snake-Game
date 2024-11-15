# 🐍 Snake Game Project

## 🎮 Features

The project is a rendition of the classic Snake game, a beloved video game that has entertained gamers for many years. In this game, the player maneuvers a snake with the arrow keys. The objective is to guide the snake to eat apples that appear at random locations on the screen. Each time the snake eats an apple, it grows in length. The game ends when the snake's head collides with the border of the screen or with its own body.

This project utilizes various programming skills, including:
- Reading and understanding code
- Working with conditionals, lists, loops, and functions
- Managing code across multiple files
- Implementing objects and classes

## 🎮 What It Should Look Like

The game uses text graphics to render the screen:
- Walls of the room are represented by '#'
- The snake is represented by '+' and an arrow ('>' for right, '<' for left, '^' for up, 'v' for down) for the head
- The apple is represented by a red and green asterisk '*'

## 🧑‍💻 Components and Files

### 1. gui.py
This file provides a simplified interface for text graphics using the `ncurses` library. It includes methods for:
- Getting key presses
- Retrieving screen dimensions
- Drawing characters and lines on the screen
- Logging output for debugging

### 2. play.py
This is the main program file that controls the overall game loop. It initializes the GUI, creates game objects, and handles user inputs. It also manages the drawing and refreshing of the screen.

**Features Implemented:**
- Detect user key presses and quit the game when 'q' is pressed.
- Ensure the game enters an infinite loop waiting for user input and updates the game state accordingly.
- Clear the screen, draw the game objects, and refresh the screen at each iteration.
- Suspend execution to control the game speed.

### 3. snake.py
This file implements the Snake class. The snake is represented as a list of positions with the head at index 0. It includes methods for drawing the snake, moving it, changing its direction, and growing its length.

**Features Implemented:**
- Draw the snake on the screen with the head and tail represented by different characters.
- Move the snake one step at a time in the current direction.
- Change the snake's direction based on user input (arrow keys).
- Prevent the snake from doubling back on itself.
- Grow the snake's length when it eats an apple.

### 4. apple.py
This file implements the Apple class. The apple appears at random positions on the screen. The class ensures that the apple does not overlap with the snake or the borders.

**Features Implemented:**
- Generate apples at random positions on the screen.
- Ensure the apple does not appear on top of the borders or the snake.
- Detect when the snake's head collides with the apple, increase the score, and relocate the apple.

### 5. room.py
This file implements the Room class, including the borders around the screen. It ensures that all four walls of the room are drawn.

**Features Implemented:**
- Draw all four walls of the room on the screen.
- Size of the four walls are dynamically changed by the size of the terminal.

### 6. position.py
This class represents an (x, y) position on the screen. It includes methods to determine if a position collides with other positions.

**Features Implemented:**
- Represent positions on the screen.
- Determine if positions collide with other objects.

