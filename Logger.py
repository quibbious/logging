import os 
import datetime 
import time

class Logging:
    def __init__(self, allowLogging: bool = False):
        """main class for the Logging module. "allowLogging"'s boolean value determines if logging is enabled or disabled. The status() function runs anyway."""
        if os.path.exists("debug.log"):
            self.debugFileExists = True
        else: 
            self.debugFileExists = False
        self.logTime = datetime.datetime.now()
        self.logTimeShort = self.logTime.strftime('%Y-%m-%d %H:%M:%S')
        self.allowLogging = allowLogging
        if allowLogging == True:
            
            self.file = open('debug.log', 'w')
            self.file.write(f"BEGINNING OF LOG FILE AT TIME {self.logTime}\nloggerDebug: logger module activated. ")
            self.file.write("\n\n")
            self.ExceptionWriter = open('debug.log', "a")
            self.file.write("------------------------------")
            print("logging started! ")
            
            
        elif allowLogging == False:
            if self.debugFileExists == True:
                os.remove('debug.log')
            print("logging is disabled.")
        
    class print():
        def __init__(self):
            super().__init__()
        def INFO(message):
            print(f"\033[37mINFO: {message}\033[0m")
            
        def WARNING(message):
            print(f"\033[33mWARNING: {message}\033[0m")
            
        def ERROR(message):
            print(f"\033[38;5;208mERROR: {message}\033[0m")
            
        def CRITICAL(message):
            print(f"\033[31mCRITICAL: {message}\033[0m")
    
    def FunctionSuccess(self, func):
        self.func = func
        """checks if a function ran successfully, and prints it to the 'debug.log' file"""
        if self.allowLogging == True:
            
            if callable(func):
            
                try:

                    caller_name = str(self.func.__name__)
                    self.func()
                    self.file.write(f"\nlogger: function {caller_name}() ran successfully.")
                    return True
                except Exception as e:
                    caller_name = str(self.func.__name__)
                    print(f"function {caller_name}() failed - '{e}'")
                    self.ExceptionWriter.write(f"\nlogger: function {caller_name}() failed! - '{e}'")  
                    return False  
            else: 
                raise Logging.print.CRITICAL(f"provided argument is not a function.")
        else:
            pass
    
    def ManLogFile(self, message):
        """allows the user to manually log messages to the 'debug.log' file. Does not log messages if flag 'allowLogging' is disabled."""
        if self.allowLogging == True: 
            self.file.write(f"\nManLog-FILE: {message}")
        else:
            pass
        
    def status(self):
        time.sleep(0.75)
        status = {
            "allowLogging": self.allowLogging,
            "debugFileExists": self.debugFileExists,
            "logTimeCurrent":self.logTimeShort,
            
        }
        print(status)
        

logger=Logging(allowLogging=True)

logger.ManLogFile("this logs to the file directly. (if enabled)")

logger.status()

        
