from libqtile import bar
from libqtile.widget import base

class QuickExit(base._TextBox):
    """
    A button of exiting the running qtile easily. When clicked this button, a countdown
    start. If the button pushed with in the countdown again, the qtile shutdown.
    """

    defaults = [
        ('default_text', '[ shutdown ]', 'A text displayed as a button'),
        ('countdown_format', '[ {} seconds ]', 'This text is showed when counting down.'),
        ('timer_interval', 1, 'A countdown interval.'),
        ('countdown_start', 5, 'Time to accept the second pushing.'),
    ]

    def __init__(self, widget=bar.CALCULATED, **config):
        base._TextBox.__init__(self, '', widget, **config)
        self.add_defaults(QuickExit.defaults)

        self.is_counting = False
        self.text = self.default_text
        self.countdown = self.countdown_start
        self.__call_later_funcs = []

        self.add_callbacks({'Button1': self.cmd_trigger})

    def __reset(self):
        self.is_counting = False
        self.countdown = self.countdown_start
        self.text = self.default_text
        for f in self.__call_later_funcs:
            f.cancel()

    def update(self):
        if not self.is_counting:
            return

        self.countdown -= 1
        self.text = self.countdown_format.format(self.countdown)
        self.timeout_add(self.timer_interval, self.update)
        self.__call_later_funcs.append(self.future)
        self.draw()

        if self.countdown == 0:
            self.qtile.stop()
            return

    def cmd_trigger(self):
        if not self.is_counting:
            self.is_counting = True
            self.update()
        else:
            self.__reset()
            self.draw()

def __init__(self, widget=bar.CALCULATED, **config):
    self.qtile.stop()

qtile.stop()
