class color:
    def esc(number):
        return f'\u001b[{number}m'
    red = esc(41)
    blue = esc(44)
    black = esc(40)
    yellow = esc(43)
    magenta = esc(45)
    white = esc(47)
    cyan = esc(46)
    end = esc(0)