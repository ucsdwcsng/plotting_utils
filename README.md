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

# I have also added a function for 
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
