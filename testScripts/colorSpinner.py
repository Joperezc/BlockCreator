


import sys, os
import colorama
import random
import time
colors = [colorama.Fore.RED, colorama.Fore.BLACK, colorama.Fore.BLUE, colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.MAGENTA, colorama.Fore.WHITE, colorama.Fore.YELLOW]

class colorSpinner:


    def __init__(self, colorLis, txtString) -> None:
        self.colorList = colorLis
        self.txtString = txtString


    def spinColor(self):
        color = random.choice(self.colorList)
        while(True):
            try:
                time.sleep(0.5)
                os.system('clear')
                print(color, self.txtString)
                color = random.choice(self.colorList)
            except:
                sys.exit()
    





    def test1():

										def test2():
											pass
										pass


if __name__ == "__main__":
    spin = colorSpinner(colors, "Hello World!")
    spin.spinColor()