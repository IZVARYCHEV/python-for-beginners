pairs = [
    ('kitten', 'sitting'),
    ('saturday', 'sunday'),
    ('море', 'гора'),
    ('компьютер', 'компьютеризация'),
    ('компьютер', 'компьютеры'),
]

from ex2_1LevensteinDistance import LevensteinDistance
if __name__ == '__main__':
    for s, t in pairs:
        print(s, t, LevensteinDistance(s, t))