class Planet:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = {}
        self.min_distance = float("inf")
        self.previous = None