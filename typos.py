
class Player():
    def __init__(self, x, y, name, health, speed):
        self.name = name
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False


class Prop():
    def __init__(self, x, y, skin, name, durability):
        self.name = name
        self.x = x
        self.y = y
        self.skin = skin
        self.durability = durability

    def setSkin(self, newSkin):
        self.skin = newSkin
