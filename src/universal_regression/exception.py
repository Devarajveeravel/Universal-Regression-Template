import sys
from src.universal_regression.logging import logger

# [NO-TOUCH ZONE]: Core Error Logic
# WHY: This function "hacks" into the Python system to find the EXACT file name 
# and EXACT line number where the code failed.
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in script: [{0}] at line: [{1}] error: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# [CUSTOMIZE ZONE]: The CustomException Class
# WHY: This creates a "Smart Error." Instead of a generic error, it uses the 
# function above to give you a detailed report.
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message