# Demonstrate how to customize logging output

import logging

# extraData = {} # KeyError: 'user'
extraData = { "user": "jo@gmail.com" }

# TODO: add another function to log from
def another_function():
    logging.debug("Another debugging message", extra=extraData)

# set the output file and debug level, and
# TODO: use a custom formatting specification
# time, level, func, line, user, message
# fmtstr = '%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s'
fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
datestr = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(filename="Start/Ch_4/output.log",
                    level=logging.DEBUG, 
                    format=fmtstr, 
                    datefmt=datestr)

logging.info("This is an info-level log message", extra=extraData)
logging.warning("This is a warning-level message", extra=extraData)
another_function()
