
class Player():
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed

    def name(self):
        return self.name

    def health(self):
        return self.health

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
