from visa_Approval.logger import logging
from visa_Approval.exception import USvisaException
import sys

## logging.info("Welcome to out logs") // this for giving log information
try:
    a =1 /"10"
except Exception as e:
    logging.info(e)
   raise USvisaException("e, sys") from e// this is for giving error information at log stamp