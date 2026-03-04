# Project Euler 201: Subsets with a unique sum
#
# S = {1², 2², ..., 100²}. Find sum(U(S, 50)) where U(S, 50) = sums that occur
# in exactly one 50-element subset.
#
# DP: count[k][s] = number of ways (0, 1, or 2) to pick k elements summing to s.
# Sparse: only store achievable (k, s) pairs.


def compute():
    S = [i * i for i in range(1, 101)]
    # count[k] = dict: sum -> count (capped at 2)
    count = [{} for _ in range(51)]
    count[0][0] = 1

    for x in S:
        for k in range(50, 0, -1):
            for s, c in list(count[k - 1].items()):
                if c == 0:
                    continue
                t = s + x
                count[k][t] = min(2, count[k].get(t, 0) + c)

    return sum(s for s, c in count[50].items() if c == 1)


if __name__ == "__main__":
    print(compute())
