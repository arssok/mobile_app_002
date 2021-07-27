from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
from kivy.properties import Property
import random
import time

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "400")

win=False

class GameApp(App):

    def tic_tac(self, arg):
        global win
        arg.disabled = True
        arg.text = "X"

        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))

        vector = (
            [self.button[x].text for x in (0, 1, 2)],
            [self.button[x].text for x in (3, 4, 5)],
            [self.button[x].text for x in (6, 7, 8)],

            [self.button[y].text for y in (0, 3, 6)],
            [self.button[y].text for y in (1, 4, 7)],
            [self.button[y].text for y in (2, 5, 8)],

            [self.button[d].text for d in (0, 4, 8)],
            [self.button[d].text for d in (2, 4, 6)])

        win = False
        color = [0, 1, 0, 1]
        color1 =[.99, .3, .90, 1]

        for index in range(8):
            if vector[index].count('X') == 3:
                win = True
                self.a.text = str(int(self.a.text) + 1)
                for i in coordinate[index]:
                    self.button[i].color = color
                for index in range(9): # ячейки неактивны, выход
                    self.button[index].disabled = True
                    return
                break
            elif vector[index].count('O') == 3:
                win = True
                self.b.text = str(int(self.b.text) + 1)
                for i in coordinate[index]:
                    self.button[i].color = color1
                for index in range(9): # ячейки неактивны, выход
                    self.button[index].disabled = True
                    return
                break

        # Ход компьютера
        def computer_move():
            global win
            # Проверка возможности победы компьютера
            # Строки
            for i in range(0, 7, 3):
                if self.button[(i+0)].text == '' and self.button[(i+1)].text == 'O' and self.button[(i+2)].text == 'O':
                    self.button[(i+0)].text = 'O'
                    self.button[(i+0)].disabled = True
                    return
                if self.button[(i+0)].text == 'O' and self.button[(i+1)].text == '' and self.button[(i+2)].text == 'O':
                    self.button[(i+1)].text = 'O'
                    self.button[(i+1)].disabled = True
                    return
                if self.button[(i+0)].text == 'O' and self.button[(i+1)].text == 'O' and self.button[(i+2)].text == '':
                    self.button[(i+2)].text = 'O'
                    self.button[(i+2)].disabled = True
                    return
            # Столбцы
            for i in range(0, 3):
                if self.button[(i+0)].text == '' and self.button[(i+3)].text == 'O' and self.button[(i+6)].text == 'O':
                    self.button[(i+0)].text = 'O'
                    self.button[(i+0)].disabled = True
                    return
                if self.button[(i+0)].text == 'O' and self.button[(i+3)].text == '' and self.button[(i+6)].text == 'O':
                    self.button[(i+3)].text = 'O'
                    self.button[(i+3)].disabled = True
                    return
                if self.button[(i+0)].text == 'O' and self.button[(i+3)].text == 'O' and self.button[(i+6)].text == '':
                    self.button[(i+6)].text = 'O'
                    self.button[(i+6)].disabled = True
                    return

            # Диагонали
            if self.button[0].text == '' and self.button[4].text == 'O' and self.button[8].text == 'O':
                self.button[0].text = 'O'
                self.button[0].disabled = True
                return
            if self.button[0].text == 'O' and self.button[4].text == '' and self.button[8].text == 'O':
                self.button[4].text = 'O'
                self.button[4].disabled = True
                return
            if self.button[0].text == 'O' and self.button[4].text == 'O' and self.button[8].text == '':
                self.button[8].text = 'O'
                self.button[8].disabled = True
                return

            if self.button[2].text == '' and self.button[4].text == 'O' and self.button[6].text == 'O':
                self.button[2].text = 'O'
                self.button[2].disabled = True
                return
            if self.button[2].text == 'O' and self.button[4].text == '' and self.button[6].text == 'O':
                self.button[4].text = 'O'
                self.button[4].disabled = True
                return
            if self.button[2].text == 'O' and self.button[4].text == 'O' and self.button[6].text == '':
                self.button[6].text = 'O'
                self.button[6].disabled = True
                return

            # Проверка возможности победы игрока
            # Строки
            for ii in range(0,7,3):
                if self.button[(ii)].text=='' and self.button[(ii+1)].text=='X' and self.button[(ii+2)].text=='X':
                    self.button[(ii)].text = 'O'
                    self.button[(ii)].disabled = True
                    return
                if self.button[(ii)].text=='X' and self.button[(ii+1)].text=='' and self.button[(ii+2)].text=='X':
                    self.button[(ii+1)].text = 'O'
                    self.button[(ii+1)].disabled = True
                    return
                if self.button[(ii+0)].text=='X' and self.button[(ii+1)].text=='X' and self.button[(ii+2)].text=='':
                    self.button[(ii+2)].text = 'O'
                    self.button[(ii+2)].disabled = True
                    return
            # Столбцы
            for ii in range(0,3):
                if self.button[(ii+0)].text=='' and self.button[(ii+3)].text=='X' and self.button[(ii+6)].text=='X':
                    self.button[(ii+0)].text = 'O'
                    self.button[(ii+0)].disabled = True
                    return
                if self.button[(ii+0)].text=='X' and self.button[(ii+3)].text=='' and self.button[(ii+6)].text=='X':
                    self.button[(ii+3)].text = 'O'
                    self.button[(ii+3)].disabled = True
                    return
                if self.button[(ii+0)].text=='X' and self.button[(ii+3)].text=='X' and self.button[(ii+6)].text=='':
                    self.button[(ii+6)].text = 'O'
                    self.button[(ii+6)].disabled = True
                    return

            # Диагонали
            if self.button[0].text == '' and self.button[4].text == 'X' and self.button[8].text == 'X':
                self.button[0].text = 'O'
                self.button[0].disabled = True
                return
            if self.button[0].text == 'X' and self.button[4].text == '' and self.button[8].text == 'X':
                self.button[4].text = 'O'
                self.button[4].disabled = True
                return
            if self.button[0].text=='X' and self.button[4].text=='X' and self.button[8].text =='':
                self.button[8].text = 'O'
                self.button[8].disabled = True
                return

            if self.button[2].text == '' and self.button[4].text == 'X' and self.button[6].text == 'X':
                self.button[2].text = 'O'
                self.button[2].disabled = True
                return
            if self.button[2].text == 'X' and self.button[4].text == '' and self.button[6].text == 'X':
                self.button[4].text = 'O'
                self.button[4].disabled = True
                return
            if self.button[2].text=='X' and self.button[4].text=='X' and self.button[6].text =='':
                self.button[6].text = 'O'
                self.button[6].disabled = True
                return


            # Пробуем занять центр, если он свободен.
            if not win and self.button[4].text == '':
                self.button[4].text = 'O'
                self.button[4].disabled = True
                return

            # Пробуем занять один из углов, если есть свободные.
            if not win and self.button[0].text == '':
                self.button[0].text = 'O'
                self.button[0].disabled = True
                return
            elif not win and self.button[2].text == '':
                self.button[2].text = 'O'
                self.button[2].disabled = True
                return
            elif not win and self.button[6].text == '':
                self.button[6].text = 'O'
                self.button[6].disabled = True
                return
            elif not win and self.button[8].text == '':
                self.button[8].text = 'O'
                self.button[8].disabled = True
                return

            # Случайный ход - делаем ход по одной стороне.
            ran_new = [1,3,5,7]
            ran = random.sample(ran_new,4)
            for ii in ran:
                if self.button[ii].text == '' and not win:
                    self.button[ii].text = 'O'
                    self.button[ii].disabled = True
                    break
                if win:
                    break
            return

        computer_move()

        vector = (
            [self.button[x].text for x in (0, 1, 2)],
            [self.button[x].text for x in (3, 4, 5)],
            [self.button[x].text for x in (6, 7, 8)],

            [self.button[y].text for y in (0, 3, 6)],
            [self.button[y].text for y in (1, 4, 7)],
            [self.button[y].text for y in (2, 5, 8)],

            [self.button[d].text for d in (0, 4, 8)],
            [self.button[d].text for d in (2, 4, 6)])

        for index in range(8):
            if vector[index].count('O') == 3:
                win = True
                self.b.text = str(int(self.b.text) + 1)
                for i in coordinate[index]:
                    self.button[i].color = color1
                break

        if win:
            for index in range(9):
                self.button[index].disabled = True

    # Продолжим
    def restart(self, arg):
        global switch, turn
        switch = 0
        for index in range(9):
            self.button[index].color = [.9, .9, .9, 1]
            self.button[index].text = ""
            self.button[index].disabled = False
        # Случайный выбор игрока, который ходит первым.
        if random.randint(0, 1) == 0:
            kk=random.randint(0,8)
            self.button[kk].text = "O"
            self.button[kk].disabled = True

    # Новая игра
    def new_game(self, arg):
        self.a.text = "0"
        self.b.text = "0"
        global switch, turn
        switch = 0
        for index in range(9):
            self.button[index].color = [.9, .9, .9, 1]
            self.button[index].text = ""
            self.button[index].disabled = False
        # Случайный выбор игрока, который ходит первым.
        if random.randint(0, 1) == 0:
            kk=random.randint(0,8)
            self.button[kk].text = "O"
            self.button[kk].disabled = True

    # Построение игрового поля
    def build(self):
        self.title = "X - O"

        root = BoxLayout(orientation='vertical', padding=10)
        grid = GridLayout(cols=3, spacing=10)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(text='',
                                        disabled_color=[0, 0, 1, 1],
                                        font_size=90,
                                        disabled=False,
#                                        background_normal='atlas: // data / images / defaulttheme / player-background',
                                        background_color=[0.0,0.5,0.5,1],
                                        #background_disabled_down='atlas: // data / images / defaulttheme / splitter',
                                        background_disabled_normal='atlas: // data / images / defaulttheme / vkeyboard_background',
                                        border=(10,0,0,10),
                                        on_press=self.tic_tac)
            grid.add_widget(self.button[index])

        lbls = BoxLayout(orientation="horizontal", size_hint=(1, .11))
        self.a = Label(text="0", size_hint=(1, 0.9), font_size=40, color = [0, 1, 0, 1] )
        self.b = Label(text="0", size_hint=(1, 0.9), font_size=40, color = [.99, .3, .90, 1])
        lbls.add_widget(self.a)
        lbls.add_widget(self.b)

        root.add_widget(grid)
        root.add_widget(Label(text='',size_hint=(1,.02)))
        root.add_widget(Button(text="Продолжим?", size_hint=[1, .1],color = [0, 1, 1, 1], on_press=self.restart))
        root.add_widget(Button(text="Новая игра!", size_hint=[1, .1],color = [1, 1, 0, 1], on_press=self.new_game))
        root.add_widget(lbls)
        return root


if __name__ == '__main__':
    GameApp().run()