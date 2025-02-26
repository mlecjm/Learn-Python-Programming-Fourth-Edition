# profiling/triples_v3.py
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if hypotenuse.is_integer():
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_hypotenuse(a, b):
    return (a * a + b * b) ** 0.5


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples_v3.py
         1002038 function calls in 0.287 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.287    0.287 {built-in method builtins.exec}
        1    0.000    0.000    0.287    0.287 triples_v3.py:1(<module>)
        1    0.143    0.143    0.287    0.287 triples_v3.py:1(calc_triples)
   500500    0.084    0.000    0.084    0.000 triples_v3.py:11(calc_hypotenuse)
   500500    0.060    0.000    0.060    0.000 {method 'is_integer' of 'float' objects}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
