from vpython import *
import math
Radius,mass = 5e-3,0.509    #Si unit ball
sradius,L = Radius/100,2*Radius    #Helix
g = vec(0,-9.8,0)
theta = math.pi/4
shift = vec(2*Radius*cos(theta),2*Radius*sin(theta),0)#left up shiht

scene = canvas(width = 600,height = 600,center = vec(0,0,0),background = vec(0.5,0.5,0))
wall = box(height = 0.1,width = 0.1,length = 0.0002,pos = vec(-0.02,0,0),color = color.red)
balls = []
springs = []
class makeaball(sphere):
    m = 1
    notcross = False
    
ball = makeaball(radius = Radius,color=color.white,pos = vec(wall.pos.x-Radius,wall.pos.y+0.03,wall.pos.z),m = mass)
balls.append(ball)
ball.v = vec(0.001,0,0)
while(balls[-1].pos.y<(wall.pos.y+wall.height/2)):
    ball = makeaball(radius = Radius,color=color.white,pos = balls[-1].pos+vec(0,2*Radius,0),m = mass)
    balls.append(ball)
    spring = helix(pos = balls[-2].pos,axis = balls[-1].pos-balls[-2].pos,radius = sradius)
    springs.append(spring)
ball = makeaball(radius = Radius,color=color.white,pos = balls[-1].pos+shift ,m = mass)
balls.append(ball)
spring = helix(pos = balls[-2].pos,axis = balls[-1].pos-balls[-2].pos,radius = sradius)
springs.append(spring)
shift.y *= -1
ball = makeaball(radius = Radius,color=color.white,pos = balls[-1].pos+shift ,m = mass)
balls.append(ball)
spring = helix(pos = balls[-2].pos,axis = balls[-1].pos-balls[-2].pos,radius = sradius)
springs.append(spring)
while(balls[-1].pos.y>=balls[0].pos.y):
    ball = makeaball(radius = Radius,color=color.white,pos = balls[-1].pos-vec(0,2*Radius,0),m = mass)
    balls.append(ball)
    spring = helix(pos = balls[-2].pos,axis = balls[-1].pos-balls[-2].pos,radius = sradius)
    springs.append(spring)
    
while True:
    rate(1000)
    #balls[1].pos.x += 0.000001
"""
while True:
    rate(1000)
    if(balls[-1].pos.y>wall.pos.y+0.03+Radius):
        ball = makeaball(radius = Radius,color=color.white,pos = vec(wall.pos.x-Radius,wall.pos.y+0.03,wall.pos.z),m = mass)
        balls.append(ball)
        spring = helix(pos = balls[-2].pos,axis = balls[-1].pos-balls[-2].pos,radius = sradius)
    
    ball.pos+=ball.v*dt
"""
