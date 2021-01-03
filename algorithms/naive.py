from algorithms.geometry import rotors_intersect, segments_overlap


def find_intersections_naive(rotors: list) -> dict:
    intersections = dict()

    for i in range(len(rotors)):
        for j in range(i + 1, len(rotors)):
            intersection_points = rotors_intersect(rotors[i], rotors[j])
            if intersection_points:
                intersections[rotors[i]] = intersection_points
                intersections[rotors[j]] = intersection_points
    
    return intersections


def merge_to_periods(merged_busy_periods, busy_period) -> list:
    left_boundary: float = busy_period[0]
    right_boundary: float = busy_period[1]

    skip_periods = set()

    for merged_period in merged_busy_periods:
        if segments_overlap(merged_period, busy_period):
            skip_periods.add(merged_period)
            left_boundary = min(left_boundary, *busy_period, *merged_period)
            right_boundary = max(right_boundary, *busy_period, *merged_period)
    
    merged_busy_periods.append((left_boundary, right_boundary))

    return [period for period in merged_busy_periods if period not in skip_periods]


def merge_free_periods_naive(busy_periods: list) -> list:
    merged_busy_periods = list()

    for busy_period in busy_periods:
        merged_busy_periods: list = merge_to_periods(merged_busy_periods, busy_period)
    
    return merged_busy_periods