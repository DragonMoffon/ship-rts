from pyglet import math
from math import cos, sin, pi

vec2 = math.Vec2
vec3 = math.Vec3
vec4 = math.Vec4

mat3 = math.Mat3
mat4 = math.Mat4

radians = pi / 180.0
degrees = 180.0 / pi

def translation(shift: vec2) -> mat3:
    return mat3(
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        -shift.x, shift.y, 1.0
    )

def rotation(angle: float) -> mat3:
    rads = radians * angle#
    c = cos(rads)
    s = sin(rads)
    return mat3(
        c, s, 0.0,
        -s, c, 0.0,
        0.0, 0.0, 1.0
    )

def scale(scale: vec2) -> mat3:
    return mat3(
        1/scale.x, 0.0, 0.0,
        0.0, 1/scale.y, 0.0,
        0.0, 0.0, 1.0
    )

def transform(shift: vec2, angle: float, scale: vec2 = vec2(1.0, 1.0)) -> mat3:
    rads = radians * angle
    c = cos(rads)
    s = sin(rads)
    return mat3(
        c / scale.x, s, 0.0,
        -s, c / scale.y, 0.0,
        -shift.x, shift.y, 1.0
    )