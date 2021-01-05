from collections import defaultdict

from algorithms.geometry import rotors_intersect, ori


def find_intersections_naive(rotors: list) -> dict:
    intersections = defaultdict(list)

    for i in range(len(rotors)):
        for j in range(i + 1, len(rotors)):
            intersection_points = rotors_intersect(rotors[i], rotors[j])
            if intersection_points:
                intersections[rotors[i]].append(
                    intersection_points if ori(rotors[i], *intersection_points) < 0 else tuple(reversed(intersection_points)))
                intersections[rotors[j]].append(
                    intersection_points if ori(rotors[j], *intersection_points) < 0 else tuple(reversed(intersection_points)))
    
    return intersections


def find_intersections_fast(rotors: list) -> dict:
    pass
