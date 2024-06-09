# Camera controls\

transform reset:
    matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0) 
    zpos 0 xpos 0 ypos 0
    xoffset 0 yoffset 0

transform smoothreset:
    ease 2.0 matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0) zpos 0 xpos 0 ypos 0 xoffset 0 yoffset 0
    matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0) 
    zpos 0 xpos 0 ypos 0
    xoffset 0 yoffset 0