import time


def parse_data(f) -> list:
    rotors = list()
    
    for line in f:
        centroid_x, centroid_y = line.split()
        rotors.append((float(centroid_x), float(centroid_y)))

    return rotors


def tictoc(func: object, *args, **kwargs) -> object:
    def _func(*args, **kwargs):
        s: int = time.time()
        result: object = func(*args, **kwargs)
        e: int = time.time()
        print(f'Terminated {func.__name__} in {e - s}s')

        return result

    return _func
