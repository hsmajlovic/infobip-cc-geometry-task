import turtle


turtle.speed(0)
scale_factor: float = 10


def lift_brush(func: object, *args, **kwargs) -> object:
    def _func(*args, **kwargs):
        func(*args, **kwargs)
        turtle.up()

    return _func


@lift_brush
def move_brush(to_point: tuple):
    turtle.setpos(to_point[0] * scale_factor, to_point[1] * scale_factor)


@lift_brush
def draw_circle(circle_center: tuple):
    move_brush(circle_center)
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
    for _, intersection_points in intersections.items():
        if intersection_points:
            for point in intersection_points:
                draw_dot(point)
