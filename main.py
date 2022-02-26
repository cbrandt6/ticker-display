from request_helper import RequestHelper
from lcd_helper import LCDHelper
import time


def main():
    lcdhelper = LCDHelper()
    request_helper = RequestHelper()
    time.sleep(15)
    lcdhelper.clear()
    lcdhelper.write("new text", (5, 0))
    lcdhelper.write("next text", (0, 1))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        
        print("Closing...")