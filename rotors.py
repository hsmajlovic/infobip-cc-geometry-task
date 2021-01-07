import sys

from algorithms.interface import Methods
from utils import parse_data


def main(input_path: str, output_path: str, rotors_func: object):
    with open(input_path) as i_f, open(output_path, 'w') as o_f:
        rotors: list = parse_data(i_f)
        intervals: list = rotors_func(rotors)
        o_f.write('\n'.join([' '.join([str(e) for e in interval]) for interval in intervals]))


if __name__ == '__main__':
    input_path, output_path, method = sys.argv[1:]
    
    if method == 'all':
        for method_name, rotors_func in Methods.items():
            main(
                input_path=input_path,
                output_path=f'_{method_name}.'.join(output_path.split('.')),
                rotors_func=rotors_func)
    else:
        try:
            main(
                input_path=input_path,
                output_path=output_path,
                rotors_func=Methods[method])
        except KeyError as e:
            print(f'No method {e} present. Try any of the following:\n', '\n'.join(list(Methods)))
