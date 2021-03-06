AUTO = False

config = {
    'BLOCK_SIZE': 50, 
    'DEBUG': False,
    'MAX_VEICHLE_NUMBER': 30,
    'VEICHLES_SPAWN_INTERVAL': AUTO,
    'BACKGROUND_COLOR': (120, 226, 104),
    'SIDE_WALK_SIZE': AUTO,
    'ROAD_COLOR': (170, 170, 170),
    'SIDE_WALK_COLOR': (94, 94, 94),
    'ROAD_LINE_QUANTITY': 5,
    'TRAFFIC_LIGHT_BORDER_SIZE': 0,
    'TRAFFIC_LIGHT_BORDER_COLOR': (96, 96, 96),
    'TRAFFIC_LIGHT_YELLOW_TIME': 10,
    'TRAFFIC_LIGHT_MIN_TIME_CHANGING': 50,
    'TRAFFIC_LIGHT_MAX_TIME_CHANGING': 90,
    'CAR_WIDTH': AUTO,
    'CAR_HEIGHT': AUTO,
    'TRUCK_WIDTH': AUTO,
    'TRUCK_HEIGHT': AUTO,

    #'DT': 0.5,
    'TEXT_COLOR': (255, 255, 255),

    'CAR_SPAWN_RATE': 70,       # p
    'TRUCK_SPAWN_RATE' : 30,    # q

    'EXPLOSION_PERSISTANCE': 3,

    'USE_TEXTURES': True,

    'VEICHLE_VISION_FIELD_WIDTH': AUTO,
    'VEICHLE_VISION_FIELD_HEIGHT': AUTO,

    'TRAFFIC_LIGHT_COLORS': {
        'red' : (255, 0, 0),
        'yellow': (247, 228, 86),
        'green': (87, 226, 40)
    }
}
