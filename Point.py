class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def setX(self, x):
        self.__x = x
    def getX(self):
        return self.__x
    
    def setY(self, y):
        self.__y = y
    def getY(self):
        return self.__y
    
    
    def membre_deplace(self, dx, dy):
        self.setX(self.getX() + dx)  
        self.setY(self.getY() + dy)