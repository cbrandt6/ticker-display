from request_helper import RequestHelper
from lcd_helper import LCDHelper
import time
import threading

def main():
    # Create helper objects
    lcdhelper = LCDHelper()
    request_helper = RequestHelper()

    # Print opening text
    time.sleep(2)
    lcdhelper.clear()
    lcdhelper.write("new text", (5, 0))
    lcdhelper.write("next text", (0, 1))
    time.sleep(2)

    # Create scrolling thread
    scrolling_thread = threading.Thread(target=lcdhelper.scrolling_write, args=("Hello there...",))
    scrolling_thread.start()
    print('Scrolling thread started')

    # Create request thread
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Closing...")