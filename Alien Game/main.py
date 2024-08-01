import time

from turtle import *
from ship import Ship
from bullet import Bullet
from alien import Alien


# Game variables
game_state = True


# Screen setup
screen = Screen()
screen.title("Alien Invader")
screen.bgcolor("Black")
screen.setup(800, 600)
screen.tracer(0)

# Initialize the ship
ship = Ship()

# List to store bullets
bullets = []
def shoot_bullet():
    """Function to draw bullet to screen"""
    if len(bullets) < 3:
        bullet = Bullet(ship)
        bullets.append(bullet)

def end_game():
    end = Turtle()
    end.hideturtle()
    end.penup()
    end.color("white")
    end.write("Game Over", align="center", font=("Arial", 42,))


# List to store aliens
aliens = []
# Create row of aliens
for x in range(-360, 360, 50):
    alien = Alien(x, 280)
    # alien2 = Alien(x, 250)
    aliens.append(alien)
    # aliens.append(alien2)

# Bind and listen for keys to move ship
screen.onkeypress(ship.move_left, "Left")
screen.onkeypress(ship.move_right, "Right")
screen.onkeypress(shoot_bullet, "space")
screen.listen()

while game_state:
    if len(aliens) == 0:
        end_game()
        
        
        # # game_state = False
        screen.update()
        print(bullets)
        break
    screen.update()
    time.sleep(.05)
    

    # Move aliens
    for alien in aliens:
        alien.move_alien()
    # Detect if aliens are at end of screen to move them down
    if aliens[-1].xcor() > 360:
        for alien in aliens:
            alien.change_dir()
    elif aliens[0].xcor() < -370:
        for alien in aliens:
            alien.change_dir()
            
    for bullet in bullets:
        # Move each bullet
        bullet.move_bullet()
        # Detect collision with bullet and alien
        for alien in aliens:
            if bullet.distance(alien) < 30:
                bullet.remove_bullet(bullets)
                alien.remove_alien(aliens)
        # Detect if bullet moves off screen
        if bullet.ycor() > 300:
            bullet.remove_bullet(bullets)

    # Stop the ship from going out of bounds
    if ship.xcor() > 360:
        ship.move_left()
    elif ship.xcor() < -370:
        ship.move_right()


for bullet in bullets:
            bullet.remove_bullet(bullets)
screen.update()


screen.exitonclick()