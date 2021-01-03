from utils import tictoc
from algorithms.geometry import find_busy_periods
from algorithms.naive import find_intersections_naive, merge_free_periods_naive
from algorithms.fast import find_intersections_fast, merge_free_periods_fast


def rotors_finder(
        rotors: list,
        intersections_finder: object,
        periods_merger: object) -> list:
    verbose: bool = False  # len(rotors) < 2 ** 4
    
    intersections: dict = intersections_finder(rotors)
    busy_periods: list = find_busy_periods(intersections)
    free_periods: list = periods_merger(busy_periods)

    if verbose:
        from draw import draw_circles, draw_intersections

        draw_circles([circle_center for circle_center, _ in rotors])
        draw_intersections(intersections)

        print(f'Free periods: {free_periods}')
    
    return free_periods


@tictoc
def rotors_quadratic_slowest(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_naive,
        periods_merger=merge_free_periods_naive)
    

@tictoc
def rotors_quadratic_intermediate(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_fast,
        periods_merger=merge_free_periods_naive)


@tictoc
def rotors_quadratic_faster(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_naive,
        periods_merger=merge_free_periods_fast)


@tictoc
def rotors_nlogn(rotors: list) -> list:
    return rotors_finder(
        rotors=rotors,
        intersections_finder=find_intersections_fast,
        periods_merger=merge_free_periods_fast)
