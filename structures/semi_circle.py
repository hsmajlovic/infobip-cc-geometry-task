import math

import shared
from structures.event_point import EventPoint
from constants import PRECISION
from enums import SemiCircleSide
from algorithms.geometry import rotors_intersect


class SemiCircle:
    def __init__(self, circle_center: tuple, side: SemiCircleSide):
        self.circle_center: tuple = circle_center
        self.side: SemiCircleSide = side
    
    def __lt__(self, other) -> bool:
        return self.sweep_line_intersection() < other.sweep_line_intersection()
    
    def __gt__(self, other) -> bool:
        return self.sweep_line_intersection() > other.sweep_line_intersection()
    
    def __eq__(self, other) -> bool:
        return self.circle_center == other.circle_center and self.side == other.side
    
    def __le__(self, other) -> bool:
        return self < other or self == other
    
    def __ge__(self, other) -> bool:
        return self > other or self == other

    def sweep_line_intersection(self) -> tuple:
        term: float = 1 - (shared.sweep_line_progress - 10 * PRECISION - self.circle_center[1]) ** 2
        if term < 0: term = 0
        term: float = math.sqrt(term)
        return self.circle_center[0] + term * ((-1) ** (self.side == SemiCircleSide.left))
    
    def intersect(self, other) -> list:
        if self.circle_center == other.circle_center:
            return list()
        
        intersections = rotors_intersect(
            rotor_center_1=self.circle_center,
            rotor_center_2=other.circle_center)
        
        if intersections is None:
            return list()

        return [intersection for intersection in intersections
                if self.belongs_to_semi_circle(intersection) and other.belongs_to_semi_circle(intersection)]
    
    def belongs_to_semi_circle(self, point: tuple) -> bool:
        diff: float = point[0] - self.circle_center[0]
        return ((self.side == SemiCircleSide.left and diff <= PRECISION) or 
                (self.side == SemiCircleSide.right and diff > 0))
