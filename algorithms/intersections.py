import heapq
from collections import defaultdict

from sortedcontainers import SortedList

import shared
from algorithms.geometry import rotors_intersect, ori
from structures.event_point import EventPoint
from structures.semi_circle import SemiCircle
from enums import EventPointType, SemiCircleSide


def quadratic_generator(rotors: list):
    for i in range(len(rotors)):
        for j in range(len(rotors)):
            if i == j:
                continue
            yield (rotors[i], rotors[j])


def form_periods(pairs) -> dict:
    intersections = defaultdict(list)

    for pair in pairs:
        intersection_points = rotors_intersect(*pair)
        if intersection_points:
            intersections[pair[0]].append(
                intersection_points if ori(pair[0], *intersection_points) < 0 else tuple(reversed(intersection_points)))
    
    return intersections


def find_intersections_naive(rotors: list) -> dict:
    return form_periods(quadratic_generator(rotors))


def find_intersections_fast(rotors: list) -> dict:
    intersection_pairs = set()
    intersections_set = set()
    status_array = SortedList()
    event_points: list = []

    for rotor_center in rotors:
        affiliations: list = [
            SemiCircle(circle_center=rotor_center, side=side)
            for side in [SemiCircleSide.left, SemiCircleSide.right]]
        heapq.heappush(event_points, EventPoint(
            coordinates=(rotor_center[0], rotor_center[1] + 1),
            affiliations=affiliations,
            event_type=EventPointType.upper))
        heapq.heappush(event_points, EventPoint(
            coordinates=(rotor_center[0], rotor_center[1] - 1),
            affiliations=affiliations,
            event_type=EventPointType.bottom))
    
    while event_points:
        next_event_point: EventPoint = heapq.heappop(event_points)
        shared.sweep_line_progress = next_event_point.coordinates[1]

        if next_event_point.event_type == EventPointType.upper:
            status_array.update(next_event_point.affiliations)
        
        if next_event_point.event_type == EventPointType.intersection:
            status_array.discard(next_event_point.affiliations[0])
            status_array.discard(next_event_point.affiliations[1])
            status_array.update(next_event_point.affiliations)
        
        left_semi_circle_position: int = status_array.index(min(next_event_point.affiliations))
        # assert max(next_event_point.affiliations) == status_array[left_semi_circle_position + (-1) ** (next_event_point.event_type == EventPointType.intersection)]
        
        if next_event_point.event_type == EventPointType.bottom:
            status_array.discard(next_event_point.affiliations[0])
            status_array.discard(next_event_point.affiliations[1])

        refine_intersections(
            intersection_pairs=intersection_pairs,
            intersections_set=intersections_set,
            status_array=status_array,
            event_points=event_points,
            left_semi_circle_position=left_semi_circle_position,
            deletion=next_event_point.event_type == EventPointType.bottom)
        
    return form_periods(intersection_pairs)


def refine_intersections(
        intersection_pairs: set,
        intersections_set: set,
        status_array: SortedList,
        event_points: list,
        left_semi_circle_position: int,
        deletion: bool) -> set:
    if left_semi_circle_position > 0:
        right_semi: SemiCircle = status_array[left_semi_circle_position]
        left_semi: SemiCircle = status_array[left_semi_circle_position - 1]
        
        for intersection_point in right_semi.intersect(left_semi):
            if intersection_point not in intersections_set:
                intersections_set.add(intersection_point)
                heapq.heappush(event_points, EventPoint(
                    coordinates=intersection_point,
                    affiliations=[left_semi, right_semi],
                    event_type=EventPointType.intersection))
                intersection_pairs.add((left_semi.circle_center, right_semi.circle_center))
                intersection_pairs.add((right_semi.circle_center, left_semi.circle_center))
    
    elif left_semi_circle_position + 2 < len(status_array) and not deletion:
        right_semi: SemiCircle = status_array[left_semi_circle_position + 2]
        left_semi: SemiCircle = status_array[left_semi_circle_position + 1]

        for intersection_point in right_semi.intersect(left_semi):
            if intersection_point not in intersections_set:
                intersections_set.add(intersection_point)
                heapq.heappush(event_points, EventPoint(
                    coordinates=(intersection_point[0], intersection_point[1]),
                    affiliations=[left_semi, right_semi],
                    event_type=EventPointType.intersection))
                intersection_pairs.add((left_semi.circle_center, right_semi.circle_center))
                intersection_pairs.add((right_semi.circle_center, left_semi.circle_center))
