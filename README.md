# Space-Shooter

Space-Shooter is a game where you have to shoot the enemy spaceships using lasers you can shoot. Can you destroy all the enemies with your laser before they reach you?

## Getting Started

Make sure you have Python 3.8.0 or newer and Pygame installed and running on your machine. You can install Pygame by opening a terminal and running the following command.
```
For Mac:
pip3 install pygame
For Windows:
pip install pygame
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 Space-Shooter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the Cycles folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Space-Shooter       (source code for game)
  +-- game              (specific game classes)
    +-- assets          (images for the game)
    +-- collide         (handles collisions)
    +-- enemy           (generates enemies)
    +-- laser           (creates lasers)
    +-- player          (player condition)
    +-- ship            (manages the player's shoots)
  +--constants          (constant values)
  +--main.py            (entry point for program)
+-- README.md           (general info)
```

## Required Technologies

* Python 3.8.0
* Pygame 2.1.2

## Rules

- The Player can move from left to right.
- The Player try to shoot so the opponent collides with their laser.
- If an enemy collides with your laser it dies.
- If you kill all the enemy spaceships...YOU WIN!

## Requirements

- The program must have a README file.
- The program may be any type of game or interactive simulation.
- The program should use classes and instances.
- The program should apply the four principles of programming with classes.
- The program should use the libraries chosen in the course.
- The program should be delivered through a version control system.
- The program should be able to be run from the command line.

<img width="995" alt="Screen Shot 2022-03-30 at 10 07 13 PM" src="https://user-images.githubusercontent.com/94416292/160975459-8a200c3b-c3ec-4302-b21d-325177b3bd77.png">
