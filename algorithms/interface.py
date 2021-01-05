from utils import tictoc
from algorithms.geometry import find_busy_periods, merge_segments
from algorithms.intersections import find_intersections_naive, find_intersections_fast


def rotors_finder(
        rotors: list,
        intersections_finder: object) -> list:
    verbose: bool = len(rotors) < 2 ** 4
    
    intersections: dict = intersections_finder(rotors)
    busy_periods: list = find_busy_periods(intersections)
    merged_busy_periods: list = merge_segments(busy_periods)

    if verbose:
        from draw import draw_circles, draw_intersections, turtle, math

        draw_circles(rotors)
        draw_intersections(intersections)

        print(f'Busy periods: {[[e * 180 / math.pi for e in t] for t in busy_periods]}')
        print(f'Busy periods merged: {[[e * 180 / math.pi for e in t] for t in merged_busy_periods]}')
        turtle.done()

    return merged_busy_periods


@tictoc
def rotors_quadratic_slowest(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_naive)
    

@tictoc
def rotors_quadratic_intermediate(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_fast)


@tictoc
def rotors_quadratic_faster(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_naive)


@tictoc
def rotors_nlogn(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_fast)
