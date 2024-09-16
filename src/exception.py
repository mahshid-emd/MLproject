import sys
from src.logger import logging

def error_message_detail(error_message):
    name = sys.exc_info()[0]
    line = sys.exc_info()[2].tb_lineno
    message = sys.exc_info()[1]
    error_message = f"Error occured in python script name: {name} \nline number: {line} \nerror message: {message}."
    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message
    

if __name__ == '__main__':
    try:
        a = [1,2,3,4]
        a[6]
    except Exception as e:
        logging.info('list index out of range')
        raise CustomException(e)

