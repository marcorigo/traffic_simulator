import json
import os

CFG =   {}

def load(workdir = None):

    global CFG

    if not workdir:
        workdir =   os.getcwd()

    with open(os.path.join(workdir, 'cfg.json')) as j:
        CFG     =   json.load(j)

    return CFG