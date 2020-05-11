#!/usr/bin/env python3

# Import and initialize the pygame library
import pygame
import random
import math
import sys

# list of colors
colors = ["blue", "light_blue", "yellow", "orange", "green"]

config = {
    "sprite": {
        "width": 8,
        "height": 20,
        "speed": 2,
    },
    "images": {
        "blue": "./images/person_blue_64x64.png",
        "light_blue": "./images/person_light_blue_64x64.png",
        "red": "./images/person_red_64x64.png",
        "white": "./images/person_white_64x64.png",
        "yellow": "./images/person_yellow_64x64.png",
        "orange": "./images/person_orange_64x64.png",
        "green": "./images/person_green_64x64.png",
        "black": "./images/person_black_64x64.png"
    },
    "game": {
        "width": 1600,
        "height": 900,
        "day": 0,
        "fps": 40,
        "loop_count": 0
    },
    "sim": {
        "social_distancing": False,
        "social_distance": 20,
        "infection_radius": 10,
        "infection_rate": .20,
        "population_count": 100,
        "pid": 1,
    }
}


class Person(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, **kwargs):
        """ Constructor. 
        """

        # Call the parent class (Sprite) constructor
        super().__init__()
        self.width = kwargs.get("width", 10)
        self.height = kwargs.get("height", 10)
        self.speed = kwargs.get("speed", 1)
        self.coord = kwargs.get("coord", None)
        self.color = kwargs.get("color", "green")

        print(self.coord)

        # choose sprite direction
        self.dx = 0
        self.dy = 0
        while self.dx + self.dy == 0:
            self.dx = random.choice([1, -1, 0])
            self.dy = random.choice([1, -1, 0])

        # give our sprite an image and resize it
        self.image = pygame.image.load(config["images"][self.color])
        self.image = pygame.transform.scale(self.image,
                                            (self.width, self.height))

        # set sprite position
        if self.coord == None:
            self.x = int(random.random() * config["game"]["width"])
            self.y = int(random.random() * config["game"]["height"])
        else:
            self.x = self.coord[0]
            self.y = self.coord[1]

        # sprite bounding rectangle
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def setDxDy(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def getDxDy(self):
        return (self.dx, self.dy)

    def changeDirection(self, sides_contacted):
        if sides_contacted["top"]:
            self.dy = 1
        if sides_contacted["bottom"]:
            self.dy = -1
        if sides_contacted["left"]:
            self.dx = 1
        if sides_contacted["right"]:
            self.dx = -1

    def move(self):

        sides_contacted = self.checkWalls()

        self.changeDirection(sides_contacted)

        if self.dx < 0:
            self.rect.x -= self.speed
        elif self.dx > 0:
            self.rect.x += self.speed

        if self.dy < 0:
            self.rect.y -= self.speed
        elif self.dy > 0:
            self.rect.y += self.speed

    def checkCollide(self, other):
        sides_contacted = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }

        if self.rect.colliderect(other.rect):

            if self.rect.top < other.rect.top:
                sides_contacted["bottom"] = True
                self.rect.y -= abs(self.rect.y - other.rect.y) // 8
            if self.rect.left < other.rect.left:
                sides_contacted["right"] = True
                self.rect.x -= abs(self.rect.x - other.rect.x) // 8
            if self.rect.right > other.rect.right:
                sides_contacted["left"] = True
                self.rect.x += abs(self.rect.x - other.rect.x) // 8
            if self.rect.bottom > other.rect.bottom:
                sides_contacted["top"] = True
                self.rect.y += abs(self.rect.y - other.rect.y) // 8


            self.changeDirection(sides_contacted)

            return True

        return False

    def checkWalls(self):
        sides = {"top": False, "bottom": False, "left": False, "right": False}

        if self.rect.top <= 0:
            sides["top"] = True
        if self.rect.left <= 0:
            sides["left"] = True
        if self.rect.right >= config["game"]["width"]:
            sides["right"] = True
        if self.rect.bottom >= config["game"]["height"]:
            sides["bottom"] = True

        return sides


class Simulation:
    def __init__(self, **kwargs):
        self.population = []
        self.game_width = kwargs.get("width", 500)
        self.game_height = kwargs.get("height", 500)
        self.population_count = kwargs.get("population_count", 10)
        self.sprite_group = pygame.sprite.Group()
        self.screen = kwargs.get("screen", None)

        print(self.screen)

        if self.screen == None:
            print(
                "Error: Simulation needs an instance of a pygame surface / screen!"
            )
            sys.exit()

    def populateSim(self, pos=None):
        for _ in range(self.population_count):
            self.addPerson()

    def addPerson(self, **kwargs):
        color = kwargs.get("color", random.choice(colors))
        width = kwargs.get("width", config["sprite"]["width"])
        height = kwargs.get("height", config["sprite"]["height"])
        speed = kwargs.get("speed", config["sprite"]["speed"])

        x = random.randint(0, self.game_width)
        y = random.randint(0, self.game_height)
        coord = kwargs.get("coord", [x, y])

        p = Person(color=random.choice(colors),
                   width=config["sprite"]["width"],
                   height=config["sprite"]["height"],
                   speed=config["sprite"]["speed"],
                   coord=coord)
        self.population.append(p)
        self.sprite_group.add(p)

    def simRun(self):
        # loop through each person and call a move method
        for i in range(len(self.population)):
            self.population[i].move()
            for j in range(len(self.population)):
                if self.population[i] != self.population[j]:
                    collided = self.population[i].checkCollide(
                        self.population[j])
                    if collided:
                        dx, dy = self.population[i].getDxDy()
                        self.population[j].setDxDy(dx * -1, dy * -1)

        self.sprite_group.draw(self.screen)


#__________________________________________________________________________

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Corona Virus') 

    font = pygame.font.Font('./fonts/Roboto-Black.ttf', 20) 



    # Set up the drawing window
    screen = pygame.display.set_mode(
        [config["game"]["width"], config["game"]["height"]])

    sim = Simulation(screen=screen,
                     width=config["game"]["width"],
                     height=config["game"]["height"],
                     population_count=config["sim"]["population_count"])

    sim.populateSim()

    # helps keep game loop running at
    # specific frames per second
    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True

    #___ GAME LOOP ____________________________________________________________
    while running:
        # Fill the background with blackish
        # Do not do this after you draw sprites!
        screen.fill((30, 30, 30))
        

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                sim.addPerson(coord=pos)

        #___CONTROL SIMULATION HERE_____________________________________________________________

        sim.simRun()

        text = font.render(str(len(sim.population)), True, (30, 255, 30), (30, 30, 255)) 
        textRect = text.get_rect()
        textRect.right = config["game"]["width"]
        textRect.bottom = config["game"]["height"]
        screen.blit(text, textRect) 

        #___END CONTROL SIMULATION_____________________________________________________________

        # This keeps game loop running at a constant FPS
        clock.tick(config["game"]["fps"])  # FPS = frames per second

        # Count number of loops game runs (careful, this number could get LARGE)
        config["game"]["loop_count"] += 1

        # Flip the display (refresh the screen)
        pygame.display.flip()

#___ END GAME LOOP ____________________________________________________________
# Done! Time to quit.
    pygame.quit()
