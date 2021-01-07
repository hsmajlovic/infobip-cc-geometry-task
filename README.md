# infobip-cc-geometry-task
Repository contains computational geometry task that was given at Infobip Coding Challenge in January 2021.

To generate new test case:
```python3 tests/test_generator.py <test_case_size>```

To benchmark the algorithms:
```pypy rotors.py <input_test_case_path> <output_test_case_path> <method>```

Available `method` args:
  - `all`: Runs all implemented algorithms
  - `quadratic`: Runs a O(n^2) solution
  - `expected_nlogn`: Runs a expected O(nlogn) solution (worst case O(n^2))
  - `nlogn`: Runs worst case nlog(n + k) solution, where k is the number of intersections. (NOT DONE YET!)
