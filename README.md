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


# create a column-width figure, takes 100% of the column, aspect ratio 0.75
fig, ax = create_figure(1.0, 0.75, use_textwidth=False)
```
