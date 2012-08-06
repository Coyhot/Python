from particlesdata import *
pygame.init()

screen = pygame.display.set_mode((600,600))
size = random.randint(1,50)
x,y = 0,300
particles = ParticleContainer()
speed = random.random()/10
nb = 3
angle = random.randint(0,360)
particles.gen_particles((10,50),nb,speed,angle)
selectedParticle = None
dragging = False
creating = False
while 1:
    pygame.display.flip()
    screen.fill((0,0,0))
    particles.moveAll(selectedParticle)
    particles.bounceAll()
    particles.displayAll(screen)
    for i,p1 in enumerate(particles.getParticles()):
        for p2 in particles.getParticles()[i+1:]:
            #particles.collide(p1,p2,screen)
            pass
            
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 2:
            creating = True
            particles.new((10,50),nb,speed,angle,(event.pos[0],event.pos[1]))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                particles.empty()
                particles.gen_particles((10,50),nb,speed,angle)
            if event.button == 1:
                mouseX, mouseY = event.pos[0], event.pos[1]
                selectedParticle = particles.findParticle(mouseX,mouseY)
                if selectedParticle:
                    dragging = True
                    selectedParticle.x,selectedParticle.y = mouseX,mouseY
        if event.type == MOUSEMOTION and creating == True:
            particles.check()
            particles.new((10,50),nb,speed,angle,(event.pos[0],event.pos[1]))
        if event.type == MOUSEMOTION and dragging == True:
            dx,dy = event.pos[0] - selectedParticle.x, event.pos[1] - selectedParticle.y
            selectedParticle.x,selectedParticle.y = event.pos[0],event.pos[1]
            selectedParticle.angle = degrees(atan2(dy,dx))+90
            selectedParticle.speed = hypot(dx,dy) * 0.1
            
        if event.type == MOUSEBUTTONUP and event.button == 2:
            creating = False
        if event.type == MOUSEBUTTONUP and event.button == 1:
            selectedParticle = None
            dragging = False
            
        if event.type == QUIT:
            pygame.quit()