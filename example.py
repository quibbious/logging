from Logger import Logging

logger=Logging(allowLogging=True) # initializes the Logging class and creates the debug.log file upon execution.

logger.ManLogFile("this logs to the file directly. (if enabled)") # directly logs a message to the debug.log file.

logger.status() #prints the status of the logger.

def failAlways():
    raise Exception("I am doomed to fail")

def neverFail():
    print("i am the gifted one")

logger.FunctionSuccess(neverFail) #returns True, and prints "i am the gifted one" to console, and "function neverFail() ran successfully." to the debug.log file
    
logger.FunctionSuccess(failAlways) #returns False, and writes " function failAlways() failed - I am doomed to fail " to the 'debug.log' file, then the program stops

# these methods can also help with the .print subclass of the Logging class.

# to print an error, use Logging.print.ERROR(message), where message is the error you want to print. For example:
Logging.print.Info(message="provides general information of no severity")
Logging.print.Warning(message="maybe a function is having some issues, but it automatically fixes it") # this works without needing to initialize the 'logger' variable as well. This does not write to 'debug.log'.
Logging.print.Error(message="use this if a function fails, but it's fine to continue")
Logging.print.Critical(message="in most cases, its best not to ignore these")
