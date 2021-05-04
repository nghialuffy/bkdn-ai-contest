from controller import process_result
from time import sleep
if __name__ =="__main__":
    try:
        while True:
            process_result()
            sleep(1)
    except Exception as exc:
        print("Error in main: %s" % str(exc))