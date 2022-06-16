from random import choice


class AI:

    def __init__(self, shape):
        self.shape = shape

    def outcome(self, b):
        check_all_lines = [sum(b[0]), sum(b[1]), sum(b[2]), b[0][0] + b[1][0] + b[2][0],
                           b[0][1] + b[1][1] + b[2][1], b[0][2] + b[1][2] + b[2][2],
                           b[0][0] + b[1][1] + b[2][2], b[2][0] + b[1][1] + b[0][2]]
        if self.shape == 'O':
            v = 3
            d = 30
        else:
            v = 30
            d = 3
        for i in range(8):
            if check_all_lines[i] == d:  # 유저 입장에서의 승패
                return 'Defeat'
            if check_all_lines[i] == v:
                return 'Victory'
        for i in b:
            for j in i:
                if j == 0:
                    return None
        return 'Draw'

    def move(self, d, re):
        b = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        possible = [(x, y) for x in range(3) for y in range(3) if d[x][y] == 0]
        corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
        check_all_lines = [sum(d[0]), sum(d[1]), sum(d[2]), d[0][0] + d[1][0] + d[2][0],
                           d[0][1] + d[1][1] + d[2][1], d[0][2] + d[1][2] + d[2][2],
                           d[0][0] + d[1][1] + d[2][2], d[2][0] + d[1][1] + d[0][2]]

        def opening():
            if self.shape == 'X':
                if len(re) == 0:
                    return choice(corner)
                if len(re) == 2:
                    if re[1] == b[4]:
                        good = []
                        if re[0] == b[0]:
                            good = [b[5], b[7], b[8]]
                        if re[0] == b[2]:
                            good = [(2, 0), (1, 0), (2, 1)]
                        if re[0] == b[8]:
                            good = [(0, 0), (0, 1), (1, 0)]
                        if re[0] == b[6]:
                            good = [(0, 2), (0, 1), (1, 2)]
                        return choice(good)
                    best = []
                    for i in corner:
                        if i[0] != re[1][0] and i[1] != re[1][1] and (i[0] == re[0][0] or i[1] == re[0][1]):
                            best.append(i)
                    r = list(set(best).intersection(possible))
                    if r:
                        return choice(r)
                    else:
                        return choice(list(set(corner).intersection(possible)))
            else:
                if len(re) == 1:
                    if re[0] == (1, 1):
                        return choice(corner)
                    else:
                        return 1, 1

        def winning():
            win = []
            if self.shape == 'X':
                c = 2
            else:
                c = 20
            for i in range(8):
                if check_all_lines[i] == c:
                    if i == 0:
                        win = [b[0], b[1], b[2]]
                    if i == 1:
                        win = [b[3], b[4], b[5]]
                    if i == 2:
                        win = [b[6], b[7], b[8]]
                    if i == 3:
                        win = [b[0], b[3], b[6]]
                    if i == 4:
                        win = [b[1], b[4], b[7]]
                    if i == 5:
                        win = [b[2], b[5], b[8]]
                    if i == 6:
                        win = [b[0], b[4], b[8]]
                    if i == 7:
                        win = [b[2], b[4], b[6]]
                    return choice(list(set(win).intersection(possible)))

        def losing():
            lose = []
            if self.shape == 'X':
                typ = 20
            else:
                typ = 2
            for i in range(8):
                if check_all_lines[i] == typ:
                    if i == 0:
                        lose = [b[0], b[1], b[2]]
                    if i == 1:
                        lose = [b[3], b[4], b[5]]
                    if i == 2:
                        lose = [b[6], b[7], b[8]]
                    if i == 3:
                        lose = [b[0], b[3], b[6]]
                    if i == 4:
                        lose = [b[1], b[4], b[7]]
                    if i == 5:
                        lose = [b[2], b[5], b[8]]
                    if i == 6:
                        lose = [b[0], b[4], b[8]]
                    if i == 7:
                        lose = [b[2], b[4], b[6]]
                    return choice(list(set(lose).intersection(possible)))

        def attack():
            good = []
            best = []
            if self.shape == 'X':
                c = 1
            else:
                c = 10
            for i in range(8):
                if check_all_lines[i] == c:
                    if i == 0:
                        good.append(b[0])
                        good.append(b[1])
                        good.append(b[2])
                    if i == 1:
                        good.append(b[3])
                        good.append(b[4])
                        good.append(b[5])
                    if i == 2:
                        good.append(b[6])
                        good.append(b[7])
                        good.append(b[8])
                    if i == 3:
                        good.append(b[0])
                        good.append(b[3])
                        good.append(b[6])
                    if i == 4:
                        good.append(b[1])
                        good.append(b[4])
                        good.append(b[7])
                    if i == 5:
                        good.append(b[2])
                        good.append(b[5])
                        good.append(b[8])
                    if i == 6:
                        good.append(b[0])
                        good.append(b[4])
                        good.append(b[8])
                    if i == 7:
                        good.append(b[2])
                        good.append(b[4])
                        good.append(b[6])
            check = list(set(good).intersection(possible))
            if check:
                m = 0
                for i in check:
                    k = good.count(i)
                    if k > m:
                        m = k
                if m > 1:
                    for i in check:
                        if good.count(i) == m:
                            best.append(i)
                    return choice(best)

        def defend():
            weak = []
            critical = []
            if self.shape == 'X':
                c = 10
            else:
                c = 1
            for i in range(8):
                if check_all_lines[i] == c:
                    if i == 0:
                        weak.append(b[0])
                        weak.append(b[1])
                        weak.append(b[2])
                    if i == 1:
                        weak.append(b[3])
                        weak.append(b[4])
                        weak.append(b[5])
                    if i == 2:
                        weak.append(b[6])
                        weak.append(b[7])
                        weak.append(b[8])
                    if i == 3:
                        weak.append(b[0])
                        weak.append(b[3])
                        weak.append(b[6])
                    if i == 4:
                        weak.append(b[1])
                        weak.append(b[4])
                        weak.append(b[7])
                    if i == 5:
                        weak.append(b[2])
                        weak.append(b[5])
                        weak.append(b[8])
                    if i == 6:
                        weak.append(b[0])
                        weak.append(b[4])
                        weak.append(b[8])
                    if i == 7:
                        weak.append(b[2])
                        weak.append(b[4])
                        weak.append(b[6])
            check = list(set(weak).intersection(possible))
            if check:
                m = 0
                for i in check:
                    k = weak.count(i)
                    if k > m:
                        m = k
                if m > 1:
                    for i in check:
                        if weak.count(i) == m:
                            critical.append(i)
                    return choice(critical)

        def random():
            return choice(possible)

        return opening() or \
               winning() or \
               losing() or \
               attack() or \
               defend() or \
               random()
