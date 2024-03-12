import sys
def error_msg_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_msg=f'Error Occured in Script[{filename}] line no [{exc_tb.tb_lineno}] error message [{str(error)}]'
    return error_msg
class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message,error_details=error_detail)
    def __str__(self):
        return self.error_message
