


import sys, os
import colorama
import threading
import random
import time
colors = [colorama.Fore.RED, colorama.Fore.BLACK, colorama.Fore.BLUE, colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.MAGENTA, colorama.Fore.WHITE, colorama.Fore.YELLOW]


#################
#Comment Block
#Class: colorSpinner
#Description: 
#################

class colorSpinner:


	




	#################
	#Comment Block
	#Function: __init__
	#Description: 
	#colorLis Param: 
	#txtString Param: 
	#################

    def __init__(self, colorLis, txtString) -> None:
        self.colorList = colorLis
        self.txtString = txtString




	#################
	#Comment Block
	#Function: spinColor
	#Description: 
	#################

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
    









	#################
	#Comment Block
	#Function: test1
	#Description: 
	#################

    def test1():




										#################
										#Comment Block
										#Function: test2
										#Description: 
										#################

										def test2():
											pass
										pass


#################
#Comment Block
#Description: 
#################

if __name__ == "__main__":
    spin = colorSpinner(colors, "Hello World!")
    spin.spinColor()