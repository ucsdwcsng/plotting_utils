import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import scienceplots
plt.style.use('science')


TEXTWIDTH = 506.295 / 72.27  # 7.006 inches (full two-column width)
COLWIDTH = 241.1474 / 72.27   # 3.337 inches (single column width)

def set_acm():
    print("Using ACM template page widths")
    TEXTWIDTH = 506.295 / 72.27  # 7.006 inches (full two-column width)
    COLWIDTH = 241.1474 / 72.27   # 3.337 inches (single column width)

    
def set_ieee():
    print("Using IEEE template page widths")
    TEXTWIDTH = 506.295 / 72.27  # 7.006 inches (full two-column width)
    COLWIDTH = 241.1474 / 72.27   # 3.337 inches (single column width)

set_acm()

# Font sizes
FONT_SIZES = {
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'axes.xmargin': 0.0
}

plt.rcParams.update(FONT_SIZES)
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['axes.grid'] = True

def create_figure(width_fraction=1.0, aspect_ratio=0.75, use_textwidth=False, subplots=None):
    """Create figure at final display size"""
    base_width = TEXTWIDTH if use_textwidth else COLWIDTH
    width = base_width * width_fraction
    height = width * aspect_ratio
    fig = plt.figure(figsize=(width,height),layout='constrained')
    if subplots is not None:
        axs = [fig.add_subplot(sp[0],sp[1],sp[2]) for sp in subplots]
        return fig, axs
    return fig

def create_figure_wh(width_fraction=1.0, height_fraction=1.0, use_textwidth=False, subplots=None):
    """Create figure at final display size"""
    base_width = TEXTWIDTH if use_textwidth else COLWIDTH
    width = base_width * width_fraction
    height = base_width * height_fraction
    fig = plt.figure(figsize=(width,height),layout='constrained')
    if subplots is not None:
        axs = [fig.add_subplot(sp[0],sp[1],sp[2]) for sp in subplots]
        return fig, axs
    return fig


def add_legend(ax, loc='lower right', in_layout=True):
    leg = ax.legend(loc=loc,
               frameon=True,
               facecolor='white', 
               framealpha=1.0,
               edgecolor='black',
               borderpad=0.3,
               labelspacing=0.3,
               handletextpad=0.5)
    leg.set_in_layout(in_layout)
    return leg


# MATLAB parula colormap. The 48 anchor colors are linearly interpolated to 256
# levels and registered with matplotlib, so cmap='parula' works everywhere.
_PARULA_DATA = [
    [0.2422, 0.1504, 0.6603], [0.2444, 0.1793, 0.7107], [0.2464, 0.2089, 0.7615],
    [0.2482, 0.2391, 0.8108], [0.2492, 0.2701, 0.8565], [0.2486, 0.3017, 0.8944],
    [0.2440, 0.3341, 0.9214], [0.2336, 0.3678, 0.9398], [0.2158, 0.4019, 0.9511],
    [0.1896, 0.4361, 0.9563], [0.1553, 0.4702, 0.9565], [0.1140, 0.5041, 0.9519],
    [0.0706, 0.5376, 0.9428], [0.0330, 0.5704, 0.9295], [0.0087, 0.6022, 0.9122],
    [0.0026, 0.6329, 0.8914], [0.0124, 0.6623, 0.8677], [0.0345, 0.6903, 0.8422],
    [0.0664, 0.7168, 0.8159], [0.1054, 0.7417, 0.7896], [0.1492, 0.7650, 0.7636],
    [0.1956, 0.7869, 0.7379], [0.2430, 0.8073, 0.7126], [0.2905, 0.8263, 0.6877],
    [0.3373, 0.8441, 0.6632], [0.3831, 0.8608, 0.6391], [0.4279, 0.8765, 0.6152],
    [0.4719, 0.8913, 0.5913], [0.5152, 0.9054, 0.5674], [0.5581, 0.9186, 0.5433],
    [0.6009, 0.9310, 0.5188], [0.6438, 0.9427, 0.4938], [0.6871, 0.9535, 0.4680],
    [0.7310, 0.9633, 0.4411], [0.7758, 0.9719, 0.4128], [0.8217, 0.9791, 0.3826],
    [0.8687, 0.9847, 0.3499], [0.9168, 0.9882, 0.3140], [0.9649, 0.9892, 0.2743],
    [0.9934, 0.9904, 0.2267], [0.9961, 0.9846, 0.1697], [0.9863, 0.9774, 0.1176],
    [0.9715, 0.9723, 0.0759], [0.9547, 0.9702, 0.0472], [0.9378, 0.9713, 0.0279],
    [0.9219, 0.9749, 0.0150], [0.9077, 0.9800, 0.0072], [0.8961, 0.9856, 0.0036]
]

PARULA = LinearSegmentedColormap.from_list('parula', _PARULA_DATA, N=256)
if 'parula' not in matplotlib.colormaps:
    matplotlib.colormaps.register(PARULA)
    matplotlib.colormaps.register(PARULA.reversed())  # 'parula_r'


def plot_range_doppler(ax, power, range_axis, doppler_axis, to_db=False,
                       colorbar=True, cbar_label=None, cmap='parula', **kwargs):
    """Plot a range-Doppler power map following the repo conventions.

    Range is on the y axis (positive range up), Doppler on the x axis, the
    parula colormap is used, and a colorbar is added by default.

    power: 2D array of shape (len(range_axis), len(doppler_axis)).
    range_axis, doppler_axis: 1D, evenly spaced bin centers (either order).
    to_db: if True, plot 10*log10(|power|) instead of power.
    colorbar: set False for panels sharing one power scale, then add a single
        shared colorbar with fig.colorbar(im, ax=axs).
    kwargs: passed to ax.imshow (e.g. vmin, vmax).

    Returns (im, cbar); cbar is None when colorbar=False.
    """
    power = np.asarray(power)
    range_axis = np.asarray(range_axis)
    doppler_axis = np.asarray(doppler_axis)
    if power.shape != (len(range_axis), len(doppler_axis)):
        raise ValueError(f"power has shape {power.shape}, expected "
                         f"(len(range_axis), len(doppler_axis)) = "
                         f"({len(range_axis)}, {len(doppler_axis)})")

    # Sort both axes ascending so origin='lower' always puts positive range up
    # and positive Doppler right, regardless of how the input was ordered.
    r_idx = np.argsort(range_axis)
    d_idx = np.argsort(doppler_axis)
    range_axis, doppler_axis = range_axis[r_idx], doppler_axis[d_idx]
    power = power[np.ix_(r_idx, d_idx)]

    if to_db:
        power = 10 * np.log10(np.abs(power) + np.finfo(float).tiny)

    # Extent covers the full bins, so each pixel is centered on its bin value
    dr = (range_axis[-1] - range_axis[0]) / max(len(range_axis) - 1, 1)
    dd = (doppler_axis[-1] - doppler_axis[0]) / max(len(doppler_axis) - 1, 1)
    extent = (doppler_axis[0] - dd / 2, doppler_axis[-1] + dd / 2,
              range_axis[0] - dr / 2, range_axis[-1] + dr / 2)

    kwargs.setdefault('interpolation', 'nearest')
    im = ax.imshow(power, origin='lower', extent=extent, aspect='auto',
                   cmap=cmap, **kwargs)
    ax.grid(False)
    ax.set_xlabel('Doppler')
    ax.set_ylabel('Range')

    cbar = None
    if colorbar:
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.set_label(cbar_label or ('Power (dB)' if to_db else 'Power'))
    return im, cbar
