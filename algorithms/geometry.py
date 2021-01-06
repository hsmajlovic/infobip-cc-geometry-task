import math

from constants import PRECISION


def ori(p1: tuple, p2: tuple, p3: tuple) -> int:
    a = [p2[0] - p1[0], p2[1] - p1[1]]
    b = [p3[0] - p1[0], p3[1] - p1[1]]

    theta = a[0] * b[1] - a[1] * b[0]

    if -PRECISION < theta < PRECISION:
        return 0
    # oriented counter clockwise (positive)
    if theta > 0:
        return 1
    # oriented clockwise (negative)
    if theta < 0:
        return -1


def rotors_intersect(rotor_center_1: tuple, rotor_center_2: tuple) -> list:
    # Code copied from: https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
    x0, y0 = rotor_center_1
    x1, y1 = rotor_center_2

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
        
        return ((round(x3, -int(math.log10(PRECISION))), round(y3, -int(math.log10(PRECISION)))),
                (round(x4, -int(math.log10(PRECISION))), round(y4, -int(math.log10(PRECISION)))))


def segments_overlap(segment_1: tuple, segment_2: tuple) -> bool:
    return (max(*segment_1, *segment_2) - min(*segment_1, *segment_2) <=
            segment_2[1] - segment_2[0] + segment_1[1] - segment_1[0] + PRECISION)


def get_angle(point: tuple, center: tuple) -> tuple:
    angle_vector: tuple = (point[0] - center[0], point[1] - center[1])
    angle: float = math.acos(angle_vector[1])
    angle: float = math.pi * 2 - angle if angle_vector[0] < 0 else angle
    
    return angle


def get_period(intersection_interval: tuple, center: tuple) -> tuple:
    return tuple([get_angle(point, center) for point in intersection_interval])


def calculate_busy_periods(rotor_center: tuple, intersection_intervals: list) -> list:
    busy_periods = list()

    for intersection_interval in intersection_intervals:
        period: tuple = get_period(intersection_interval, rotor_center)
        if period[0] > math.pi > period[1]:
            busy_periods.append((period[0], math.pi * 2))
            busy_periods.append((0, period[1]))
        else:
            busy_periods.append(period)
    
    return busy_periods


def find_busy_periods(intersections: dict) -> list:
    busy_periods = list()

    for rotor_center, intersection_intervals in intersections.items():
        busy_periods.extend(calculate_busy_periods(rotor_center, intersection_intervals))
    
    return busy_periods


def merge_segments(segments: list) -> list:
    all_points = list()
    beginnings = set()
    ends = set()
    
    for segment in segments:
        beginnings.add(segment[0])
        ends.add(segment[1])
        all_points.extend(segment)
    
    merged_segments = list()
    open_segments: int = 0
    merged_segment = list()

    for point in sorted(all_points):
        if point in beginnings:
            if open_segments == 0:
                merged_segment.append(point)
            open_segments += 1
            
        if point in ends:
            open_segments -= 1
            if open_segments == 0:
                merged_segment.append(point)
                merged_segments.append(tuple(merged_segment))
                merged_segment.clear()
    
    return merged_segments
