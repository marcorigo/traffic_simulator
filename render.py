class RenderEngine:
    def __init__(self, canvas, pygame, cell_width, width, height, font):
        self.pygame = pygame
        self.canvas = canvas
        self.cell_width = cell_width
        self.width = width
        self.height = height
        self.font = font
        self.car = self.pygame.image.load('./sprites/veichles/car1.png').convert_alpha()
        self.truck = self.pygame.image.load('./sprites/veichles/truck.png').convert_alpha()
        self.taxi = self.pygame.image.load('./sprites/veichles/taxi.png').convert_alpha()
        self.explosion = self.pygame.image.load('./sprites/explosion.png').convert_alpha()

        self.roadSprites = {
            '═':    self.pygame.image.load('./sprites/map/roadHorizontal.png').convert_alpha(), 

            '║':    self.pygame.image.load('./sprites/map/roadVertical.png').convert_alpha(),

            '╬':    self.pygame.image.load('./sprites/map/roadIntersection.png').convert_alpha(),

            '╔':    self.pygame.image.load('./sprites/map/roadCurveES.png').convert_alpha(),

            '╚':    self.pygame.image.load('./sprites/map/roadCurveNE.png').convert_alpha(),

            '╗':    self.pygame.image.load('./sprites/map/roadCurveSO.png').convert_alpha(),

            '╝':    self.pygame.image.load('./sprites/map/roadCurveNO.png').convert_alpha(),

            '➡':   self.pygame.image.load('./sprites/map/roadHorizontalSpawn2.png').convert_alpha(),

            '⬅':   self.pygame.image.load('./sprites/map/roadHorizontalSpawn4.png').convert_alpha(),

            '⬆':    self.pygame.image.load('./sprites/map/roadVerticalSpawn1.png').convert_alpha(),

            '⬇':    self.pygame.image.load('./sprites/map/roadVerticalSPawn3.png').convert_alpha(),

            '╩':    self.pygame.image.load('./sprites/map/TRoad1.png').convert_alpha(),

            '╠':    self.pygame.image.load('./sprites/map/TRoad2.png').convert_alpha(),

            '╦':    self.pygame.image.load('./sprites/map/TRoad3.png').convert_alpha(),

            '╣':    self.pygame.image.load('./sprites/map/TRoad4.png').convert_alpha(),

             0:     self.pygame.image.load('./sprites/map/grass.png').convert_alpha(),
        }

        self.resize(self.roadSprites)

    def resize(self, sprites):
        for key in sprites.keys():
            sprites[key] = self.pygame.transform.scale(sprites[key], (self.cell_width, self.cell_width))


    def drawRoadTile(self,x, y, road_type):
        roadTile = self.roadSprites[road_type]
        if roadTile:

            imagerect = roadTile.get_rect()
            imagerect.center = ( x + (self.cell_width // 2) , y + ( self.cell_width // 2))   
            self.canvas.blit(roadTile, imagerect)
            return True
        else:
            return False
    def drawVeichle(self, veichle_name, x, y, width, height, angle, fvW, fvH):
        veichle = None
        if veichle_name == 'car':
            veichle = self.pygame.transform.scale(self.car, (width, height))
            self.car = veichle
        if veichle_name == 'truck':
            veichle = self.pygame.transform.scale(self.truck, (width, height))
            self.truck = veichle
        if veichle_name == 'taxi':
            veichle = self.pygame.transform.scale(self.taxi, (width, height))
            self.taxi = veichle
        if veichle_name == 'explosion':
            veichle = self.pygame.transform.scale(self.explosion, (width, height))
            self.explosion = veichle
        image_orig = veichle
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

    def drawCircle(self, x, y, radius, color, border_size = 0, color_border = None):
        self.pygame.draw.circle(self.canvas, color, (int(x), int(y)), int(radius))
        if border_size and color_border:
            self.pygame.draw.circle(self.canvas, color_border, (int(x), int(y)), int(radius) + border_size, border_size)

    def drawText(self, message, color, x, y):
        self.canvas.blit(self.font.render(message, True, color), (x, y))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)

    def drawExplosion(self, explosion):
        self.drawVeichle('explosion', explosion['x'], explosion['y'], explosion['width'], explosion['height'], 0, 0, 0)
