import LCD1602
import time


class LCDHelper:

    def __init__(self):
        LCD1602.init(0x27, 1)  # init(slave address, background light)
        LCD1602.write(0, 0, 'Hello')
        LCD1602.write(1, 1, 'There')
        time.sleep(2)
    
    def clear(self):
        LCD1602.clear()

    def write(self, text, text_pos):
        LCD1602.write(text_pos[0], text_pos[1], text)

    def scrolling_write(self, text):
        try:
            while(True):
                for i in range(15, -1*len(text), -1):
                    
                    self.clear()
                    time.sleep(0.15)
                    # write
                    if i >= 0:
                        self.write(text, (i, 0))
                    else:
                        self.write(text[len(text) - (len(text)+i)::], (i, 0))
                    time.sleep(0.15)
        except KeyboardInterrupt:
            print("Loop broken")
            

    def destroy():
	    LCD1602.clear()