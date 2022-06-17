from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from ai import AI

fontName = 'Dongle-Light.ttf' # 폰트 설정
Window.clearcolor = (204/255, 204/255, 1) # 바탕색 설정

SHAPES = ('X', 'O')


who_win = [0, 0] # 승패 기록 리스트
data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # 보드의 상태 기록 리스트
re = [] # 몇 수에 어디뒀는지 기록하는 리스트


def turn_generator(): # 턴 제너레이터
    while 1:
        for shape in SHAPES:
            yield shape


def first_generator(): # 유저가 O, X를 번갈아가며 하게 하는 제너레이터
    while 1:
        for first in (0, 1):
            yield first


class Board(GridLayout):

    shapes = None
    grid = None

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.padding = [0, Window.height / 6, 0, Window.height / 6]
        self.spacing = [Window.width / 150, Window.width / 150]

        self.cols = 3
        self.rows = 3
        self.shapes = turn_generator()
        self.first = first_generator()

        self.grid = [[Button() for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_tiles()
        self.initial_player()

    def initial_player(self):
        self.bot = AI(SHAPES[next(self.first)]) # 봇이 X할지 O할지 제너레이터에서 가져옴

        if self.bot.shape == 'X': # 봇이 X일 경우 봇이 먼저 첫 수를 둠
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            self.grid[y][x].font_size = Window.height / 6.1
            self.grid[y][x].color = (25/255, 25/255, 25/255)
            data[x][y] = 1
            re.append((x, y))

    def draw_tiles(self): # 9개의 버튼 중 무엇이 눌렸는지에 따라 다른 역할 수행

        tile1 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile1.bind(on_press=self.pressed1)
        self.grid[0][0] = tile1
        self.add_widget(tile1)

        tile2 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile2.bind(on_press=self.pressed2)
        self.grid[1][0] = tile2
        self.add_widget(tile2)

        tile3 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile3.bind(on_press=self.pressed3)
        self.grid[2][0] = tile3
        self.add_widget(tile3)

        tile4 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile4.bind(on_press=self.pressed4)
        self.grid[0][1] = tile4
        self.add_widget(tile4)

        tile5 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile5.bind(on_press=self.pressed5)
        self.grid[1][1] = tile5
        self.add_widget(tile5)

        tile6 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile6.bind(on_press=self.pressed6)
        self.grid[2][1] = tile6
        self.add_widget(tile6)

        tile7 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile7.bind(on_press=self.pressed7)
        self.grid[0][2] = tile7
        self.add_widget(tile7)

        tile8 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile8.bind(on_press=self.pressed8)
        self.grid[1][2] = tile8
        self.add_widget(tile8)

        tile9 = Button(background_normal='', background_color=(153/255, 153/255, 1),
                       font_size=Window.height / 6.1, font_name=fontName)
        tile9.bind(on_press=self.pressed9)
        self.grid[2][2] = tile9
        self.add_widget(tile9)

    def pressed1(self, instance): # 눌린 버튼의 위치에 따라 data 값을 변경해주고 re에 추가해줌
        if instance.text:
            return None
        re.append((0, 0))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][0] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[0][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished(): # 게임이 안 끝났다면 move 함수에서 리턴해온 값을 data에 반영해주고 re에 추가함
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished() # 게임이 끝났는지 확인함

    def pressed2(self, instance):
        if instance.text:
            return None
        re.append((0, 1))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][1] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[0][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed3(self, instance):
        if instance.text:
            return None
        re.append((0, 2))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[0][2] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[0][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed4(self, instance):
        if instance.text:
            return None
        re.append((1, 0))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][0] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[1][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed5(self, instance):
        if instance.text:
            return None
        re.append((1, 1))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][1] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[1][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed6(self, instance):
        if instance.text:
            return None
        re.append((1, 2))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[1][2] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[1][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed7(self, instance):
        if instance.text:
            return None
        re.append((2, 0))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][0] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[2][0] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220/255, 220/255, 220/255)
            self.is_finished()

    def pressed8(self, instance):
        if instance.text:
            return None
        re.append((2, 1))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][1] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[2][1] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220 / 255, 220 / 255, 220 / 255)
            self.is_finished()

    def pressed9(self, instance):
        if instance.text:
            return None
        re.append((2, 2))
        instance.text = next(self.shapes)
        if instance.text == 'X':
            data[2][2] = 1
            instance.color = (25/255, 25/255, 25/255)
        else:
            data[2][2] = 10
            instance.color = (220/255, 220/255, 220/255)

        if not self.is_finished():
            (x, y) = self.bot.move(data, re)
            self.grid[y][x].text = next(self.shapes)
            re.append((x, y))
            if self.grid[y][x].text == 'X':
                data[x][y] = 1
                self.grid[y][x].color = (25/255, 25/255, 25/255)
            else:
                data[x][y] = 10
                self.grid[y][x].color = (220 / 255, 220 / 255, 220 / 255)
            self.is_finished()

    def is_finished(self):

        outcome = self.bot.outcome(data)

        if outcome == 'Defeat': # outcome 함수의 리턴값에 따라 who_win에 변경 값(누가 이겼는지) 반영
            who_win[1] += 1
        elif outcome == 'Victory':
            who_win[0] += 1

        if outcome:
            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='     %s\nYou : %d  AI : %d' % (outcome, who_win[0], who_win[1]), font_name=fontName, font_size=50))
            close_button = Button(text='Play Again', font_name=fontName, font_size=50)
            content.add_widget(close_button)

            popup = Popup(title='Game Over', content=content, auto_dismiss=False,
                          size_hint=(.4, .4))
            popup.open()
            close_button.bind(on_release=lambda *args: self.restart_board(popup, *args)) # restart_board 함수 호출
            return True
        else:
            return False

    def restart_board(self, *args): # re, data, grid 등을 초기 상태로 변경하고 다음 게임이 X부터 시작하도록 필요한 만큼(1번 or 2번) 턴 제너레이터 호출
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


class TicTacToe(App):

    def build(self):

        self.board = Board()
        return self.board


if __name__ == '__main__':
    TicTacToe().run()
