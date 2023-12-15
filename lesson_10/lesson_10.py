from logger import logger as log

def divide(x, y):

    assert x > 0, f"x=={x}, але повинно бути додатнім числом"

    try:
        result = x / y
    except ZeroDivisionError as e:
        log.error('Attempted to divide by zero')
        raise e
    else:
        log.info(f'{x} divided by {y} is {result}')
        return result
    finally:
        log.debug('Its message of level DEBUG')
        log.info('Its message of level INFO')
        log.warning('Its message of level WARNING')
        log.error('Its message of level ERROR')
        log.critical('Its message of level CRITICAL')

if __name__ == "__main__":
    divide(-1, 2)
    #divide(1, 0)