import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage
from urllib import request
from PIL import Image
import numpy as np

def copilot_proportion():
    total_developers = 100
    copilot_users = 20

    proportion = copilot_users / total_developers

    fig, ax = plt.subplots()

    copilot_icon = Image.open(request.urlopen("https://github.githubassets.com/images/icons/copilot/cp-head-square.png"))
    copilot_icon = np.array(copilot_icon)
    copilot_icon = OffsetImage(copilot_icon, zoom=0.1)

    not_copilot_icon = Image.open(request.urlopen("https://cdn-icons-png.flaticon.com/512/6515/6515181.png"))
    not_copilot_icon = np.array(not_copilot_icon)
    not_copilot_icon = OffsetImage(not_copilot_icon, zoom=0.1)

    copilot_developers = proportion * total_developers
    not_copilot_developers = total_developers - copilot_developers

    for i in range(int(copilot_developers)):
        ax.add_artist(offsetbox.AnnotationBbox(copilot_icon, [i, 0], frameon=False))

    for i in range(int(not_copilot_developers)):
        ax.add_artist(offsetbox.AnnotationBbox(copilot_icon, [i, 0], frameon=False))

    ax.set_xlim(-1, total_developers + 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    plt.show()

copilot_proportion()
