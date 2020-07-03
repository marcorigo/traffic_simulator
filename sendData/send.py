import time
import os
import random
import json
import logging
from azure.eventhub import EventData, EventHubProducerClient
import cfg as cfg
config =   cfg.load()
import threading
import math
import atexit

from .logger import get_logger
logger = get_logger(logging.INFO)

SEND_INTERVAL = config['SEND_INTERVAL']
CONN_STRING = config['EVENTHUB_CONN_STRING']
NAME = config['EVENTHUB_NAME']

client = None

if config['USE_AZURE']:
    client = EventHubProducerClient.from_connection_string(conn_str = CONN_STRING, eventhub_name = NAME)

class SendDataThread (threading.Thread):
    def __init__(self, name, data):
        threading.Thread.__init__(self, daemon=True)
        self.name = name
        self.data = data
        self.client = client
        self.init()
        atexit.register(self.closeConnection)


    def init(self):
        if not CONN_STRING or not NAME:
            raise ValueError("No EventHubs URL or name supplied.")


    def run(self):
        if not self.data:
           logger.info('Started send data thread')

        self.sendData(self.data)

        logger.info('Bots data successfully sended')


    def createBatch(self, event_data_batch, bots):
        for bot in bots:
            reading_vehicle = self.createJson(bot)
            event_data_batch.add(EventData(json.dumps(reading_vehicle)))

        return event_data_batch


    def sendData(self, bots):
        if not bots:
            logger.info('No bots passed')
            return

        event_data_batch = self.client.create_batch()

        event_data_batch = self.createBatch(event_data_batch, bots)

        self.client.send_batch(event_data_batch)

        time.sleep(SEND_INTERVAL)


    def closeConnection(self):
        self.client.close()


class  SendVehicleDataThread (SendDataThread):
    def __init__(self, name, data = []):
        super().__init__(name, data)
        
    def createJson(self, bot):
        return {'id': bot.veichle.id, 'type': type(bot.veichle).__name__, 'road': bot.getCurrentRoad(), 'velocity': math.sqrt((math.pow(float(bot.veichle.velocity.x), 2)) + (math.pow(float(bot.veichle.velocity.y), 2)))}


class  SendTrafficLightDataThread (SendDataThread):
    def __init__(self, name, data = []):
        super().__init__(name, data)
        
    def createJson(self, bot):
        pass