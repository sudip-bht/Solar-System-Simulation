from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from texture_loader import LoadTextures

def draw_celestial_body(texture_file, radius, position, with_blending=False, ring=False):
    texture = LoadTextures(texture_file)
    
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GL_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(*position)
    gluSphere(quadric, radius, 32, 16)
    
    if with_blending:
        glColor4f(1.0, 1.0, 1.0, 0.4)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)
        gluSphere(quadric, radius, 32, 16)
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glDisable(GL_BLEND)
    
    if ring:
        glPushMatrix()
        glScalef(1.1, 1, 1)
        glutWireTorus(0.10, 0.67, 100, 50)
        glPopMatrix()
    
    glPopMatrix()
    gluDeleteQuadric(quadric)
