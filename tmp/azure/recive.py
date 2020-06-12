import time
import os
import random
import json
import datetime
import logging
import uuid
from azure.servicebus import QueueClient, Message

from logger import get_logger
logger = get_logger(logging.INFO)

CONN_STRING = ""
NAME = 'data'

try:
    if not CONN_STRING or not NAME:
        raise ValueError("No EventHubs URL or name supplied.")

    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(CONN_STRING, NAME)

    # Receive the message from the queue
    with queue_client.get_receiver() as queue_receiver:
        while True:
            messages = queue_receiver.fetch_next(timeout=3)
            for message in messages:
                logger.info(message)
                message.complete()
            time.sleep(5)

except KeyboardInterrupt:
    pass
