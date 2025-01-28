class Ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def At(self, t):
        return self.origin + t * self.direction