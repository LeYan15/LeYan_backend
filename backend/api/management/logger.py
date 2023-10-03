import logging
import logging.handlers

FORMAT = "%(asctime)s :: %(name)s:%(lineno)s - %(levelname)s - %(message)s"


def password_filter(log: logging.LogRecord) -> int:
    if "password" in str(log.msg):
        return 0
    return 1


def init_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    sh.addFilter(password_filter)

    fh = logging.handlers.RotatingFileHandler(
        filename="backend/api/logs/test.log"
    )
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug("logger was init")
