import Constans as const


class Button:
    def __init__(self, x, y, content=""):
        self.width = 200
        self.height = 200
        self.x = x
        self.y = y
        self.sign = const.EMPTY
        self.content = content

    def draw(self, win):
        win.blit(self.sign, (self.x, self.y))

    def set_content(self, content):
        if content == "":
            self.sign = const.EMPTY
            self.content = ""
        elif content == 'X':
            self.sign = const.THUNDER
            self.content = "X"
        elif content == "O":
            self.sign = const.HEART
            self.content = "O"

    def if_clicked(self, mouse_pos):
        return mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width and mouse_pos[1] >= self.y and mouse_pos[
            1] <= self.y + self.height
