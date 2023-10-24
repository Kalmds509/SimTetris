import os
import time
import random

# Largeur de la console
CONSOLE_WIDTH = 20
CONSOLE_HEIGHT = 20

# Fonction pour afficher l'obstacle
def draw_obstacle(x, y):
    os.system('clear' if os.name == 'posix' else 'cls')

    for row in range(y):
        print('|' + ' ' * (CONSOLE_WIDTH - 2) + '|')

    obstacle_row = ' ' * x + '##' + ' ' * (CONSOLE_WIDTH - x - 2)
    print(obstacle_row)
    print(obstacle_row)
    print(obstacle_row)
    print(obstacle_row)

    for row in range(y, CONSOLE_HEIGHT - 1):
        print('|' + ' ' * (CONSOLE_WIDTH - 2) + '|')

# Fonction principale du jeu
def main():
    x = random.randint(0, CONSOLE_WIDTH - 2)  # Position horizontale aléatoire
    y = 0  # Position verticale initiale

    while True:
        draw_obstacle(x, y)
        
        time.sleep(0.33)  # Délai de 1/3 de seconde
        y += 1

        if y >= CONSOLE_HEIGHT - 1:
            y = 0
            x = random.randint(0, CONSOLE_WIDTH - 2)

if __name__ == "__main__":
    main()
