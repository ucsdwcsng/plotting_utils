# Simple wrapper for creating non-scaled latex figures with correct font sizes in matplotlib

Including a raw matplotlib figure in a latex document will often cause you to end up with extremely small fonts in your figures, since you typically scale the figure down in order to make it fit into a column or page width in latex. The solution to this is to generate the figure at exactly the page size you need, this preserves all of the font sizes correctly. This repo includes a file which has a wrapper to do this, plus sets `layout=constrained` to remove unnecessary whitespace in your figure, to help you meet your page count requirement.

# To use

Install:

```
pip3 install scienceplots
sudo apt-get install cm-super texlive-latex-extra texlive-fonts-recommended dvipng
```

In a python script:

```
from acm_fig import *

# if using the IEEE template, instead of ACM, call set_ieee() or manually update TEXTWIDTH and COLWIDTH
# set_ieee()

# Create a column width figure, 100% of the column wide, 30% of the column tall
fix = create_figure_wh(1.0, 0.3, use_textwidth=False)

# you can add subplots like normal
ax = fig.add_subplot()

# I have also added a function to get a nicer looking legend, but the default ax.legend() works as well.
add_legend(ax, loc='lower right')

```

In Latex: Do not use figure scaling in included subplots, instead you should generate the figure directly at the scale you want, so that font sizes are not distorted. Just directly include the figure pdf:

```
\begin{figure}[t]
\centering
    \includegraphics[]{figures/my_figure.pdf}
	\caption{My caption}
\end{figure}
```

# Range-Doppler power maps

All range-Doppler (and other range/Doppler power or amplitude) maps must follow these conventions:

1. **Range on the y axis.**
2. **Doppler on the x axis.**
3. **Positive range points up** (never invert the y axis; use `origin='lower'` with `imshow`).
4. **Use `cmap='parula'`** for all amplitude/power plots. Importing `acm_fig` registers MATLAB's parula colormap (and `parula_r`) with matplotlib, so `cmap='parula'` works in any plotting call.
5. **Always show a colorbar** for power. The only exception is a group of panels that share the same power scale (same `vmin`/`vmax`): use one shared colorbar for the group.

The `plot_range_doppler` helper handles all of this. It accepts `power` with shape `(len(range_axis), len(doppler_axis))` and sorts the axes itself, so descending or fftshift-ordered bin vectors still come out right side up:

```
from acm_fig import *

fig = create_figure(1.0, 0.75)
ax = fig.add_subplot()
im, cbar = plot_range_doppler(ax, power, range_m, doppler_mps, to_db=True)
ax.set_xlabel('Doppler (m/s)')
ax.set_ylabel('Range (m)')
```

For several panels that share one power scale, turn off the per-panel colorbars, fix `vmin`/`vmax`, and add one colorbar:

```
fig, axs = create_figure_wh(1.0, 0.4, use_textwidth=True, subplots=[(1, 3, i) for i in (1, 2, 3)])
for ax, p in zip(axs, powers):
    im, _ = plot_range_doppler(ax, p, range_m, doppler_mps, to_db=True, colorbar=False, vmin=-40, vmax=0)
fig.colorbar(im, ax=axs, label='Power (dB)')
```
