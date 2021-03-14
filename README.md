# Infobip Coding Challenge - Computational geometry problem
Repository contains computational geometry problem that was a candidate for Infobip Coding Challenge in January 2021.

## Problem

Given n rotating line segments of length 1m in a plane and the following constraints:
    - Each line segment kicks off its rotation from a vertical position and rotates around its lower endpoint.
    - Each line segments makes a full circle in 2pi seconds.
your goal is to find the sorted list of time intervals in radians (within a [0, 2pi] period) in which any of the segments is within the rotation circle of any other line segment.

Each segment is given as a pair of coordinates of its lower endpoint (rotation center).

Sample input:
```
0.5 0
-0.5 0
```

Sample output:
```
0.52358 2.618
3.66518 5.75959
```

Precision: `1e-5`
Expected runtime complexity: `O(nlog(n + k)`, where k is the number of intersections of rotation circles.


## For committee

To generate new test case:
```python3 tests/test_generator.py <test_case_size>```

To benchmark the algorithms:
```pypy rotors.py <input_test_case_path> <output_test_case_path> <method>```

Available `method` args:
  - `all`: Runs all implemented algorithms
  - `quadratic`: Runs a O(n^2) solution
  - `expected_nlogn`: Runs a expected O(nlogn) solution (worst case O(n^2))
  - `nlogn`: Runs worst case nlog(n + k) solution, where k is the number of intersections. (NOT DONE YET!)
