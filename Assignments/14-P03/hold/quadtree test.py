#!/usr/bin/env python3

import pygame
from pygame.locals import *
pygame.init()

import time, math, random

### METHODS ###


def n(x):
    y = 1
    for z in range(x):
        y *= z + 1
    return y


def rect_quad_split(rect):
    w = rect.width / 2.0
    h = rect.height / 2.0
    rl = []
    rl.append(
        pygame.Rect(float(rect.left), float(rect.top), float(w), float(h)))
    rl.append(
        pygame.Rect(float(rect.left + w), float(rect.top), float(w), float(h)))
    rl.append(
        pygame.Rect(float(rect.left), float(rect.top + h), float(w), float(h)))
    rl.append(
        pygame.Rect(float(rect.left + w), float(rect.top + h), float(w),
                    float(h)))

    return rl


def lerp(a, b, p):
    return (a + (b - a) * p)


### CLASSES ###


class QuadLeaf(object):
    def __init__(self, world, rect, quadtree, level):
        self.world = world
        self.rect = rect
        self.quadtree = quadtree
        self.level = level

        quadtree.levels[level].append(self)
        self.branches = None
        self.entities = []  #a list of collidable objects on this leaf

    def subdivide(self):
        self.branches = []
        for rect in rect_quad_split(self.rect):
            b = QuadLeaf(self.world, rect, self.quadtree, self.level + 1)
            self.branches.append(b)

    def test_collisions(self, obj):
        for obj2 in self.entities:
            if obj2.rect.colliderect(obj.rect):
                if [obj, obj2] not in self.quadtree.collisions and [
                        obj2, obj
                ] not in self.quadtree.collisions:
                    self.quadtree.collisions.append([obj, obj2])

        if self.level == self.quadtree.level_limit - 1:
            return

        if self.branches != None:
            for b in self.branches:
                b.test_collisions(obj)

    def add_entity(self, obj):
        for obj2 in self.entities:
            if obj2.rect.colliderect(obj.rect):
                if [obj, obj2] not in self.quadtree.collisions and [
                        obj2, obj
                ] not in self.quadtree.collisions:
                    self.quadtree.collisions.append([obj, obj2])

        if self.level == self.quadtree.level_limit - 1:  #if it's hit the limit of levels
            self.entities.append(obj)
            obj.level = int(self.level)
            return

        if self.branches == None:
            self.subdivide()

        #the first thing it has to check is if the object fits in any branches
        fits = None
        for b in self.branches:
            if b.rect.contains(obj.rect):
                fits = b
        if fits == None:
            #doesn't fit in any of the branches, stays on this level
            self.entities.append(obj)
            obj.level = int(self.level)
            for b in self.branches:
                b.test_collisions(obj)
        else:
            #it DOES fit in a branch, hand it to the branch
            fits.add_entity(obj)

    def render(self):
        pygame.draw.rect(self.world.screen, [127, 127, 127], self.rect, 2)
        if self.branches != None:
            for b in self.branches:
                b.render()


class QuadTree(object):
    def __init__(self, world, world_rect):
        self.world = world
        self.world_rect = world_rect

        self.level_limit = 3
        self.reset()

    def add_entity(self, obj):
        for obj2 in self.entities:
            if obj2.rect.colliderect(obj.rect):
                if [obj, obj2] not in self.collisions and [
                        obj2, obj
                ] not in self.collisions:
                    self.collisions.append([obj, obj2])

        if self.level_limit <= 0:
            self.entities.append(obj)
            obj.level = -1
            return

        #the first thing it has to check is if the object fits in any branches
        fits = None
        for b in self.branches:
            if b.rect.contains(obj.rect):
                fits = b
        if fits == None:
            #doesn't fit in any of the branches, stays on main level
            self.entities.append(obj)
            obj.level = -1
            for b in self.branches:
                b.test_collisions(obj)
        else:
            #it DOES fit in a branch, hand it to the branch
            fits.add_entity(obj)

    def test_collisions(self):
        #this means that each object will need a collide command
        for c in self.collisions:
            c[0].collide(c[1])
            c[1].collide(c[0])

    def reset(self):
        self.levels = []
        for x in range(self.level_limit):
            self.levels.append([])
        self.branches = []
        if self.level_limit > 0:
            for rect in rect_quad_split(self.world_rect):
                b = QuadLeaf(self.world, rect, self, 0)
                self.branches.append(b)
        self.entities = []  #a list of all collidable objects on the main level
        self.collisions = []

    def render(self):
        for branch in self.branches:
            branch.render()


class Ball(object):
    def __init__(self, world, pos, radius):
        self.world = world
        self.pos = pos
        self.vector = [0, 0]
        self.radius = radius
        self.set_rect()

        self.level = -1

    def set_rect(self):
        self.rect = pygame.Rect(self.pos[0] - self.radius,
                                self.pos[1] - self.radius, self.radius * 2,
                                self.radius * 2)

    def collide(self, obj):
        x = (self.pos[0] - obj.pos[0])
        y = (self.pos[1] - obj.pos[1])
        dist = math.sqrt(x**2 + y**2)
        if dist <= self.radius + obj.radius and dist != 0:
            #we collided, act apon it
            x /= dist
            y /= dist
            collide_amount = (self.radius + obj.radius) - dist

            p1 = collide_amount / float(self.radius + obj.radius)
            p2 = math.sin(math.radians(lerp(0, 90, p1)))

            p = lerp(
                1, p2,
                0.5)  #the bigger this number, the more squishy the balls are

            collide_amount *= p
            self.vector[0] += x * collide_amount
            self.vector[1] += y * collide_amount

    def update(self):
        ## HEY LOOK AT THIS!!!!
        #you can change these variables!
        self.level = -1
        self.vector[1] = self.vector[1] + 0.0  #<-- simulates gravity

        self.vector[0] = self.vector[0] * 1.0  #<-- simulates air resistance
        self.vector[1] = self.vector[1] * 1.0  #<--

    def move(self):
        dist = math.sqrt(self.vector[0]**2 + self.vector[1]**2)
        if dist > self.radius:
            self.vector[0] /= dist
            self.vector[1] /= dist
            self.vector[0] *= self.radius
            self.vector[1] *= self.radius

        self.pos[0] += self.vector[0]
        self.pos[1] += self.vector[1]

        if self.pos[
                0] - self.radius < self.world.quadtree.world_rect.left or self.pos[
                    0] + self.radius > self.world.quadtree.world_rect.right:
            self.vector[0] *= -1
            self.pos[0] += self.vector[0]
            self.vector[0] *= 0.8

        if self.pos[
                1] - self.radius < self.world.quadtree.world_rect.top or self.pos[
                    1] + self.radius > self.world.quadtree.world_rect.bottom:
            self.vector[1] *= -1
            self.pos[1] += self.vector[1]
            self.vector[1] *= 0.8

        self.set_rect()
        self.world.quadtree.add_entity(self)

    def render(self, showLevel=False):
        if showLevel:
            if self.level == -1:
                c = [255, 0, 0]
            elif self.level == 0:
                c = [255, 255, 0]
            elif self.level == 1:
                c = [0, 255, 0]
            elif self.level == 2:
                c = [0, 255, 255]
            elif self.level == 3:
                c = [0, 0, 255]
            else:
                c = [255, 0, 255]
        else:
            c = [127, 127, 0]
        self.pos[0] = int(self.pos[0])
        self.pos[1] = int(self.pos[1])
        
        self.world.rects.append(
            pygame.draw.circle(self.world.screen, c, self.pos,
                               int(self.radius)))
        pygame.draw.circle(self.world.screen, [0, 0, 0], self.pos, self.radius,
                           1)


##########################################################
###    MAIN    ###########################################
##########################################################


class World(object):
    def __init__(self):
        #SET UP __INIT__
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.clock = pygame.time.Clock()
        self.framerate = 1000

        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)

        self.quadtree = QuadTree(
            self, pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1]))
        self.quadtree.level_limit = 0

        self.balls = []
        for x in range(600):
            radius = (x % 3) * 2 + 6
            self.balls.append(
                Ball(self, [
                    random.randint(50, self.screen_size[0] - 50),
                    random.randint(50, self.screen_size[1] - 50)
                ], radius))

        self.bg_color = [0, 0, 0]
        self.screen.fill(self.bg_color)

        #SET UP ENTITIES
        self.reset()
        self.run()

    def reset(self):
        pass

    def run(self):
        stage = 0
        print(
            "The tree will start turned off. You will see the frame rate will be very low"
        )
        next = time.time() + 10.0
        avg_frame_rate = 0
        prev_frame_rate = 0
        avg_checks = 0

        # RUN MAIN LOOP
        while True:
            self.clock.tick(self.framerate)
            self.events = pygame.event.get()
            self.keys = pygame.key.get_pressed()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_but = pygame.mouse.get_pressed()
            self.fps = self.clock.get_fps()
            self.rects = []

            #UPDATE
            for b in self.balls:
                b.update()

            #MOVE
            for b in self.balls:
                b.move()

            #TEST COLLISIONS
            self.quadtree.test_collisions()

            #RENDER
            if stage != None:
                self.quadtree.render()

            for b in self.balls:
                b.render(stage != None)

            #renders framerate
            img = self.font.render(str(int(self.fps)), True, [255, 255, 255])
            rect = img.get_rect(topleft=[0, 0])
            self.rects.append(rect)
            self.screen.blit(img, rect)

            #renders collision checks
            img = self.font.render(str(int(avg_checks)), True, [255, 255, 255])
            rect = img.get_rect(bottomleft=[0, self.screen_size[1]])
            self.rects.append(rect)
            self.screen.blit(img, rect)

            pygame.display.flip()
            self.screen.fill(self.bg_color)

            for rect in self.rects:
                self.screen.fill(self.bg_color, rect)

            avg_frame_rate = lerp(avg_frame_rate, self.fps, 0.05)
            if stage != None:
                avg_checks = lerp(avg_checks, len(self.quadtree.collisions),
                                  0.1)
                if time.time() >= next:
                    print(stage + 1)
                    if avg_frame_rate > prev_frame_rate:
                        #continues to test
                        prev_frame_rate = avg_frame_rate
                        next = time.time() + 10.0
                        stage += 1
                        self.quadtree.level_limit = stage
                    else:
                        #found peak of preformance
                        print(
                            "Found peak. Preformance for this computer will not be any better then it is now."
                        )
                        M = (len(self.balls) - 1) * len(self.balls)
                        print(f"Would normally have {M} collision checks,")
                        print(
                            "but this quadtree reduces it to roughly {int(avg_checks)}collision checks"
                        )
                        self.quadtree.level_limit = stage - 1
                        stage = None

            #EVENT HANDLER UPDATE
            for event in self.events:
                if event.type == MOUSEBUTTONDOWN:
                    for b in self.balls:
                        b.vector[0] += random.randint(-10, 10)
                        b.vector[1] += random.randint(-10, 10)
                if event.type == KEYDOWN or event.type == QUIT:
                    if event.type == QUIT or event.key == K_ESCAPE:
                        pygame.quit()
                        return

            self.quadtree.reset()


world = World()
