from colorama import Fore, Style, init

init()


class Colorizer:
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'reset': Style.RESET_ALL
    }

    def __init__(self, color):
        self.color_code = self.colors[color]

    def __enter__(self):
        print(self.color_code, end='')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Style.RESET_ALL, end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with Colorizer('red'):
    print('printed in red')
print('printed in default color')
