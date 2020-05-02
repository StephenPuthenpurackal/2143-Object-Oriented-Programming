#!/usr/bin/env python3

'''
DO NOT USE 
'''
# Import and initialize the pygame library
import pygame
import random
import math
import sys

# list of colors
colors = ["blue", "light_blue", "yellow", "orange", "green"]

config = {
    "sprite": {
        # "width": 25,
        # "height": 40,
        "width": 12,
        "height": 20,
        "speed": 1,
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
        # "width": 1600,
        # "height": 900,
        "width": 600,
        "height": 600,
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
        "caption":"Virus Outbreak"
    }
}


def Pid():
    pid = config["sim"]["pid"]
    config["sim"]["pid"] += 1
    return pid


class Person(pygame.sprite.Sprite):
    '''
    This class represents the ball.
    It derives from the "Sprite" class in Pygame
    '''
    def __init__(self, **kwargs):
        ''' Constructor. 
        '''

        # Call the parent class (Sprite) constructor
        super().__init__()
        self.width = kwargs.get("width", 10)
        self.height = kwargs.get("height", 10)
        self.speed = kwargs.get("speed", 1)
        self.coord = kwargs.get("coord", None)
        self.color = kwargs.get("color", "green")
        self.pid = Pid()

        self.state = "susceptible"

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

    def __repr__(self):
        ''' Call the __str__method. __repr__ is an exact unambiguous 
            representation of an object, but we will be good with the
            __str__ version for now.
        '''

        return self.__str__()

    def __str__(self):
        ''' Print everything about a person out in a readable format.
        '''
        # assign values to small vars to make print 
        # statement readable
        w = self.width
        h = self.height
        s = self.speed
        c = self.color
        p = self.pid 
        x = self.x
        y = self.y
        dx = self.dx
        dy = self.dy
        t = self.rect.top
        b = self.rect.bottom
        l = self.rect.left
        r = self.rect.right

        return  f"pid: {p}, w:{w}, h:{h}, s:{s}, x:{x}, y:{y}, dx:{dx}, dy:{dy}, rect:[{t},{b},{l},{r}], state:{self.state}"


    def setDxDy(self, dx, dy):
        ''' Set the direction of a person
            Params:
                dx [int] : x direction 
                dy [int] : y direction
            Example:
                Possible x and y values  : [1,-1,0]
                x = 1
                y = -1
                setDxDy(x,y)
        '''
        self.dx = dx
        self.dy = dy

    def getDxDy(self):
        ''' Get the direction of a person
            Returns:
                [tuple] : (x coord , y coord)
        '''
        return (self.dx, self.dy)

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
        ''' Checks to see if we collided with some "other" person
            Params:
                other [Person] : another Person object
            Returns:
                [bool] : True = collided False = nope
        '''
        sides_contacted = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }

        # If collision is True between myself and other
        if self.rect.colliderect(other.rect):
            sides_contacted = {
                "top": False,
                "bottom": False,
                "left": False,
                "right": False
            }

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

    def changeDirection(self, sides_contacted):
        ''' Looks at which side collision happened and changes
            direction accordingly.
        '''
        if sides_contacted["top"]:
            self.dy = 1
        if sides_contacted["bottom"]:
            self.dy = -1
        if sides_contacted["left"]:
            self.dx = 1
        if sides_contacted["right"]:
            self.dx = -1

    def checkWalls(self):
        ''' Determines if a person hit a wall, and which one.
        '''
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

# class SimStats(object):
#     def __init__(self):
#         pass

# class Community(SimStats):
#     def __init__(self):
#         pass


class Population(list):
    def __init__(self, _list=[]):
        list.__init__(self,_list)

        '''
            x1,y1 -----------------------+
            |                            |
            |                            |
            |                            |
            |                            |
            +------------------------x2,y2
                                     width,height
        '''
        # boundaries 
        self.x1 = 0                             # upper left x
        self.y1 = 0                             # upper left y

        self.x2 = config["game"]["width"]       # lower right x
        self.y2 = config["game"]["height"]      # lower right y

        self.w = int(self.x2 - self.x1)         # width 
        self.h = int(self.y2 - self.y1)         # height

        self.counts = {
            "susceptible":0,
            "infected":0,
            "removed":0
        }

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        ''' Print everything about a population out in a readable format.
        '''
        s = ""
        for p in self[:]:
            t = str(p)
            s += t + "\n"
        return s

    def getUpperLeft(self):
        ''' return the upperleft coords of this population
            group.
        '''
        return (x1,y1)

    def getLowerRight(self):
        ''' return the lowerright coords of this population
            group.
        '''
        return (x2,y2)

    def setUpperLeft(self,coords):
        ''' return the upperleft coords of this population
            group.
        '''
        self.x1 = coords[0]
        self.y1 = coords[1]

    def setLowerRight(self,coords):
        ''' return the lowerright coords of this population
            group.
        '''
        self.x2 = coords[0]
        self.y2 = coords[1]
    
    def _ResetCounts(self):
        ''' Private method to reset the counts dictionary to zeros
        '''
        self.counts = {
            "susceptible":0,
            "infected":0,
            "removed":0
        }

    def Stats(self):
        ''' Calculate stats (counts for now)
        '''
        self._ResetCounts()
        for p in self[:]:
            self.counts[p.state] += 1
        
        return self.counts



class Community(Population):
    def __init__(self, **kwargs):
        pass


def CreateCommunities(rows=1,cols=1,padding=10):
    total = rows * cols
    comm = []
    for i in range(rows):
        for j in range(cols):
            pass
    

class Simulation:
    def __init__(self, **kwargs):

        self.screen = kwargs.get("screen", None)
        if self.screen == None:
            print(
                "Error: Simulation needs an instance of a pygame surface / screen!"
            )
            sys.exit()

        self.communities = CreateCommunities()
        self.population = Population()
        self.game_width = kwargs.get("width", 500)
        self.game_height = kwargs.get("height", 500)
        self.population_count = kwargs.get("population_count", 10)
        self.sprite_group = pygame.sprite.Group()
        self.collision_count = 0
        

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
                    collided = self.population[i].checkCollide(self.population[j])
                    if collided:
                        dx, dy = self.population[i].getDxDy()
                        self.population[j].setDxDy(dx * -1, dy * -1)

        self.sprite_group.draw(self.screen)

class FontHelper:
    def __init__(self,**kwargs):
        self.screen = kwargs.get("screen", None)

        if not isinstance(self.screen, pygame.Surface):
            print("Error, FontHelper needs a 'pygame.Surface' to be passed in when constructed! Aborting.") 
            sys.exit()
        
        self.font_size = kwargs.get("font_size", 20)
        self.font_path = kwargs.get("font_path", None)
        
        if not self.font_path:
            self.font_path = './fonts/Roboto-Black.ttf'

        self.color = kwargs.get("color", (255,255,255))
        self.background = kwargs.get("background", (0,0,0))
        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.font = pygame.font.Font(self.font_path, self.font_size)

        self.location = None


    def printLocation(self,location):
        '''
        location can be a list with: [top,bottom,left,right]
            top,bottom,left,right = print at respective location in the center (top center, left center, etc.)
            top,right = print at top right corner
            bottom,left = print at bottem left corner
        location can be a tuple with: (x,y)
            gives exact location to print
        '''
        if isinstance(location, list):
            self.location = location
            self.x = -1
            self.y = -1
        
        if isinstance(location, tuple):
            self.x = location[0]
            self.y = location[1]
            self.location = None

    def print(self,text):
        if isinstance(text, list):
            text = ', '.join(map(str, text))
        elif not isinstance(text,str):
            text = str(text)

        # text to print, antialias, foregroundcolor, backgroundcolor (30, 255, 30), (30, 30, 255)
        text = self.font.render(text, True, self.color, self.background) 
        textRect = text.get_rect()

        if self.x > 0 and self.y > 0:
            textRect.center.x = self.x
            textRect.center.y = self.y
        else:
            textRect.x = config["game"]["width"] // 2
            textRect.y = config["game"]["height"] // 2
            if "top" in self.location:
                textRect.top = 0
            if "bottom" in self.location:
                textRect.bottom = config["game"]["height"]
            if "left" in self.location:
                textRect.left = 0           
            if "right" in self.location:
                textRect.right = config["game"]["width"]

        self.screen.blit(text, textRect) 

#__________________________________________________________________________

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(config["sim"]["caption"]) 
    # Set up the drawing window
    screen = pygame.display.set_mode(
        [config["game"]["width"], config["game"]["height"]])

    font = pygame.font.Font('./fonts/Roboto-Black.ttf', 20) 

    fh = FontHelper(screen=screen)
    fh.printLocation(["top","left"])
    

    sim = Simulation(screen=screen,
                     width=config["game"]["width"],
                     height=config["game"]["height"],
                     population_count=config["sim"]["population_count"])

    sim.populateSim()

    print(sim.population)

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

        # text = font.render(str(len(sim.population)), True, (30, 255, 30), (30, 30, 255)) 
        # textRect = text.get_rect()
        # textRect.right = config["game"]["width"]
        # textRect.bottom = config["game"]["height"]
        # screen.blit(text, textRect) 

        fh.print(str(len(sim.population)))

        print(sim.population.Stats())

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
