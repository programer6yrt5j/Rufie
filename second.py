from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty


class Seconds(Label):
    done = BooleanProperty(False)

    def __init__(self, total: int, **kwargs):
        self.current: int = 0
        self.total: int = total
        self.text = 'прошло секунд:' + str(self.current)
        super().__init__(text=self.text)

    def start(self):
        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        self.current += 1
        self.text = 'прошло секунд:' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

    def restart(self, total: int):
        self.done = False
        self.total = total
        self.current = 0
        self.text = 'прошло секунд:' + str(self.current)
        self.start
