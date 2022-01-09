import FindPocEdge
from Ex4.client_python import Agent
from src_Ex3.DiGraph import DiGraph


class pokemon:
    def __init__(self, value, Type,pos1, pos: (0, 0, 0), graph: DiGraph):
        self.value = value
        self.pos = pos1
        self.type = Type
        find = FindPocEdge.PocEdge((pos[0], pos[1], pos[2]),Type)
        self.src, self.dest = find.findEdge(graph)
        self.target = False
        self.Agent=Agent
        self.killed=False

