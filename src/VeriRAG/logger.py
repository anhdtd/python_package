import logging

from VeriRAG import constant


def get_logger():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("./logging.log", "a", "utf-8")

    format = (
        "%(asctime)s %(levelname)s %(name)s [%(filename)s:%(lineno)d] : %(message)s"
    )
    format = logging.Formatter(format)

    c_handler.setFormatter(format)
    f_handler.setFormatter(format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


logger = get_logger()

# if __name__=="__main__":
#     logger = get_logger(__name__)
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')
#     logger.debug('This is a debug message')
#     logger.info('This is an info message')
