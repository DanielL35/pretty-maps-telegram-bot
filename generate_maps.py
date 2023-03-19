import prettymaps
from matplotlib import pyplot as plt
import uuid


def generate_png(coords):
    """
    generates a map from coordinates and saves it as a file
    """

    plt = prettymaps.plot(
        (coords),
        circle = True,
        radius = 500,
        layers = {
            "green": {
                "tags": {
                    "landuse": "grass",
                    "natural": ["island", "wood"],
                    "leisure": "park"
                }
            },
            "forest": {
                "tags": {
                    "landuse": "forest"
                }
            },
            "water": {
                "tags": {
                    "natural": ["water", "bay"]
                }
            },
            "parking": {
                "tags": {
                    "amenity": "parking",
                    "highway": "pedestrian",
                    "man_made": "pier"
                }
            },
            "streets": {
                "width": {
                    "motorway": 5,
                    "trunk": 5,
                    "primary": 4.5,
                    "secondary": 4,
                    "tertiary": 3.5,
                    "residential": 3,
                }
            },
            "building": {
                "tags": {"building": True},
            },
        },
        style = {
            "background": {
                "fc": "#F2F4CB",
                "ec": "#dadbc1",
                "hatch": "ooo...",
            },
            "perimeter": {
                "fc": "#F2F4CB",
                "ec": "#dadbc1",
                "lw": 0,
                "hatch": "ooo...",
            },
            "green": {
                "fc": "#D0F1BF",
                "ec": "#2F3737",
                "lw": 1,
            },
            "forest": {
                "fc": "#64B96A",
                "ec": "#2F3737",
                "lw": 1,
            },
            "water": {
                "fc": "#a1e3ff",
                "ec": "#2F3737",
                "hatch": "ooo...",
                "hatch_c": "#85c9e6",
                "lw": 1,
            },
            "parking": {
                "fc": "#F2F4CB",
                "ec": "#2F3737",
                "lw": 1,
            },
            "streets": {
                "fc": "#2F3737",
                "ec": "#475657",
                "alpha": 1,
                "lw": 0,
            },
            "building": {
                "palette": [
                    "#FFC857",
                    "#E9724C",
                    "#C5283D"
                ],
                "ec": "#2F3737",
                "lw": 0.5,
            }
        }
    )

    filename = uuid.uuid4().hex
    plt.fig.savefig('{}.png'.format(filename))

    # empty cache
    
    
    return filename

#test_coords = (52.47643583435979, 13.43871614431018)

#test_filename = generate_png(test_coords)