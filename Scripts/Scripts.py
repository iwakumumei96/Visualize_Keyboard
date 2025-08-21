import pyglet
from Scripts import Button

class Scripts:
    def __init__(self):
        self.LoadConfigName("config.ini")
        self.LoadConfig()

    def LoadConfigName(self, path):
        f = open(path, "r")
        self.config_name = f.readline().strip()
        f.close()

    def LoadConfig(self):
        f = open("Configs/" + self.config_name + ".ini")
        lines = f.readlines()
        f.close()
        header = True
        self.buttons = []
        for line in lines:
            segments = line.split(",")
            if header:
                if len(segments) > 4:
                    self.screen_x = int(segments[0].strip())
                    self.screen_y = int(segments[1].strip())
                    self.BGcolor  = [
                        float(segments[2].strip()) / 255, 
                        float(segments[3].strip()) / 255, 
                        float(segments[4].strip()) / 255
                    ]
                else:
                    self.screen_x = 640
                    self.screen_y = 480
                    self.BGcolor  = (0, 0, 0, 1)
                header = False
            else:
                self.buttons.append(Button.Button(segments))

    def GetKeycodes(self):
        keycodes = []
        for i1 in range(0, len(self.buttons)):
            keycodes.append(self.buttons[i1].keycode)
        return keycodes
    
    def GetRects(self):
        rects = []
        for i1 in range(0, len(self.buttons)):
            rects.append(pyglet.shapes.Rectangle(
                x      = self.buttons[i1].x,
                y      = self.buttons[i1].y,
                width  = self.buttons[i1].width,
                height = self.buttons[i1].height,
                color  = self.buttons[i1].released
            ))
        return rects

    def SetBGcolor(self):
        pyglet.gl.glClearColor(self.BGcolor[0], self.BGcolor[1], self.BGcolor[2], 1)
