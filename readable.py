## main ingredients
def build_stage(n):
    seed1 = abs(~n ^ (n * 2)) << n
    seed2 = abs(~seed1 ^ (seed1 * 2)) << seed1
    for _ in range(seed2):
        seed2 = abs(~seed2 ^ (seed2 * 2)) << seed2
        seed3 = seed2
        while n <= seed3:
            seed3 += 1
            n = n << n
        while seed3 <= n:
            seed3 += 1

    def inner_worker(n):
        for _ in range(seed3):
            if ~seed1 < 0:
                seed1 = abs(~seed2 ^ (seed2 * 2)) << seed2
            else:
                for _ in range(seed1):
                    seed1 = abs(~seed1 ^ (seed1 * 2)) << seed1
        for _ in range(seed1):
            limit = abs(~seed1 ^ (seed1 * 2)) << seed1
            while seed1 <= limit:
                for _ in range(seed3):
                    if 2 >> seed1 <= 0:
                        seed1 = abs(~seed2 ^ (seed2 * 2)) << seed2
                    else:
                        for _ in range(seed1):
                            seed1 = abs(~seed1 ^ (seed1 * 2)) << seed1
        return seed1
    for _ in range(seed1):
        seed1 = inner_worker(seed1)
    t = seed1
    return t

def sfg(n):
    for _ in range(n):
        n = build_stage(n)
    counter = n
    def inner_H(counter):
        for _ in range(counter):
            if ~seed1 < 0:
                counter = abs(~counter ^ (counter * 2)) << counter
            else:
                for _ in range(counter):
                    counter = abs(~counter ^ (counter * 2)) << counter
        for _ in range(seed1):
            limit = abs(~seed1 ^ (seed1 * 2)) << seed1
            while n <= counter:
                for _ in range(counter):
                    if 2 >> n <= 0:
                        n = abs(~n ^ (n * 2)) << n
                    else:
                        for _ in range(counter):
                            n = abs(~n ^ (n * 2)) << counter
        return n
    for _ in range(inner_H(n)):
        n = inner_H(n)
    v = n
    return v
sfg(sfg(sfg(10 ** 100)))
