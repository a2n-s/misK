import time
import os


#
# bars = "\\|/-"
#
# bar = 0
# while True:
#     print(bars[bar], end='\r')
#     bar = (bar + 1) % len(bars)
#     time.sleep(0.5)
#
#
# from itertools import cycle
# from time import sleep
#
# for frame in cycle(r'-\|/-\|/'):
#     print('\r', frame, sep='', end='', flush=True)
#     sleep(0.2)

class ProgressBar:
    def __init__(self, total, width=100, desc=''):
        self.total = total
        self.progress = 0
        self.width = width
        self.formats = ["{}",
                        "{:5.1f}%",
                        "{:" + str(len(str(self.total))) + "d}/{}",
                        "[{:02d}:{:02d}<{:02d}:{:02d}, {:4.2f} {}]"]

        self.desc = desc if desc == '' else desc + ':'
        self.start = time.time()
        self.times = {}

    def _inner_bar(self, progress, width):
        done = int(progress * width / 100)
        digit = int(round((progress - int(progress)) * 10, 0))
        bar = '#' * done + str('#' if digit == 10 else digit) + ' ' * (width - done - 1)
        return '[' + bar[:width] + ']'

    def _bar(self, progress):
        t = time.time() - self.start
        self.times[self.progress] = t
        pred = int(t * self.total / self.progress - t)
        t = int(t)
        speed = list(self.times.values())[-10:]
        speed = (speed[-1] - speed[0]) / len(speed)
        speed, it = (speed, "its/s") if speed >= 1 else (1 / speed, "s/it") if speed > 0 else (float("nan"), "----")
        deco_width = len(
            ' '.join([self.formats[0], self.formats[1],
                      self.formats[2], self.formats[3]]).format(self.desc, progress, self.progress, self.total,
                                                                t // 60, t % 60, pred // 60, pred % 60, speed, it))
        terminal_width, _ = os.get_terminal_size()
        width = min(self.width, terminal_width - deco_width - 3)
        bar_format = ' '.join([self.formats[0], self.formats[1],
                               self._inner_bar(progress, width),
                               self.formats[2], self.formats[3]])

        return bar_format.format(self.desc, progress, self.progress, self.total,
                                 t // 60, t % 60, pred // 60, pred % 60,
                                 speed, it)

    def __call__(self, incr=1, force=None):
        if force is None:
            self.progress += incr
        else:
            self.progress = force
        print('\r', self._bar(progress=100 * (self.progress - 1) / self.total), sep='', end='')

    def set_description(self, desc):
        self.desc = desc if desc == '' else desc + ':'

    def close(self):
        print('\r', self._bar(progress=100), sep='')


if __name__ == "__main__":
    from tqdm import tqdm, trange
    from time import sleep

    # with tqdm(total=100, ascii=True) as pbar:
    #     for i in range(100):
    #         sleep(0.1)
    #         pbar.update(1)

    # for i in trange(3, desc='1st loop'):
    #     for j in tqdm(range(100), desc='2nd loop', leave=False):
    #         sleep(0.01)

    n = 5123
    bar = ProgressBar(n, width=100)
    for i in range(n):
        sleep(0.1)
        bar(incr=1)
    bar.close()
