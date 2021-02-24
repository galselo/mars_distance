import numpy as np
import great_circle_calculator.great_circle_calculator as gcc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.font_manager import FontProperties

plt.rcParams["font.family"] = "Bebas Neue"
plt.rcParams.update({'font.size': 20})

# lon, lat
data = {"Pathfinder": (-33.1312, 19.748),
        "Opportunity": (354.473-360., -1.946),
        "Spirit": (175.472, -14.569),
        "Curiosity": (137.407, -4.733),
        "Perseverance": (77.5, 18.4),
        "Viking 1": (-48.041, 22.487),
        "Viking 2": (360.-225.71, 47.64)}


rome = (12.496366, 41.902782)

plt.figure(figsize=(13, 8))

m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180)
m.shadedrelief()
#m.etopo(scale=0.5, alpha=0.5)

afont = FontProperties(fname="fa-solid-900.ttf")

for k, p2 in data.items():
    p1 = data["Perseverance"]

    be = gcc.bearing_at_p1(p1, p2)
    d_m = gcc.distance_between_points(p1, p2) / 6371000. * 3396200.

    c = gcc.point_given_start_and_bearing(rome, be, d_m)
    d_e2 = gcc.distance_between_points(rome, c)
    print(k, d_m / 1e3)

    x, y = m(c[0], c[1])
    plt.text(x, y, '\uf3c5', fontproperties=afont, va="baseline", ha="center", fontsize=20)
    plt.text(x+2, y+3, k, fontsize=26)

plt.xlim(-81, 105)
plt.ylim(-30, 80)
plt.tight_layout()
plt.show()

