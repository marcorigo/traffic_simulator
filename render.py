from config import config

class RenderEngine:
    def __init__(self, canvas, pygame, cell_width, width, height, font):
        self.pygame = pygame
        self.canvas = canvas
        self.cell_width = cell_width
        self.width = width
        self.height = height
        self.font = font
        self.font_color = config['TEXT_COLOR']
        self.car = self.pygame.image.load('./sprites/veichles/car1.png').convert_alpha()
        self.truck = self.pygame.image.load('./sprites/veichles/truck.png').convert_alpha()
        self.taxi = self.pygame.image.load('./sprites/veichles/taxi.png').convert_alpha()
        self.roadSprites = {
            '═' :self.pygame.image.load('./sprites/map/roadHorizontal.png').convert_alpha(), 

            '║' :   self.pygame.image.load('./sprites/map/roadVertical.png').convert_alpha(),

            '╬' :   self.pygame.image.load('./sprites/map/roadIntersection.png').convert_alpha(),

            '╔' :   self.pygame.image.load('./sprites/map/roadCurveES.png').convert_alpha(),

            '╚' :   self.pygame.image.load('./sprites/map/roadCurveNE.png').convert_alpha(),

            '╗' :   self.pygame.image.load('./sprites/map/roadCurveSO.png').convert_alpha(),

            '╝' :   self.pygame.image.load('./sprites/map/roadCurveNO.png').convert_alpha(),

            '➡' :   self.pygame.image.load('./sprites/map/roadHorizontalSpawn2.png').convert_alpha(),

            '⬅' :   self.pygame.image.load('./sprites/map/roadHorizontalSpawn4.png').convert_alpha(),

            '⬆' :   self.pygame.image.load('./sprites/map/roadVerticalSpawn1.png').convert_alpha(),

            '⬇' :   self.pygame.image.load('./sprites/map/roadVerticalSpawn3.png').convert_alpha(),

            '╩' :   self.pygame.image.load('./sprites/map/TRoad1.png').convert_alpha(),

            '╠' :   self.pygame.image.load('./sprites/map/TRoad2.png').convert_alpha(),

            '╦' :   self.pygame.image.load('./sprites/map/TRoad3.png').convert_alpha(),

            '╣' :   self.pygame.image.load('./sprites/map/TRoad4.png').convert_alpha(),

             0  :   self.pygame.image.load('./sprites/map/grass.png').convert_alpha(),
        }

        self.veichlesSprites = {
            'car'       :   [   self.pygame.image.load('./sprites/veichles/car1.png').convert_alpha(),  False   ],
            'truck'     :   [   self.pygame.image.load('./sprites/veichles/truck.png').convert_alpha(), False   ],
            'taxi'      :   [   self.pygame.image.load('./sprites/veichles/taxi.png').convert_alpha(),  False   ],
            'explosion' :   [   self.pygame.image.load('./sprites/other/explosion.png').convert_alpha(),      False   ],
        }

        self.resize(self.roadSprites, self.cell_width, self.cell_width)

    def resize(self, sprites, width, height):
        for key in sprites.keys():
            sprites[key] = self.pygame.transform.scale(sprites[key], (width, height))

    def getRoadTile(self, road_type):
        return self.roadSprites[road_type]

    def drawRoadTile(self,x, y, road_type):
        roadTile = self.getRoadTile(road_type)
        if roadTile:

            imagerect = roadTile.get_rect()
            imagerect.center = ( x + (self.cell_width // 2) , y + ( self.cell_width // 2))   
            self.canvas.blit(roadTile, imagerect)
            return True
        else:
            return False

    def drawVeichle(self, veichle_name, x, y, width, height, angle, fvW, fvH, image = None):

        # Resize texture for first time
        if not self.veichlesSprites[veichle_name][1]:
            self.veichlesSprites[veichle_name][0] = self.pygame.transform.scale(self.veichlesSprites[veichle_name][0], (width, height))
            self.veichlesSprites[veichle_name][1] = True

        image_orig = self.veichlesSprites[veichle_name][0]
        image = image_orig.copy()

        rect = image.get_rect()  
        rect.center = ( x + (width // 2) , y + ( height // 2))
        old_center = rect.center  
        rot = angle
        new_image = self.pygame.transform.rotate(image_orig , rot)  
        rect = new_image.get_rect()  
        rect.center = old_center   
        self.canvas.blit(new_image , rect)  

    def drawImage(self, image, x, y):
        self.canvas.blit(image, (x, y)) 

    def drawRect(self, x, y, width, height, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, height))

    def drawCircle(self, x, y, radius, color, border_size = 0, color_border = None):
        self.pygame.draw.circle(self.canvas, color, (int(x), int(y)), int(radius))
        if border_size and color_border:
            self.pygame.draw.circle(self.canvas, color_border, (int(x), int(y)), int(radius) + border_size, border_size)

    def drawText(self, message, x, y):
        self.canvas.blit(self.font.render(message, True, self.font_color), (x, y))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)

    def drawExplosion(self, explosion):
        self.drawVeichle('explosion', explosion['x'], explosion['y'], explosion['width'], explosion['height'], 0, 0, 0)

    def createSurfaceFromMap(self, map, width, height):
        screen = self.pygame.Surface((width, height))
        for y in range(len(map)):
            for x in range(len(map[y])):
                road = map[y][x]
                if road:
                    screen.blit(self.getRoadTile(road.road_type), (x * road.cell_width, y * road.cell_width))
        return screen
