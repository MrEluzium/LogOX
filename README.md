<div align="center">
 <h1>LogOX</h1>
 My interlayer package for python logging

</div>

### About

LogOX is a small add-on over a standart logging module in Python, expanding the process of a logger declaring. Created to make the usage of logger in my own projects easier.

### Feautures

- Log messages store both in the console and in the file

- Log files store in log/ directory and name by date

- Rotating log file every 24 hours

- Better built-in formatting style is used

- Debug messages formatting with file name and code line

### Installation

```
pip install LogOX
```

### Example

```python
import LogOX

log = LogOX.get_logger("MyApp")
debug = LogOX.get_logger(level=LogOX.DEBUG)

log.info("Starting...")
# [03/Jan/2022 21:20:09] MyApp:INFO: Starting...
debug.debug("Yeah debug")
# [03/Jan/2022 21:22:13] [test.py:7] test:DEBUG: Yeah debug
```

###### Log directory format:

```
log/
|- 2022-01-05.log
|- 2022-01-04.log
|- 2022-01-03.log
```
