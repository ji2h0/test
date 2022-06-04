from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from ai import AI

SHAPES = ('X', 'O')


who_win = [0, 0]
data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
re = []


def turn_generator():
    while 1:
        for shape in SHAPES:
            yield shape


def first_generator():
    while 1:
        for first in (0, 1):
            yield first


class Board(GridLayout):

    shapes = None
    grid = None

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.cols = 3
        self.rows = 3
        self.shapes = turn_generator()
        self.first = first_generator()

        self.grid = [[Button() for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_tiles()
        self.initial_player()

    def initial_player(self):
        self.bot = AI(SHAPES[next(self.first)])

        if self.bot.shape == 'X':
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            self.grid[y][x].font_size = 100
            self.grid[y][x].color = (12/255, 12/255, 12/255)
            data[x][y] = 1
            re.append([x, y])

    def draw_tiles(self):

        tile1 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile1.bind(on_press=self.pressed1)
        self.grid[0][0] = tile1
        self.add_widget(tile1)

        tile2 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile2.bind(on_press=self.pressed2)
        self.grid[1][0] = tile2
        self.add_widget(tile2)

        tile3 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile3.bind(on_press=self.pressed3)
        self.grid[2][0] = tile3
        self.add_widget(tile3)

        tile4 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile4.bind(on_press=self.pressed4)
        self.grid[0][1] = tile4
        self.add_widget(tile4)

        tile5 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile5.bind(on_press=self.pressed5)
        self.grid[1][1] = tile5
        self.add_widget(tile5)

        tile6 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile6.bind(on_press=self.pressed6)
        self.grid[2][1] = tile6
        self.add_widget(tile6)

        tile7 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile7.bind(on_press=self.pressed7)
        self.grid[0][2] = tile7
        self.add_widget(tile7)

        tile8 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile8.bind(on_press=self.pressed8)
        self.grid[1][2] = tile8
        self.add_widget(tile8)

        tile9 = Button(background_color=(0.8, 0.8, 1), font_size=100)
        tile9.bind(on_press=self.pressed9)
        self.grid[2][2] = tile9
        self.add_widget(tile9)

    def pressed1(self, instance):
        if instance.text:
            return None
        re.append([0, 0])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][0] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[0][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 0, 0):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed2(self, instance):
        if instance.text:
            return None
        re.append([0, 1])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][1] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[0][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 0, 1):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed3(self, instance):
        if instance.text:
            return None
        re.append([0, 2])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][2] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[0][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 0, 2):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed4(self, instance):
        if instance.text:
            return None
        re.append([1, 0])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][0] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[1][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 1, 0):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed5(self, instance):
        if instance.text:
            return None
        re.append([1, 1])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][1] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[1][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 1, 1):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed6(self, instance):
        if instance.text:
            return None
        re.append([1, 2])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][2] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[1][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 1, 2):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed7(self, instance):
        if instance.text:
            return None
        re.append([2, 0])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][0] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[2][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 2, 0):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12/255, 12/255, 12/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed8(self, instance):
        if instance.text:
            return None
        re.append([2, 1])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][1] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[2][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 2, 1):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12 / 255, 12 / 255, 12 / 255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220 / 255, 220 / 255, 220 / 255)
            self.is_finished(self.grid[y][x], x, y)

    def pressed9(self, instance):
        if instance.text:
            return None
        re.append([2, 2])
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][2] = 1
            instance.color = (12/255, 12/255, 12/255)
        else:
            data[2][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(instance, 2, 2):
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append([x, y])
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (12 / 255, 12 / 255, 12 / 255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220 / 255, 220 / 255, 220 / 255)
            self.is_finished(self.grid[y][x], x, y)

    def is_finished(self, instance, x, y):

        winner = self.get_winner(instance, x, y)

        if winner:
            content = BoxLayout(orientation='vertical')
            if winner == 'D':
                content.add_widget(Label(text='      Draw\nYou : %d  AI : %d' % (who_win[0], who_win[1])))
            else:
                content.add_widget(Label(text='      %s won\nYou : %d  AI : %d' % (winner, who_win[0], who_win[1])))
            close_button = Button(text='Play Again')
            content.add_widget(close_button)

            popup = Popup(title='Game Over', content=content, auto_dismiss=False,
                          size_hint=(.4, .4))
            popup.open()
            close_button.bind(on_release=lambda *args: self.restart_board(popup, *args))
            return True
        else:
            return False

    def get_winner(self, instance, x, y):
        if instance.text == 'X':
            c = 1
        else:
            c = 10
        mx = [1, 1, 0, -1, -1, -1, 0, 1]
        my = [0, 1, 1, 1, 0, -1, -1, -1]
        for _ in range(8):
            cnt = 0
            if 0 <= x + mx[_] < 3 and 0 <= y + my[_] < 3 and data[x + mx[_]][y + my[_]] == c:
                for i in range(2, -3, -1):
                    if 0 <= x + i * mx[_] < 3 and 0 <= y + i * my[_] < 3 and data[x + i * mx[_]][y + i * my[_]] == c:
                        cnt += 1
                        if cnt == 3:
                            if instance.text == self.bot.shape:
                                who_win[1] += 1
                                return 'AI'
                            else:
                                who_win[0] += 1
                                return 'You'
                    else:
                        cnt = 0
        for i in data:
            for j in i:
                if j == 0:
                    return None
        return 'D'

    def restart_board(self, *args):
        args[0].dismiss()
        re.clear()
        for i in range(3):
            for j in range(3):
                data[i][j] = 0

        for i in self.grid:
            for j in i:
                j.text = ''

        if next(self.shapes) != 'O':
            next(self.shapes)

        self.initial_player()


class Gomoku(App):

    def build(self):

        self.board = Board()
        return self.board


if __name__ == '__main__':
    Gomoku().run()