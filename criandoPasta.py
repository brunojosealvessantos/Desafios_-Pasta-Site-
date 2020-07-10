#Desafio 2 - Criando uma pasta
import pyautogui

class Bot:
    def __init__(self):
        self.x = 394
        self.y = 18
        self.duracao = 2
    def run(self,right,left):
        pyautogui.moveTo(x=self.x, y=self.y, duration=self.duracao)
        pyautogui.click(button = right)
        pyautogui.moveTo(x=354, y=318, duration=2)
        pyautogui.moveTo(x=400, y=318, duration=1)
        pyautogui.click(button = left)
        pyautogui.write('Pasta Teste')
        pyautogui.hotkey('Enter')

bot = Bot()
bot.run('right','left')
