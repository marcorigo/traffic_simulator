import time
import random
from const import config


class TrafficLight():
    dt = 0
    def __init__(self, cell_width):
        self.yellow_light_time = config.TRAFFIC_LIGHT_YELLOW_TIME
        self.min_interval = config.TRAFFIC_LIGHT_MIN_TIME_CHANGING
        self.max_interval = config.TRAFFIC_LIGHT_MAX_TIME_CHANGING
        self.border_size = config.TRAFFIC_LIGHT_BORDER_SIZE
        self.border_color = config.TRAFFIC_LIGHT_BORDER_COLOR
        self.colors = config.TRAFFIC_LIGHT_COLORS
        self.init_colors = ['green', 'red']
        self.radius = cell_width / 15
        self.change_time = random.randint(self.min_interval, self.max_interval)
        self.last_change = int(time.time())
        # Get first green roads randomly
        self.changing = random.randint(1, 2)
        self.x_light = self.init_colors.pop(self.changing - 1)
        self.y_light = self.init_colors[0]
        self.cell_width = cell_width


    def draw(self,renderEngine,road,rotation=0):
        if rotation == 0:
            self.top(renderEngine, road)
            self.bottom(renderEngine, road)
            self.left(renderEngine, road)
            self.right(renderEngine, road)
        # ╩
        if rotation == 1:
            # Draw traffic light
            self.top(renderEngine,road)
            self.left(renderEngine,road)
            self.right(renderEngine,road)

        # ╠
        if rotation == 2:
            # Draw traffic light
            self.top(renderEngine,road)
            self.bottom(renderEngine,road)
            self.right(renderEngine,road)

        # ╦
        if rotation == 3:
            # Draw traffic light
            self.bottom(renderEngine,road)
            self.left(renderEngine,road)
            self.right(renderEngine,road)

        # ╣
        if rotation == 4:
            # Draw traffic light
            self.top(renderEngine,road)
            self.bottom(renderEngine,road)
            self.left(renderEngine,road)


    def top(self, renderEngine,road):
        renderEngine.drawCircle(road.x + self.cell_width / 2, road.y + self.border_size,
                                self.radius,
                                self.colors[self.y_light],
                                self.border_size, self.border_color)


    def bottom(self, renderEngine,road):
        renderEngine.drawCircle(road.x + self.cell_width / 2,
                                road.y + self.cell_width - self.radius - self.border_size,
                                self.radius,
                                self.colors[self.y_light],
                                self.border_size, self.border_color)


    def left(self, renderEngine, road):
        renderEngine.drawCircle(int(road.x + self.border_size), int(road.y + self.cell_width / 2),
                                self.radius,
                                self.colors[self.x_light],
                                self.border_size, self.border_color)


    def right(self, renderEngine, road):
        renderEngine.drawCircle(int(road.x + self.cell_width - self.radius - self.border_size),
                                int(road.y + self.cell_width / 2),
                                self.radius,
                                self.colors[self.x_light],
                                self.border_size, self.border_color)


    def update(self):
        self.change_time *= self.dt
        self.yellow_light_time *= self.dt

        now = int(time.time())

        if self.last_change + self.change_time < now:
            self.last_change = now

            if self.changing == 1:
                self.x_light = 'yellow'
                self.changing = 2
                self.road_allowed = [0]
            else:
                self.y_light = 'yellow'
                self.changing = 1
                self.road_allowed = [0]

        if self.last_change + self.yellow_light_time < now:
            if self.changing == 1:
                self.y_light = 'red'
                self.x_light = 'green'
                self.road_allowed = [2, 4]
            else:
                self.x_light = 'red'
                self.y_light = 'green'
                self.road_allowed = [1, 3]
