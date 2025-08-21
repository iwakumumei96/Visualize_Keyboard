class Button:
    def __init__(self, segments):
        if len(segments) == 11:
            self.keycode = segments[0].strip()
            adj = 0
        if len(segments) == 12:
            self.keycode = [segments[0].strip(), segments[1].strip()]
            adj = 1
        self.x        = float(segments[adj + 1].strip())
        self.y        = float(segments[adj + 2].strip())
        self.width    = float(segments[adj + 3].strip()) - self.x
        self.height   = float(segments[adj + 4].strip()) - self.y
        self.released = (
            int(segments[adj +  5].strip()),
            int(segments[adj +  6].strip()),
            int(segments[adj +  7].strip())
        )
        self.pressed  = (
            int(segments[adj +  8].strip()),
            int(segments[adj +  9].strip()),
            int(segments[adj + 10].strip())
        )
