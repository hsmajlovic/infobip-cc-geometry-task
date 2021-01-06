class EventPoint:
    def __init__(self, coordinates: tuple, affiliations: list, event_type: object):
        self.coordinates: tuple = coordinates
        self.affiliations: list = affiliations
        self.event_type: object = event_type
    
    def __lt__(self, other) -> bool:
        return (self.coordinates[1], self.coordinates[0]) > (other.coordinates[1], other.coordinates[0])
    
    def __gt__(self, other) -> bool:
        return (self.coordinates[1], self.coordinates[0]) < (other.coordinates[1], other.coordinates[0])
    
    def __eq__(self, other) -> bool:
        return self.coordinates == other.coordinates
    
    def __le__(self, other) -> bool:
        return self < other or self == other
    
    def __ge__(self, other) -> bool:
        return self > other or self == other
