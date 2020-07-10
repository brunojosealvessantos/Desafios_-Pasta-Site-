#Desafio 1 - Zerando o jogo de clicks
import pyautogui

class Bot:
    def __init__(self):
        self.x = 213
        self.y = 301
        self.duracao = 1
    def run(self):
        pyautogui.moveTo(x=self.x, y=self.y, duration=self.duracao)
        for i in range(1, 10000000):
            pyautogui.click()

bot = Bot()
bot.run()
