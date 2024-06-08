from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from scene import InitGL, ReSizeGLScene, DrawGLScene, keyPressed

ESCAPE = b'\033'

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(612, 540)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Solar System")
    
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(612, 540)
    glutMainLoop()
    keyPressed()

if __name__ == "__main__":
    print("Hit ESC key to quit.")
    main()
