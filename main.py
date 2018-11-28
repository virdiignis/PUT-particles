from random import randint, random
from itertools import product

PARTICLES_COUNT = 10


class Particle:
    @staticmethod
    def __sgn__(x):
        return int(x / abs(x)) if x != 0 else 0

    def __init__(self, x, y, px, py):
        self.r = {'x': x, 'y': y}
        self.p = {'x': px, 'y': py}

    def move(self, R):
        for l in ('x', 'y'):
            self.r[l] += self.p[l]
            if abs(self.r[l]) > R:
                self.r[l] = self.__sgn__(self.r[l]) * (R - (abs(self.r[l]) % R))
                self.p[l] = -self.p[l]

    def __eq__(self, other: tuple):
        return other[0] - 1 < self.r['x'] <= other[0] and other[1] - 1 < self.r['y'] <= other[1] and other[2] - 1 < \
               self.p['x'] <= other[2] and other[3] - 1 < self.p['y'] <= other[3]

    def __str__(self):
        return "({}, {}, {}, {})".format(self.r['x'], self.r['y'], self.p['x'], self.p['y'])


class Space:
    @staticmethod
    def __rpos__(max_range):
        return (-1) ** randint(0, 1) * random() * max_range

    def __init__(self, dimension):
        self.R = 2 * dimension + 1
        self.P = dimension + 1 - (dimension % 2)
        self.dt = 1 / 2 / self.P
        self.particles = [
            Particle(random() * randint(-self.R, -self.R + 1), self.__rpos__(self.R), self.__rpos__(self.P),
                     self.__rpos__(self.P)) for _ in range(PARTICLES_COUNT)]

    def step(self):
        for p in self.particles: p.move(self.R)

    def states(self):
        for state in product(range(-self.R, self.R), range(-self.R, self.R), range(-self.P, self.P),
                             range(-self.P, self.P)):
            c = self.particles.count(state)
            if c:
                print("State ({}, {}, {}, {}): {}".format(*state, c))


if __name__ == "__main__":
    s = Space(2)
    for _ in range(10): s.step()
    s.states()
    # for p in s.particles: print(p)
