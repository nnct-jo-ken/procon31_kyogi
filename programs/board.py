import numpy as np

NEUTRAL = 0
WALL1 = 1
POS1 = 2
WALL2 = 3
POS2 = 4
AGENT1 = 1
AGENT2 = 2
NO_AGENT = 0

class board():
    def __init__(self, width, height, agentNum):
        self.width = width
        self.height = height
        self.agentNum = agentNum
        self.fieldInfo = np.empty((width, height), dtype=np.int)
        self.fieldPoint = np.empty((width, height), dtype=np.int)
        self.fieldAgent = np.empty((width, height), dtype=np.int)
        self.scores = [0, 0]

    