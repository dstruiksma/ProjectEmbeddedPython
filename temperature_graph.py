import datetime as dt
import matplotlib.pyplot as plt
import random
import Connection

"""
Temperatuur per 60 seconden
"""

fig = plt.figure(1, figsize=(7, 6), dpi=100)
ax = fig.add_subplot(111)
xs = []
ys = []

def animate(i, xs, ys):

    # TODO Hier moet de temperatuur gelezen worden
    temp_c = random.randint(10, 30)

    # Tijd toevoegen aan x-as
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))

    result = 0
    if (Connection.temperature_list.keys().__contains__('1')):
        temp = Connection.temperature_list['1']
        result = temp[-1]

    # Temperatuur toevoegen aan y-as
    ys.append(result)

    # Niet meer dan 20 waarden tegelijk in beeld
    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.plot(xs, ys)

    ax.set_xticklabels(xs, rotation=45, ha='right')
    fig.subplots_adjust(bottom=0.30)
    ax.set_ylabel('Temperatuur (°C)')
