import sys

from enums import Methods
from utils import parse_data


def main(input_path: str, output_path: str, rotors_func: object):
    with open(input_path) as i_f, open(output_path, 'w') as o_f:
        rotors: list = parse_data(i_f)
        intervals: list = rotors_func(rotors)
        o_f.write('\n'.join(intervals))


if __name__ == '__main__':
    input_path, output_path, method = 'tests/data/input_4.txt', 'tests/data/output_4.txt', 'all'  # sys.argv[1:]
    
    if method == 'all':
        for method_name, rotors_func in Methods.items():
            main(
                input_path=input_path,
                output_path=method_name.join(output_path.split('.')),
                rotors_func=rotors_func)
    else:
        main(
            input_path=input_path,
            output_path=output_path,
            rotors_func=Methods[method])    
