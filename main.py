import pyglet
from Keyboard_Module import Keyboard_Module as Key
from Scripts import Scripts

def main():
    scripts = Scripts.Scripts()
    window = pyglet.window.Window(scripts.screen_x, scripts.screen_y, caption = "Visualize Keyboard")
    keys = Key.Keyboard_Module(window, scripts.GetKeycodes())
    scripts.SetBGcolor()
    rects = scripts.GetRects()

    # ESC無効化
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            return True
    window.push_handlers(on_key_press)

    def update(dt):
        keys.Update()
        for i1 in range(0, len(rects)):
            if keys.pressed[i1]:
                rects[i1].color = scripts.buttons[i1].pressed
            else:
                rects[i1].color = scripts.buttons[i1].released

    @window.event
    def on_draw():
        window.clear()
        for rect in rects:
            rect.draw()

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()

if __name__ == '__main__':
    main()
