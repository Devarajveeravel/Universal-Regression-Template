import os
import sys
import logging

# [TECH TERM]: logging_str
# WHY: Defines the format of the log (Time, Level like INFO/ERROR, Module name, and the Message).
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# [TECH TERM]: log_dir
# WHY: We create a folder called "logs" so we don't clutter your main project.
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# [NO-TOUCH ZONE]: Configuration logic
# WHY: This tells the computer to save logs to a file AND show them in your terminal.
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # Saves to the log file
        logging.StreamHandler(sys.stdout)  # Prints to your screen
    ]
)

# [CUSTOMIZE ZONE]: The name of your logger
logger = logging.getLogger("universal_regression_logger")