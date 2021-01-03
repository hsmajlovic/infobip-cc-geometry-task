import math

from constants import PRECISION


def rotors_intersect(rotor_1: tuple, rotor_2: tuple) -> list:
    # Code copied from: https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
    (x0, y0), _ = rotor_1
    (x1, y1), _ = rotor_2

    d: float = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    
    # non intersecting
    if d >= 2 - PRECISION:
        return None
    else:
        a: float = d / 2
        h: float = math.sqrt(1 - a ** 2)
        x2: float = x0 + a * (x1 - x0) / d   
        y2: float = y0 + a * (y1 - y0) / d   
        x3: float = x2 + h * (y1 - y0) / d     
        y3: float = y2 - h * (x1 - x0) / d 

        x4: float = x2 - h * (y1 - y0) / d
        y4: float = y2 + h * (x1 - x0) / d
        
        return [(x3, y3), (x4, y4)]


def segments_overlap(segment_1: tuple, segment_2: tuple) -> bool:
    return (max(*segment_1, *segment_2) - min(*segment_1, *segment_2) <=
            segment_2[1] - segment_2[0] + segment_1[1] - segment_1[0] + PRECISION)


def get_angle(point: tuple, center: tuple, offset_angle: float) -> float:
    angle_vector: tuple = (point[0] - center[0], point[1] - center[1])
    angle: float = math.acos(angle_vector[1])
    angle: float = math.pi * 2 - angle if angle < 0 else angle
    
    return angle - offset_angle


def calculate_busy_period(rotor: tuple, intersection_points: list) -> tuple:
    center, angle = rotor

    return tuple(sorted(
        [get_angle(intersection_point, center, angle)
         for intersection_point in intersection_points]))


def find_busy_periods(intersections: dict) -> list:
    busy_periods = list()

    for rotor, intersection_points in intersections.items():
        busy_periods.append(calculate_busy_period(rotor, intersection_points))
    
    return busy_periods
