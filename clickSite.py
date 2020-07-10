#Desafio 1 - Click em um site
import pyautogui

class Bot:
    def __init__(self):
        self.x = 346
        self.y = 598
        self.duracao = 2
    def run(self):
        pyautogui.moveTo(x=self.x, y=self.y, duration=self.duracao)
        for i in range(1, 100):
            pyautogui.click()

bot = Bot()
bot.run()
