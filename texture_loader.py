from OpenGL.GL import *
from PIL import Image

textures = {}

def LoadTextures(fname):
    if textures.get(fname) is not None:
        return textures.get(fname)
    
    texture = textures[fname] = glGenTextures(1)
    image = Image.open(fname)
    ix, iy = image.size
    image = image.tobytes("raw", "RGBX", 0, -1)
    
    glBindTexture(GL_TEXTURE_2D, texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    return texture
file_names=['images/mercurymap.bmp','images/venusmap.bmp','images/earthmap.bmp','images/marsmap.bmp','images/jupitermap.bmp','images/saturnmap.bmp','images/uranusmap.bmp','images/mercurymap.bmp','images/stars.bmp','images/sun.tga']
def load_all_textures():
    for file_name in file_names:
        LoadTextures(file_name)
