from leck5.задание3.задание2.ex2_1LevensteinDistance import LevensteinDistance
pairs = [
    ('kitten', 'sitting'),
    ('saturday', 'sunday'),
    ('море', 'гора'),
    ('компьютер', 'компьютеризация'),
    ('компьютер', 'компьютеры'),
]

if __name__ == '__main__':
    for s, t in pairs:
        print(s, t, LevensteinDistance(s, t))
