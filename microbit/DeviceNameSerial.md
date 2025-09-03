# Device name and serial number example

This documents [Python](https://www.python.org/community/microbit/) example code for obtaining the *friendly name* of a BBC [`micro:bit`](https://microbit-micropython.readthedocs.io/en/v2-docs/) through the [`micro:bit` Python Editor](https://microbit.org/get-started/user-guide/python-editor/).

This code displays the `device name` and (optionally) the `device serial number` so the [`micro:bit`](https://microbit-micropython.readthedocs.io/en/v2-docs/) can be properly labeled. This is the [`micro:bit` Python](https://microbit.org/get-started/user-guide/python-editor/) version of the [`micro:bit` MakeCode](https://microbit.org/get-started/user-guide/microsoft-makecode/) block:

![](obsidian/assets/obsidian/Pasted%20image%2020250903170200.png)

# Code

```python
# Imports go at the top
from microbit import *
import machine
import struct

# https://arc.net/l/quote/vbhsxtkp How to find the name of your micro:bit
def microbit_friendly_name():
    length = 5
    letters = 5
    codebook = [
        ['z', 'v', 'g', 'p', 't'],
        ['u', 'o', 'i', 'e', 'a'],
        ['z', 'v', 'g', 'p', 't'],
        ['u', 'o', 'i', 'e', 'a'],
        ['z', 'v', 'g', 'p', 't']
    ]
    name = []
    # Derive our name from the nrf51822's unique ID
    _, n = struct.unpack("II", machine.unique_id())
    ld = 1
    d = letters
    for i in range(0, length):
        h = (n % d) // ld
        n -= h
        d *= letters
        ld *= letters
        name.insert(0, codebook[i][h])
    return "".join(name)

# https://arc.net/l/quote/ygrtbswg How to find the micro:bit serial number
def get_serial_number(type=hex):
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25 
    return type(machine.mem32[NRF_FICR_BASE + (DEVICEID_INDEX*4)] & 0xFFFFFFFF)

# Code in a 'while True:' loop repeats forever
while True:
    display.scroll(microbit_friendly_name().upper())
    sleep(500)
    # display.scroll(get_serial_number()[2:])
    # sleep(500)

1234567890123456789012345678901234567890123456789012345678901234567890
```

# Links

| Link | Description |
| --- | --- |
| [[https://arc.net/l/quote/vbhsxtkp]] | How to find the name of your micro:bit |
| [[https://arc.net/l/quote/ygrtbswg]] | How to find the micro:bit serial number |
| [[https://makecode.microbit.org/99369-62072-41802-44928]] | MakeCode device-name project |
| [[https://tech.microbit.org/hardware/edgeconnector/]] | micro:bit pinouts |
| [[https://docs.python.org/3.4/]] | Python 3.4 documentation |

#microbit #embedded #Python
