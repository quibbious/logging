# logging

the logging library is a simple event logger that handles exceptions, functions (when permitted), and allows for manual logging.


# Documentation

## Usage

First, you will need to initialize the Logger, and provide a boolean value to allow the Logger to function. This can be done with:

`myLogger = Logging(allowLogging=True)`

After initalizing the logger, you can use its many functions. These include:

`myLogger.status() #prints debug info about the logger`

`myLogger.FunctionSuccess(foo) #allows a function name as input and returns True if it ran successfully (more later).`

`myLogger.ManLogFile(message) #allows the user to manually log a message to the debug.log file.`

### Logging.print

While not mentioned earlier, there is a subclass to 'Logging' called 'print'. Print allows the user to manually print different errors to the console. These include:

-Logging.print.Info(message)

`[INFO]: provides general information of no severity`

-Logging.print.Warning(message)

`[WARNING]: maybe a function is having some issues, but it automatically fixes it`

-Logging.print.Error(message)

`[ERROR]: use this if a function fails, but it's fine to continue`

-Logging.print.Critical(message)

`[CRITICAL]: in most cases, its best not to ignore these`

### WIP
