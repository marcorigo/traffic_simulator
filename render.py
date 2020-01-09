class RenderEngine:
    def __init__(self, canvas, pygame, width, height):
        self.pygame = pygame
        self.canvas = canvas
        self.width = width
        self.height = height
        self.car = self.pygame.image.load('car.png').convert_alpha()
        self.truck = self.pygame.image.load('truck.png')

    def drawVeichle(self, veichle_name, x, y, width, height, angle, fvW, fvH):
        veichle = None
        if veichle_name == 'car':
            veichle = self.pygame.transform.scale(self.car, (width, height))
            self.car = veichle
        if veichle_name == 'truck':
            veichle = self.pygame.transform.scale(self.truck, (width, height))
            self.truck = veichle
        image_orig = veichle.convert().convert_alpha()
        image = image_orig.copy()

        rect = image.get_rect()  
        rect.center = ( x + (width // 2) , y + ( height // 2))   
        old_center = rect.center  
        rot = angle
        new_image = self.pygame.transform.rotate(image_orig , rot)  
        rect = new_image.get_rect()  
        rect.center = old_center   
        self.canvas.blit(new_image , rect)  

    def drawRect(self, x, y, width, height, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, height))

    def drawCircle(self, x, y, radius, color):
        self.pygame.draw.circle(self.canvas, color, (int(x), int(y)), int(radius))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
