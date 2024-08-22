# Colors

[Web colors](https://en.wikipedia.org/wiki/Web_colors) can be specified in Cascading Style Sheets ([CSS](https://en.wikipedia.org/wiki/CSS)) in a variety of ways. Including using [CSS color names](https://www.w3.org/TR/css-color-4/#named-colors) or 3- or 6-digit [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) (base 16) values (or 4- or 8-digit hex values when including the optional alpha / opacity argument of RGBA). Later versions of the CSS standard include [CSS Color 4](https://en.wikipedia.org/wiki/Web_colors#CSS_Color_4) and [CSS Color 5](https://en.wikipedia.org/wiki/Web_colors#CSS_Color_5) with several enhancements.

Because I'm slightly color blind, I typically use colors from the 216 [web-safe colors](https://websafecolors.info/) on my websites. ([ColorHexa](https://www.colorhexa.com/663399) has an interesting *Color Blindness Simulator* as part of their color pages to help with [web accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/).) See [this reference](https://dev.to/alvaromontoro/the-ultimate-guide-to-css-colors-2020-edition-1bh1) for a complete description of CSS colors.

## Named colors

CSS Colors can be specified as one of the case-insensitive [CSS color names](https://www.w3.org/TR/css-color-4/#named-colors). There are 148 named colors that come from 16 original VGA colors, 131 of the 504 [X11 colors](https://www.w3schools.com/colors/colors_x11.asp), and [`rebeccapurple`](https://medium.com/@valgaze/the-hidden-purple-memorial-in-your-web-browser-7d84813bb416). ([https://youtu.be/HmStJQzclHc](https://youtu.be/HmStJQzclHc) is a history of the names &mdash; who knew there was a [Crayola 72 pack](https://crayola.fandom.com/wiki/72-count_box_(1973))?)

## Hexadecimal colors

CSS Colors can be specified as a hexadecimal number preceded by a hash character (`#`). The standard way to specify a color in an RGB color space is to use three two-digit hexadecimal numbers, one for each color. That yields 256 levels (from `00` to `ff`) of red, green, and blue. The color numbers can be specified as either 3 or 6 hexadecimal digits, where the 3-digit number simply repeats each digit twice. For example, [`rebeccapurple`](https://www.color-hex.com/color/663399) can be specified as either `#639` or `#663399`.