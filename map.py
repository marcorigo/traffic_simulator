from car import Car

class Map:
    def __init__(self, canvas):
        self.canvas = canvas
        self.veichles = []
        self.map = [['0', '0'],
                    ['0', '0']]
                    
    def addVeichle(self):
        veichle = Car()
        veichle.model = self.canvas.create_rectangle(veichle.posx, veichle.posy, veichle.posx + veichle.width, veichle.posy + veichle.heigth, fill = 'red')
        self.veichles.append(veichle)

    def update(self):
        for veichle in self.veichles:
            veichle.move()
            self.canvas.move(veichle.model, veichle.speed, 0)