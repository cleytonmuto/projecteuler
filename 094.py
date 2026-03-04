# Project Euler 94: Almost equilateral triangles
#
# Sides (s, s, s+1) or (s, s, s-1). Valid s follow Pell-type recurrences:
#   (s,s,s+1): s_n = 14*s_{n-1} - s_{n-2} - 4
#   (s,s,s-1): s_n = 14*s_{n-1} - s_{n-2} + 4


def compute(limit=1_000_000_000):
    total = 0
    # (s, s, s+1): perimeter = 3s + 1
    p0, p1 = 1, 5
    while True:
        peri = 3 * p1 + 1
        if peri > limit:
            break
        total += peri
        p0, p1 = p1, 14 * p1 - p0 - 4

    # (s, s, s-1): perimeter = 3s - 1
    m0, m1 = 1, 17
    while True:
        peri = 3 * m1 - 1
        if peri > limit:
            break
        total += peri
        m0, m1 = m1, 14 * m1 - m0 + 4

    return str(total)


if __name__ == "__main__":
    print(compute())
