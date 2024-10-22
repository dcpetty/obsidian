# Monk Makes Plant Monitor

In connecting the [Monk Makes Plant Monitor](https://monkmakes.com/pmon) to a [`micro:bit`](https://microbit-micropython.readthedocs.io/en/v2-docs/) using [`micro:bit` Python](https://microbit.org/get-started/user-guide/python-editor/), there are several assumptions

# Code

```Python
# Imports go at the top
from microbit import *

delay, buffer = 10, ''
pm_init = lambda: uart.init(9600, 8, None, 1, tx=pin8, rx=pin9)
py_init = lambda: uart.init(115200)

def read_data(delay=delay):
    """Returns a dictionary with data readings of humidity, temperature, and moisture
    read over a serial connection from a Monk Makes Plant Monitor. An example return
    is: {'h': 48.43, 'w': 38.0, 't': 23.56}. The value types will be float, unless
    a ValueError is generated from the return."""
    res, ret = dict(), ''
    pm_init()
    # Process commands for humidity, temperature, and wetness
    for cmd in 'htw':
        uart.write(cmd + '\n')
        sleep(max(100,delay))   # this is an experimental magic number to allow response
        while not ret:
            ret = uart.readline()
        try:
            key, val = str(ret, 'utf-8').strip().split('=')
            res[key], ret = float(val), ''
        except ValueError as e:
            res[cmd], ret = e, ''
    sleep(delay)
    return(res)
    
    
# Code in a 'while True:' loop repeats forever
while True:
    data = read_data()
    py_init()
    print(data)
    sleep(delay)
    if button_a.is_pressed(): break
```

# Links

| Link | Description |
| --- | --- |
| [[https://monkmakes.com/]] | 'Founded in 2013, Monk Makes Ltd designs and manufacturers a wide range of electronics kits and circuit boards from its base in the North West of England.' |
| [[https://monkmakes.com/pmon]] | Plant Monitor website |
| [[https://monkmakes.com/downloads/datasheet_plant_monitor.pdf]] | Plant Monitor datasheet |
| [[https://github.com/monkmakes/plant_monitor_firmware]] | Plant Monitor firmware |
| [[https://tech.microbit.org/hardware/edgeconnector/]] | micro:bit pinouts |
| [[https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html]] | micro:bit UART |
| [[https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf]] | ATTiny 1614 — the µcontroller |
