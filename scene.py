from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from celestial_bodies import draw_celestial_body
from texture_loader import LoadTextures, load_all_textures

ESCAPE = b'\033'

rotations = [0.0] * 8
LightAmb = (0.7, 0.7, 0.7)
LightDif = (1.0, 1.0, 0.0)
LightPos = (4.0, 4.0, 6.0, 1.0)

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glClearStencil(0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDif)
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    load_all_textures()

def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawStars(Width, Height):
    glColor3f(1.0, 1.0, 1.0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glDisable(GL_DEPTH_TEST)
    glBindTexture(GL_TEXTURE_2D, LoadTextures('images/stars.bmp'))
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(-Width, Height)
    glVertex2d(-Width, -Height)
    glTexCoord2f(Width, Width)
    glVertex2d(Width, 0)
    glTexCoord2f(Width, 0.0)
    glVertex2d(Width, Height)
    glTexCoord2f(0.0, 0.0)
    glVertex2d(0, Height)
    glEnd()
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)

def DrawGLScene():
    global rotations
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    DrawStars(25, 25)
    glTranslatef(0.0, 0.0, -20.0)
    
    celestial_bodies = [
        ('images/mercurymap.bmp', 0.2, (0.0, 0.0, 1.9)),
        ('images/venusmap.bmp', 0.3, (0.0, 0.0, 3.0)),
        ('images/earthmap.bmp', 0.4, (0.0, 0.0, 4.0)),
        ('images/marsmap.bmp', 0.45, (0.0, 0.0, 5.5)),
        ('images/jupitermap.bmp', 0.6, (0.0, 0.0, 7.0)),
        ('images/saturnmap.bmp', 0.55, (0.0, 0.0, 8.5), True),
        ('images/uranusmap.bmp', 0.55, (0.0, 0.0, 10.0)),
        ('images/neptunemap.bmp', 0.45, (0.0, 0.0, 11.5))
    ]
    
    for i, body in enumerate(celestial_bodies):
        glRotatef(rotations[i], 1.0, 0.0, 0.0)
        glRotatef(rotations[i], 0.0, 1.0, 0.0)
        glRotatef(-1, 0.0, 0.0, 1.0)
        if len(body) == 4:
            draw_celestial_body(body[0], body[1], body[2], ring=body[3])
        else:
            draw_celestial_body(body[0], body[1], body[2])

    draw_celestial_body('images/sun.tga', 0.7, (0.0, 0.0, 0.0), with_blending=True)
    
    rotations = [(rot + 0.16) % 360 for rot in rotations]
    
    glutSwapBuffers()

def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()
