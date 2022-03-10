# functions_utiles.py

from LogFormatter import setup_logging

def init_logger(logfile_file,console_log_level,logfile_log_level):
    """
    Initialisation of the logger
    """
    if (not setup_logging(console_log_output="stdout", console_log_level=console_log_level, console_log_color=True,
                          logfile_file=logfile_file, logfile_log_level=logfile_log_level, logfile_log_color=False,
                          log_line_template="%(color_on)s[%(asctime)s] [%(module)s] [%(funcName)s] [%(levelname)-8s] %(message)s%(color_off)s")):
        print("Failed to setup logging, aborting.")
        return 1
