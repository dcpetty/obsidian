---
title: "NeoPixel example"
date: 2024-10-31 21:16:42
last_modified_at: 2024-10-31 21:54:09
show_date: true
permalink: /microbit/neopixelexample/
tags:
- Python
- embedded
- microbit
toc: true
toc_sticky: true
---
This documents [Python](https://www.python.org/community/microbit/) example code for the [50mm 12 NeoPixel (WS2812B) Ring](https://universal-solder.ca/12-led-ring-ws2812b-rgb-addressable-50mm/) connected to a BBC [`micro:bit`](https://microbit-micropython.readthedocs.io/en/v2-docs/) through the [`micro:bit` Python Editor](https://microbit.org/get-started/user-guide/python-editor/).

# Assumptions

- XXX
- The connector has 4 solder-pad connections, *32mmx32mm with 2.0mm diameter.* The pins are:

| Pin | Signal | I/O | Notes |
| :---: | :---: | :---: | --- |
| 1 | `DI` | I | DI ??? |
| 2 | `5V` | +V | +5-7V |
| 5 | `GND` | &#x23da; | 0V |
| 4 | `DO` | DO | DO ??? |

# Code

```python
# Imports go at the top
from microbit import *
import math, neopixel, random

np = neopixel.NeoPixel(pin0, 12)
n, delay, maximum = 12, 200, 30

# https://stackoverflow.com/a/2450976/17467335
# The de-facto unbiased shuffle algorithm is the Fisher-Yates
# (aka Knuth) Shuffle.
# See https://github.com/coolaj86/knuth-shuffle.
def shuffle(array):
    """Return array shuffled in place with the unbiased Fisher-Yates
    (aka Knuth) algorithm."""
    current_index = len(array)

    # While there remain elements to shuffle...
    while 0 != current_index:

        # Pick a remaining element...
        random_index = int(random.random() * current_index)
        current_index -= 1

        # And swap it with the current element.
        array[current_index], array[random_index] = \
            array[random_index], array[current_index]

    return array

def compress(x, scale=1):
    """Return x on [0, 1) exponentially compressed, scaled to scale,
    and floored."""
    # https://www.desmos.com/calculator/gdcw7rndv2
    # The compression factor of 4 is good. It must be greater than e
    # for color[j] > 0.
    return int(math.exp(4 * (x - 1)) * scale)

def random_lights(n=12, maximum=30):
    """Return n random leds with maximum brightness (< 256)."""
    leds, color = [tuple(), ] * n, [0, ] * 3
    for i in range(len(leds)):
        for j in range(len(color)):
            color[j] = compress(random.random(), maximum)
        leds[i] = tuple(color)
    return leds

def chase_lights(rot, color=(102, 51, 153, ), n=12, maximum=30):
    """Return n leds of color divided over n steps scaled by maximum
    rotated by rot."""
    leds = [tuple(), ] * n
    for i in range(len(leds)):
        scaled = [ compress(c / 255 * i / n, maximum) for c in color ]
        leds[i] = tuple(scaled)
    # Rotate by rot.
    return leds[rot: ] + leds[: rot]

# Code in a 'while True:' loop repeats forever
while True:

    # Set random leds and shuffle every delay ms until button_a pressed.
    leds = random_lights(n, maximum)
    while not button_a.was_pressed():
        leds = shuffle(leds)
        for j in range(len(leds)):
            np[j] = leds[j]
        np.show()
        sleep(delay)

    # Set chasing leds every delay ms until button_a pressed.
    chase = 0
    while not button_a.was_pressed():
        leds = chase_lights(chase, (0, 255, 0, ))   # chase green leds
        for j in range(len(leds)):
            np[j] = leds[j]
        np.show()
        sleep(delay)
        chase = (chase + 1) % 12

1234567890123456789012345678901234567890123456789012345678901234567890
```

# Links

| Link | Description |
| --- | --- |
| [https://www.desmos.com/&#8203;calculator/&#8203;gdcw7rndv2](https://www.desmos.com/calculator/gdcw7rndv2) | [Desmos](https://www.desmos.com/) exponential compression graph |
| [https://universal-solder.ca/&#8203;12-led-ring-ws2812b-rgb-addressable-50mm/&#8203;)](https://universal-solder.ca/12-led-ring-ws2812b-rgb-addressable-50mm/)) | 50mm 12 NeoPixel (WS2812B) Ring available from [Universal Solder](https://universal-solder.ca/) |
| [https://tech.microbit.org/&#8203;hardware/&#8203;edgeconnector/&#8203;](https://tech.microbit.org/hardware/edgeconnector/) | micro:bit pinouts |
| [https://microbit-micropython.readthedocs.io/&#8203;en/&#8203;v2-docs/&#8203;neopixel.html](https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html) | micro:bit NeoPixel |
| [https://docs.python.org/&#8203;3.4/&#8203;](https://docs.python.org/3.4/) | Python 3.4 documentation |

#microbit #embedded #Python