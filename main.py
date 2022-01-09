import sys

import pygame
from pygame import display, RESIZABLE

from Ex4.client_python.Exx4 import Exx4
from Ex4.client_python.client import Client


class main:
    def __init__(self):
        self.poc = Exx4()
        self.screen = display.set_mode((1080, 720), depth=32, flags=RESIZABLE)
        self.client = Client()

    def run(self):
        PORT = 6666
        # server host (default localhost 127.0.0.1)
        HOST = '127.0.0.1'
        pygame.init()
        self.client.start_connection(HOST, PORT)
        self.client.start()

        self.poc.getGraph(self.client)
        self.poc.putPokemons(self.client)
        self.poc.putAgent(self.client)

        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        pygame.font.init()
        list1 = []
        firsttime = 0
        clock = pygame.time.Clock()
        self.client.start()

        while self.client.is_running() == 'true':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.poc.Updatepoc(self.client)
            self.poc.UpdeateAgents(self.client)
            self.poc.draw(self.screen)
            self.poc.choose_Agents(firsttime, self.client)

            clock.tick(60)
            firsttime = firsttime + 1
            if float(self.client.time_to_end())<60:
                self.client.stop_connection()
                self.client.stop()

if __name__ == '__main__':
    x = main()
    x.run()
