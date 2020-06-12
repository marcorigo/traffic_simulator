import time
import os
import random
import json
import datetime
import logging
import uuid
from azure.eventhub import EventData, EventHubProducerClient

from logger import get_logger
logger = get_logger(logging.INFO)

CONN_STRING = ""
NAME = 'a'

try:
    if not CONN_STRING or not NAME:
        raise ValueError("No EventHubs URL or name supplied.")

    devices = []
    for x in range(0, 10):
        devices.append(str(uuid.uuid4()))

    client = EventHubProducerClient.from_connection_string(conn_str = CONN_STRING, eventhub_name = NAME)

    while True:    # For each device, produce 20 events. 
        event_data_batch = client.create_batch() # Create a batch. You will add events to the batch later. 
        for dev in devices:
            # Create a dummy reading.
            reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'uv': random.random(), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100)}
            s = json.dumps(reading) # Convert the reading into a JSON string.
            logger.info(s)
            event_data_batch.add(EventData(s)) # Add event data to the batch.
            time.sleep(1)
        client.send_batch(event_data_batch) # Send the batch of events to the event hub.

    client.close()

except KeyboardInterrupt:
    pass
