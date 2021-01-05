import turtle
import math


from constants import DEFAULT_COLOR


turtle.speed(0)
scale_factor: float = 50


def lift_brush(func: object, *args, **kwargs) -> object:
    def _func(*args, **kwargs):
        turtle.up()
        func(*args, **kwargs)
        turtle.up()

    return _func


@lift_brush
def move_brush(to_point: tuple):
    turtle.setpos(to_point[0] * scale_factor, to_point[1] * scale_factor)


@lift_brush
def draw_circle(circle_center: tuple):
    circle_bottom: tuple = (circle_center[0], circle_center[1] - 1)
    move_brush(circle_bottom)
    turtle.down()
    turtle.circle(scale_factor)


@lift_brush
def draw_circles(circle_centers: tuple):
    for circle_center in circle_centers:
        draw_circle(circle_center)


@lift_brush
def draw_dot(dot: tuple):
    move_brush(dot)
    turtle.dot()


@lift_brush
def draw_intersections(intersections: dict):
    points = {point for _, intersection_tuples in intersections.items() if intersection_tuples
              for points_tuple in intersection_tuples for point in points_tuple}
    for point in points:
        draw_dot(point)
