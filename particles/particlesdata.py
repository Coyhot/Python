import pygame
from pygame.locals import *
import sys
import os
from math import *
import random
import sys
gravity = (180,0.0)
elasticity = 1.0
airMass = 0.1
G = 50
def addVectors((angle1, length1), (angle2, length2)):
    x  = sin(radians(angle1)) * length1 + sin(radians(angle2)) * length2
    y  = cos(radians(angle1)) * length1 + cos(radians(angle2)) * length2
    length = hypot(x, y)
    angle = 90 - degrees(atan2(y, x))
    return (angle, length)

class ParticleContainer:
    def __init__(self):
        self.particles = []
    def new(self,(minsize,maxsize),nb,speed,angle,(x,y)):
            size = random.randint(minsize,maxsize)
            self.particles.append(Particle((x,y),size,))
            
    def gen_particles(self,(minsize,maxsize),nb,speed,angle):
        for i in range(nb):
            size = random.randint(minsize,maxsize)
            x,y = random.randint(0,600),random.randint(0,600)
            
            self.particles.append(Particle((x,y),size,))
    def display(self,i):
        self.particles[i].display()
    def move(self, i):
        self.particles[i].move()
    def displayAll(self,screen):
        for particle in self.particles:
            particle.display(screen)
    def findParticle(self,x,y):
        for p in self.particles:
            if hypot(p.x-x,p.y-y) <= p.size:
                return p
    def check(self):
        if len(self.particles) > 300:
            self.particles.pop(0)
    def moveAll(self,selectedParticle):
        for particle in self.particles:
            if particle != selectedParticle:
                particle.move()
    def bounceAll(self):
        for particle in self.particles:
            particle.bounce()
    def empty(self):
        self.particles = []
    def clean(self):
        for p in self.particles:
            if p.clean() == True:
                self.particles.remove(p)
    def attract(self):
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 != p2:
                    dx,dy = p1.x - p2.x , p1.y-p2.y
                    distance = hypot(dx,dy)
                    force = ((1/((distance)*(distance)))/G)*p2.size*p2.size
                    angle = degrees(atan2(dy,dx))+270
                    p1.angle,p1.speed = addVectors((p1.angle,p1.speed),(angle,force))
                    if p2.size != 0 and p1.size != 0 and p1.size + p2.size > distance:
                        p1.merge(p2)
            p1.move()
    def collide(self,p1,p2,screen):
        dx,dy = p1.x-p2.x, p1.y-p2.y
        distance = hypot(dx,dy)
        if distance < p1.size + p2.size:
            totalMass = p1.mass + p2.mass
            tangent = degrees(atan2(dy,dx))
            angle = 90 + tangent
            overlap = (p1.size + p2.size)-distance
            p1.x += sin(radians(angle))*overlap
            p1.y -= cos(radians(angle))*overlap
            p2.x -= sin(radians(angle))*overlap
            p2.y += cos(radians(angle))*overlap
            p1.angle = 2*tangent - p1.angle
            p2.angle = 2*tangent - p2.angle
            p1.speed *= overlap/p1.size*10
            p2.speed = overlap/p2.size*10

            p1.speed *= elasticity
            p2.speed *= elasticity

                





    def getParticles(self):
        return self.particles

class Particle:
    def __init__(self,(x,y),size):
        self.x, self.y = x,y
        self.size = size
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.mass = random.random()
        self.colour = (self.mass*255,0,(255-(self.mass*255)),100)
        self.drag = 1
    def clean(self):
        if self.size == 0:
            return True
    def setSpeed(self,movement):
        self.speed = movement
        
    def setAngle(self,angle):
        self.angle = angle
    def merge(self,p2):
        if self.size > 0 and p2.size > 0:
            if self.size > p2.size:
                self.size += 1
                p2.size -= 1
            if self.size <= p2.size:
                p2.size += 1
                self.size -= 1

        


    def move(self):
        self.x += sin(radians(self.angle)) * self.speed
        self.y -= cos(radians(self.angle)) * self.speed
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.speed *= self.drag
    def bounce(self):
        if self.x > 600 - self.size:
            self.x = 2*(600-self.size)-self.x
            self.angle = -self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        if self.y > 600 -self.size:
            self.y = 2*(600- self.size)-self.y
            self.angle = 180 - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = 180- self.angle
            self.speed *= elasticity
            
    def display(self,screen):
        if self.size >0:
            
            pygame.draw.circle(screen,self.colour,(int(self.x), int(self.y)), int(self.size), self.thickness)
    def verify(self):
        if self.size > 100:
            return 1
        else:
            return 0
        
        
