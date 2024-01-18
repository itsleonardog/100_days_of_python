# Hirst Painting

## Overview
Hirst Painting is a Python project that uses the Turtle graphics library and the colorgram library to create a digital art piece inspired by the style of Damien Hirst's famous dot paintings. The program extracts colors from an image using the colorgram library and then uses the Turtle module to create a composition of dots on a canvas.

## How to Use
To run the Hirst Painting project, follow these steps:

1. Install the required libraries:

   ```bash
   pip install colorgram-py
   ```

2. Import the colorgram library and extract colors from an image:

   ```python
   import colorgram

   rgb_colors = []
   colors = colorgram.extract('img.jpg', 30)
   for color in colors:
       r = color.rgb.r
       g = color.rgb.g
       b = color.rgb.b
       new_color = (r, g, b)
       rgb_colors.append(new_color)
   ```

3. Use the extracted colors to create a Hirst-style painting:

   ```python
   import turtle as turtle_module
   import random

   # ... (rest of the code)
   ```

## Dependencies
- [colorgram](https://pypi.org/project/colorgram-py/): A library to extract colors from images.
- [turtle](https://docs.python.org/3/library/turtle.html): A graphics library for creating simple drawings.
