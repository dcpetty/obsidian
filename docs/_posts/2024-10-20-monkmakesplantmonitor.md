---
title: "Monk Makes Plant Monitor"
date: 2024-10-20 18:56:13
last_modified_at: 2024-10-26 10:19:17
show_date: true
permalink: /microbit/monkmakesplantmonitor/
toc: true
toc_sticky: true
---
This documents a [Python](https://www.python.org/community/microbit/) library for the [Monk Makes Plant Monitor](https://monkmakes.com/pmon) (MMPM) connected to a BBC [`micro:bit`](https://microbit-micropython.readthedocs.io/en/v2-docs/) through the [`micro:bit` Python Editor](https://microbit.org/get-started/user-guide/python-editor/) over a serial connection.

# Assumptions

- The MMPM communicates over a two-way serial link at 9600bps, N81 protocol on two unused pins. This code assumes TX on `pin8` and RX on `pin9`. (The only pins on a [micro:bit v2](https://tech.microbit.org/hardware/edgeconnector/) that are unused for other micro:bit functions are `pin0`, `pin1`, `pin2`, `pin8`, `pin9`, and `pin16`.)
- In order to use the micro:bit on-line serial terminal that, '&hellip;shows errors and other output from the program running on your micro:bit' so the '&hellip;program can print messages using the `print` function,' the [UART](https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html) must be set to its default settings with `uart.init(115200)`. *However*, the MMPM also communicates serially using the UART, so it must also be initialized before use.
- The three commands used to read the three sensors are `'h'`, `'t'`, and `'w'`. There are other commands (`'j'`, `'L'`, `'l'`, and `'v'`) that are unused by this library. The command summary is:

| Command | Delay | Units | Notes |
| :---: | :---: | :---: | --- |
| `'h'` | 100ms | % &#xb1; 2% | relative humidity |
| `'t'` | 100ms | &#xb0;C | temperature |
| `'w'` | 1000ms | % | moisture |

- The connector J3 has 5 connections, both with clippable through-hole connections and 0.1" pin header. The pins are:

| Pin | Signal | I/O | Notes |
| :---: | :---: | :---: | --- |
| 1 | `PA6/D2/DAC` | O | analog moisture (25mV / %) |
| 2 | `TxD` | O | transmit data |
| 3 | `RxD` | I | receive data |
| 4 | `+3V` | +V | +3V |
| 5 | `GND` | &#x23da; | ground |

# Code

```python
# Imports go at the top
from microbit import *

delay= 10
pm_init = lambda: uart.init(9600, 8, None, 1, tx=pin8, rx=pin9)
py_init = lambda: uart.init(115200)

def read_data(delay=delay):
    """Returns a dictionary with data readings of humidity, temperature,
    and moisture read over a serial connection from a Monk Makes Plant
    Monitor. An example return is: {'h': 48.43, 'w': 38.0, 't': 23.56}.
    The value types will be float. If a ValueError is generated from
    the uart.readline text, the commands are repeated until all results
    are good. The UART is set to 9600 8N1 on pins 8 & 9."""
    pm_init()
    res, ret = dict(), ''
    # Process 'h', 't', & 'w' commands until all responses are float.
    while not(res and all(type(val) is float for val in res.values())):
        # Process commands for humidity, temperature, and wetness.
        for cmd, slp in {'h': 100, 't': 100, 'w': 1000}.items():
            uart.write(cmd)
            sleep(max(slp, delay))   # slp response time from datasheet
            while not ret:
                ret = uart.readline()
            # ret must be of the form 'h=48.43\n', otherwise ValueError.
            try:
                key, val = str(ret, 'utf-8').strip().split('=')
                res[key], ret = float(val), ''
            except ValueError as e:
                res[cmd], ret = e, ''
    sleep(delay)
    return res

def echo_data(data, delay=delay):
    """Setup UART to default (115200) and print data."""
    py_init()
    print(data)
    sleep(delay)

# Code in a 'while True:' loop repeats forever
while True:
    data = read_data()
    echo_data(data)
    if button_a.is_pressed(): break

1234567890123456789012345678901234567890123456789012345678901234567890

```

# Links

| Link | Description |
| --- | --- |
| [https://monkmakes.com/&#8203;](https://monkmakes.com/) | 'Founded in 2013, Monk Makes Ltd designs and manufacturers a wide range of electronics kits and circuit boards from its base in the North West of England.' |
| [https://monkmakes.com/&#8203;pmon](https://monkmakes.com/pmon) | Plant Monitor website |
| [https://www.adafruit.com/&#8203;product/&#8203;5587](https://www.adafruit.com/product/5587) | Plant Monitor available at [adafruit](https://www.adafruit.com/) |
| [https://monkmakes.com/&#8203;downloads/&#8203;datasheet_plant_monitor.pdf](https://monkmakes.com/downloads/datasheet_plant_monitor.pdf) | Plant Monitor datasheet |
| [https://github.com/&#8203;monkmakes/&#8203;plant_monitor_firmware](https://github.com/monkmakes/plant_monitor_firmware) | Plant Monitor firmware |
| [https://tech.microbit.org/&#8203;hardware/&#8203;edgeconnector/&#8203;](https://tech.microbit.org/hardware/edgeconnector/) | micro:bit pinouts |
| [https://microbit-micropython.readthedocs.io/&#8203;en/&#8203;v2-docs/&#8203;uart.html](https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html) | micro:bit UART |
| [https://ww1.microchip.com/&#8203;downloads/&#8203;en/&#8203;DeviceDoc/&#8203;ATtiny1614-16-17-DataSheet-DS40002204A.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf) | ATTiny 1614 — the µcontroller |
| [https://docs.python.org/&#8203;3.4/&#8203;](https://docs.python.org/3.4/) | Python 3.4 documentation |