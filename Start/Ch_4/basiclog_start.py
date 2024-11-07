# demonstrate the logging api in Python
import logging

# TODO: use the built-in logging module


# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, 
                    filemode='w', # overwrites log file
                    filename='Start/Ch_4/output.log')

# TODO: Try out each of the log levels
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
logging.critical('Critical var {} and int {}'.format(['Value'], 100)) # outputs: CRITICAL:root:Critical var ['Value'] and int 100

# TODO: Output formatted strings to the log

