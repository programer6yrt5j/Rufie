from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from rufie import instructions
from ruffier import test
from second import Seconds

age = 0
name = ''
p1, p2, p3 = 0, 0, 0


def check_int(value: str):
    try:
        return int(value)
    except:
        return False


class MainScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)

        main_txt = Label(text=instructions.text1)
        name_txt = Label(text='введите имя')
        age_txt = Label(text='введите возраст')
        self.age_txt_inp: TextInput = TextInput(multiline=False)
        self.name_txt_inp: TextInput = TextInput(multiline=False)
        self.main_btn = Button(text='продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        layout_h1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        layout_h2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        layout_v = BoxLayout(orientation='vertical', padding=8, spacing=8)

        layout_h1.add_widget(name_txt)
        layout_h1.add_widget(self.name_txt_inp)

        layout_h2.add_widget(age_txt)
        layout_h2.add_widget(self.age_txt_inp)

        layout_v.add_widget(main_txt)
        layout_v.add_widget(layout_h1)
        layout_v.add_widget(layout_h2)
        layout_v.add_widget(self.main_btn)
        self.add_widget(layout_v)

        self.main_btn.on_press = self.next

    def next(self):
        global name
        global age
        name = self.name_txt_inp.text
        age = check_int(self.age_txt_inp.text)
        if age == False or age <= 7:
            age = 0
            self.age_txt_inp.text = str(age)
        else:
            self.manager.current = 'second'


class PulseScr1(Screen):
    def __init__(self, name: str):
        super().__init__(name=name)

        self.next_scr = False
        self.btn1 = Button(text='начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.text1 = Label(text=instructions.text2)
        pulse = Label(text='Введи результат:', halign='right')
        self.pulse_inp = TextInput(multiline=False)
        self.pulse_inp.set_disabled(True)
        self.timer = Seconds(1)
        self.timer.bind(done=self.finish)

        layout_h1 = BoxLayout(size_hint=(0.5, None), pos_hint={'center_x': 0.5}, height='30sp')
        layout_v = BoxLayout(orientation='vertical', padding=8, spacing=8)

        layout_h1.add_widget(pulse)
        layout_h1.add_widget(self.pulse_inp)

        layout_v.add_widget(self.text1)
        layout_v.add_widget(self.timer)
        layout_v.add_widget(layout_h1)
        layout_v.add_widget(self.btn1)
        self.add_widget(layout_v)

        self.btn1.on_press = self.next

    def next(self):
        if not self.next_scr:
            self.btn1.set_disabled(True)
            self.timer.start()
        global p1
        p1 = check_int(self.pulse_inp.text)
        if p1 == False or p1 < 0:
            p1 = 0
            self.pulse_inp.text = str(p1)
        else:
            self.manager.current = 'third'

    def finish(self, *args):
        self.btn1.set_disabled(False)
        self.pulse_inp.set_disabled(False)
        self.btn1.text = 'продолжить'
        self.next_scr = True


class TimerScr1(Screen):
    def __init__(self, name: str):
        super().__init__(name=name)

        self.btn1 = Button(text='начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.next_scr = False
        self.timer = Seconds(1)
        self.timer.bind(done=self.finish)

        self.text1 = Label(text='Выполните 30 приседаний за 45 секунд.')

        layout_v = BoxLayout(orientation='vertical', padding=8, spacing=8)

        layout_v.add_widget(self.text1)
        layout_v.add_widget(self.timer)
        layout_v.add_widget(self.btn1)
        self.add_widget(layout_v)

        self.btn1.on_press = self.next

    def next(self):
        if not self.next_scr:
            self.btn1.set_disabled(True)
            self.timer.start()
        else:
            self.manager.current = 'fourth'

    def finish(self, *args):
        self.btn1.set_disabled(False)
        self.btn1.text = 'продолжить'
        self.next_scr = True


class PulseScr2(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)

        main_txt = Label(text=instructions.text3)
        bef_result = Label(text='результат')
        aft_result_txt = Label(text='результат после отдыха')
        self.bef_result_txt_inp = TextInput(multiline=False)
        self.bef_result_txt_inp.set_disabled(True)
        self.aft_res_txt_inp = TextInput(multiline=False)
        self.aft_res_txt_inp.set_disabled(True)
        self.timer = Seconds(1)
        self.timer.bind(done=self.finish)
        self.state = 0
        self.btn1 = Button(text='продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        layout_h1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        layout_h2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        layout_v = BoxLayout(orientation='vertical', padding=8, spacing=8)

        layout_h1.add_widget(bef_result)
        layout_h1.add_widget(self.aft_res_txt_inp)

        layout_h2.add_widget(aft_result_txt)
        layout_h2.add_widget(self.bef_result_txt_inp)

        layout_v.add_widget(main_txt)
        layout_v.add_widget(self.timer)
        layout_v.add_widget(layout_h1)
        layout_v.add_widget(layout_h2)
        layout_v.add_widget(self.btn1)
        self.add_widget(layout_v)

        self.btn1.on_press = self.next

    def next(self):
        global p2, p3
        if self.state != 2:
            self.btn1.set_disabled(True)
            self.timer.restart(1)
            self.timer.start()
        else:
            p2 = check_int(self.bef_result_txt_inp.text)
            if p2 == False or p1 < 0:
                p2 = 0
                self.bef_result_txt_inp.text = str(p2)

            p3 = check_int(self.aft_res_txt_inp.text)
            if p3 == False or p1 < 0:
                p3 = 0
                self.aft_res_txt_inp.text = str(p3)
            if p2 != 0 and p3 != 0:
                self.manager.current = 'result'
        self.state += 1

    def finish(self, *args):
        if self.state == 0:
            self.btn1.text = 'продолжить'
        elif self.state == 1:
            self.aft_res_txt_inp.set_disabled(False)
        elif self.state == 2:
            self.bef_result_txt_inp.set_disabled(False)
        self.btn1.set_disabled(False)


class Result(Screen):
    def __init__(self, name: str):
        super().__init__(name=name)

        self.result_label = Label(text='это результат')

        layout_v = BoxLayout(orientation='vertical', padding=8, spacing=8)

        layout_v.add_widget(self.result_label)
        self.add_widget(layout_v)
        self.on_enter = self.show_result

    def show_result(self):
        self.result_label.text = name + '\n' + test(p1, p2, p3, age)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(PulseScr1(name='second'))
        sm.add_widget(TimerScr1(name='third'))
        sm.add_widget(PulseScr2(name='fourth'))
        sm.add_widget(Result(name='result'))
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm


app = MyApp()
app.run()
