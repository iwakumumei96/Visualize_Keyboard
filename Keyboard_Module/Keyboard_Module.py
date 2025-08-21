import pyglet
import keyboard

class Keyboard_Module:
    def __init__(self, window, keycodes):
        self.keycodes  = keycodes
        self.codes_len = len(keycodes)
        
        self.active_codes = []
        self.inactive_codes = []
        for i1 in range(0, self.codes_len):
            keycode = self.keycodes[i1]
            if type(keycode) is list:
                self.active_codes.append(keycode[0])
                self.inactive_codes.append(keycode[1])
            else:
                self.active_codes.append(keycode)
                self.inactive_codes.append(keycode)

        self.pressed   = [0 for _ in range(0, self.codes_len)]
        self.active    = [0 for _ in range(0, self.codes_len)]
        self.inactive  = [0 for _ in range(0, self.codes_len)]

        self.keys = pyglet.window.key.KeyStateHandler()
        window.push_handlers(self.keys)



    def GetIndex(self, keycode):
        if keycode in self.keycodes:
            return self.keycodes.index(keycode)
        if keycode in self.active_codes:
            return self.active_codes.index(keycode)
        if keycode in self.inactive_codes:
            return self.inactive_codes.index(keycode)
        return -1

    def Update(self):
        self.UpdateActive()
        self.UpdateInacrive()
        self.UpdatePressed()

    def UpdateActive(self):
        for i1 in range(0, self.codes_len):
            try:
                if self.keys[eval("pyglet.window.key." + self.active_codes[i1])]:
                    self.active[i1] += 1
                else:
                    self.active[i1] = 0
            except:
                pass

    def UpdateInacrive(self):
        for i1 in range(0, self.codes_len):
            try:
                if keyboard.is_pressed(self.inactive_codes[i1]):
                    self.inactive[i1] += 1
                else:
                    self.inactive[i1] = 0
            except:
                pass

    def UpdatePressed(self):
        for i1 in range(0, self.codes_len):
            if self.active[i1] + self.inactive[i1]:
                self.pressed[i1] += 1
            else:
                self.pressed[i1] = 0
