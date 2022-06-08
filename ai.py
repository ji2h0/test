from random import randint


class AI:

    def __init__(self, shape):
        self.shape = shape

    def move(self, b, re):
        possible_moves = [(x, y) for x in range(3) for y in range(3) if b[x][y] == 0]
        corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
        check_all_lines = [sum(b[0]), sum(b[1]), sum(b[2]), b[0][0] + b[1][0] + b[2][0],
                           b[0][1] + b[1][1] + b[2][1], b[0][2] + b[1][2] + b[2][2],
                           b[0][0] + b[1][1] + b[2][2], b[2][0] + b[1][1] + b[0][2]]

        def opening():
            if self.shape == 'X':
                if len(re) == 0:
                    return corner[randint(0, 3)]
                if len(re) == 2:
                    if re[1] == [1, 1]:
                        good_pos = []
                        if re[0] == [0, 0]:
                            good_pos = [(2, 2), (1, 2), (2, 1)]
                        if re[0] == [0, 2]:
                            good_pos = [(2, 0), (1, 0), (2, 1)]
                        if re[0] == [2, 2]:
                            good_pos = [(0, 0), (0, 1), (1, 0)]
                        if re[0] == [2, 0]:
                            good_pos = [(0, 2), (0, 1), (1, 2)]
                        return good_pos[randint(0, 2)]
                    best = []
                    for i in corner:
                        if i[0] != re[1][0] and i[1] != re[1][1] and (i[0] == re[0][0] or i[1] == re[0][1]):
                            best.append(i)
                    r = list(set(best).intersection(possible_moves))
                    if r:
                        return r[0]
                    else:
                        return list(set(corner).intersection(possible_moves))[randint(0, 1)]
            else:
                if len(re) == 1:
                    if re[0] == [1, 1]:
                        return corner[randint(0, 3)]
                    else:
                        return 1, 1

        def winning_position():
            win_pos = []
            if self.shape == 'X':
                typ = 2
            else:
                typ = 20
            for i in range(8):
                if check_all_lines[i] == typ:
                    if i == 0:
                        win_pos = [(0, 0), (0, 1), (0, 2)]
                    if i == 1:
                        win_pos = [(1, 0), (1, 1), (1, 2)]
                    if i == 2:
                        win_pos = [(2, 0), (2, 1), (2, 2)]
                    if i == 3:
                        win_pos = [(0, 0), (1, 0), (2, 0)]
                    if i == 4:
                        win_pos = [(0, 1), (1, 1), (2, 1)]
                    if i == 5:
                        win_pos = [(0, 2), (1, 2), (2, 2)]
                    if i == 6:
                        win_pos = [(0, 0), (1, 1), (2, 2)]
                    if i == 7:
                        win_pos = [(2, 0), (1, 1), (0, 2)]
                    return list(set(win_pos).intersection(possible_moves))[0]

        def losing_position():
            lose_pos = []
            if self.shape == 'X':
                typ = 20
            else:
                typ = 2
            for i in range(8):
                if check_all_lines[i] == typ:
                    if i == 0:
                        lose_pos = [(0, 0), (0, 1), (0, 2)]
                    if i == 1:
                        lose_pos = [(1, 0), (1, 1), (1, 2)]
                    if i == 2:
                        lose_pos = [(2, 0), (2, 1), (2, 2)]
                    if i == 3:
                        lose_pos = [(0, 0), (1, 0), (2, 0)]
                    if i == 4:
                        lose_pos = [(0, 1), (1, 1), (2, 1)]
                    if i == 5:
                        lose_pos = [(0, 2), (1, 2), (2, 2)]
                    if i == 6:
                        lose_pos = [(0, 0), (1, 1), (2, 2)]
                    if i == 7:
                        lose_pos = [(2, 0), (1, 1), (0, 2)]
                    return list(set(lose_pos).intersection(possible_moves))[0]

        def defend_move():
            weak_pos = []
            critical_pos = []
            if self.shape == 'X':
                typ = 10
            else:
                typ = 1
            for i in range(8):
                if check_all_lines[i] == typ:
                    if i == 0:
                        weak_pos.append((0, 0))
                        weak_pos.append((0, 1))
                        weak_pos.append((0, 2))
                    if i == 1:
                        weak_pos.append((1, 0))
                        weak_pos.append((1, 1))
                        weak_pos.append((1, 2))
                    if i == 2:
                        weak_pos.append((2, 0))
                        weak_pos.append((2, 1))
                        weak_pos.append((2, 2))
                    if i == 3:
                        weak_pos.append((0, 0))
                        weak_pos.append((1, 0))
                        weak_pos.append((2, 0))
                    if i == 4:
                        weak_pos.append((0, 1))
                        weak_pos.append((1, 1))
                        weak_pos.append((2, 1))
                    if i == 5:
                        weak_pos.append((0, 2))
                        weak_pos.append((1, 2))
                        weak_pos.append((2, 2))
                    if i == 6:
                        weak_pos.append((0, 0))
                        weak_pos.append((1, 1))
                        weak_pos.append((2, 2))
                    if i == 7:
                        weak_pos.append((2, 0))
                        weak_pos.append((1, 1))
                        weak_pos.append((0, 2))
            check = list(set(weak_pos).intersection(possible_moves))
            if check:
                m = 0
                for i in check:
                    k = weak_pos.count(i)
                    if k > m:
                        m = k
                for i in check:
                    if weak_pos.count(i) == m:
                        critical_pos.append(i)
                if len(critical_pos) == 1:
                    return critical_pos[0]
                else:
                    t = list(x for x in possible_moves if x not in critical_pos)
                    return t[randint(0, len(t) - 1)]

        def attack_move():
            good_pos = []
            best_pos = []
            if self.shape == 'X':
                typ = 1
            else:
                typ = 10
            for i in range(8):
                if check_all_lines[i] == typ:
                    if i == 0:
                        good_pos.append((0, 0))
                        good_pos.append((0, 1))
                        good_pos.append((0, 2))
                    if i == 1:
                        good_pos.append((1, 0))
                        good_pos.append((1, 1))
                        good_pos.append((1, 2))
                    if i == 2:
                        good_pos.append((2, 0))
                        good_pos.append((2, 1))
                        good_pos.append((2, 2))
                    if i == 3:
                        good_pos.append((0, 0))
                        good_pos.append((1, 0))
                        good_pos.append((2, 0))
                    if i == 4:
                        good_pos.append((0, 1))
                        good_pos.append((1, 1))
                        good_pos.append((2, 1))
                    if i == 5:
                        good_pos.append((0, 2))
                        good_pos.append((1, 2))
                        good_pos.append((2, 2))
                    if i == 6:
                        good_pos.append((0, 0))
                        good_pos.append((1, 1))
                        good_pos.append((2, 2))
                    if i == 7:
                        good_pos.append((2, 0))
                        good_pos.append((1, 1))
                        good_pos.append((0, 2))
            check = list(set(good_pos).intersection(possible_moves))
            if check:
                m = 0
                for i in check:
                    k = good_pos.count(i)
                    if k > m:
                        m = k
                for i in check:
                    if good_pos.count(i) == m:
                        best_pos.append(i)
                return best_pos[randint(0, len(best_pos) - 1)]

        def random_ai():
            return possible_moves[randint(0, len(possible_moves) - 1)]

        return opening() or \
               winning_position() or \
               losing_position() or \
               defend_move() or \
               attack_move() or \
               random_ai()
