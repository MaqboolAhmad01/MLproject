import logging
import os
import sys
from exception import customException
from datetime import datetime
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
print(os.getcwd())
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
print(LOG_FILE_PATH)

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:

        logging.info("divide by zero")
        raise customException(e,sys)
