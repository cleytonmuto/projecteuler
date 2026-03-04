"""
Pell's equation x^2 - D*y^2 = 1.
For each non-square D, find the minimal positive x (and corresponding y).
Uses the continued fraction of sqrt(D) to compute the fundamental solution.
"""

import eulerlib
import fractions
import math


def sqrt_to_continued_fraction(n):
    """Returns (prefix, period) for sqrt(n). n must not be a perfect square."""
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        flr = val.floor()
        terms.append(flr)
        val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
    split = seen[val]
    return (terms[:split], terms[split:])


def minimal_x(D):
    """Returns minimal (x, y) for Pell's equation x^2 - D*y^2 = 1. D must not be a perfect square."""
    contfrac = sqrt_to_continued_fraction(D)
    temp = contfrac[0] + contfrac[1][:-1]
    val = fractions.Fraction(temp[-1], 1)
    for term in reversed(temp[:-1]):
        val = 1 / val + term
    p, q = val.numerator, val.denominator
    if len(contfrac[1]) % 2 == 0:
        return p, q
    return p * p + D * q * q, 2 * p * q


class QuadraticSurd:
    """Represents (a + b*sqrt(d))/c."""

    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()
        if c < 0:
            a, b, c = -a, -b, -c
        g = math.gcd(a, math.gcd(b, c))
        if g != 1:
            a, b, c = a // g, b // g, c // g
        self.a, self.b, self.c, self.d = a, b, c, d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d,
        )

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d,
        )

    def floor(self):
        temp = math.isqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)

    def __hash__(self):
        return hash((self.a, self.b, self.c, self.d))


def main():
    # Pell's equation: x^2 - D*y^2 = 1
    max_D = 1000
    greatest_x = 0
    spotted_D = 0
    for D in range(2, max_D + 1):
        if eulerlib.is_square(D):
            continue  # No non-trivial solution when D is a perfect square
        x, y = minimal_x(D)
        if x > greatest_x:
            greatest_x = x
            spotted_D = D
        print(f"D={D}: minimal x={x}, y={y} (x^2 - {D}*y^2 = {x*x - D*y*y})")
    print(f"Answer: D={spotted_D} produces the largest minimal x={greatest_x}")

if __name__ == "__main__":
    main()
