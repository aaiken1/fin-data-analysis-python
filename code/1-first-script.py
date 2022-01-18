# Not everything has to be a Jupyter notebook. This is a Python script. See the .py on the end of the file name? No code cells or Markdown here. Run your code and see the output in the terminal below.

# How to create a file like this? File:New File and select Python as your language.

# This IS NOT Markdown. These are code comments! Python will ignore these.

# How to run this file? Right-click in this editor window and look for Run Python File in Terminal. Or, click the play button in the upper-right. Or, hit select the code you want to run and hit Shift-Enter.

# Also, try right-clicking and running Current File in an Interactive Window. You can then easily save or export your work.

print(4>3)

print("Hello World")


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

# You should have a sine graph pop up!