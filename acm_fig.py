import matplotlib.pyplot as plt

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
    #fig, ax = plt.subplots(figsize=(width, height))
    fig = plt.figure(figsize=(width,height))
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.12, top=0.98)
    if subplots is not None:
        axs = [fig.add_subplot(sp[0],sp[1],sp[2]) for sp in subplots]
        return fig, axs
    return fig

def add_legend(ax, loc='lower right'):
    ax.legend(loc=loc,
               frameon=True,
               facecolor='white', 
               framealpha=1.0,        # Change from 0.0 to 1.0 for opaque background
               edgecolor='black',      # Black outline
               borderpad=0.3,          # Minimal padding between text and box edge
               labelspacing=0.3,       # Minimal vertical spacing between entries
               handletextpad=0.5)      # Spacing between marker and text
