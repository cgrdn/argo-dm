
from pathlib import Path
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='ticks', palette='colorblind')

imei_numbers = [
    '300125061656740',
    '300125061360970',
]

wmo_numbers = [
    '4902598',
    '4902599',
]

imei = imei_numbers[0]
wmo = wmo_numbers[0]

ctd = pd.read_hdf(Path(f'../data/provor/{imei}') / f'{wmo}_ctd.h5')
oxy = pd.read_hdf(Path(f'../data/provor/{imei}') / f'{wmo}_optode.h5')
eco = pd.read_hdf(Path(f'../data/provor/{imei}') / f'{wmo}_ecopuck.h5')

fig, axes = plt.subplots(2, 2, sharey=True)
deg = chr(176)
sns.scatterplot(x=f'Temperature ({deg}C)', y='Mean pressure (dbar)', hue='Profile number', data=ctd, ax=axes[0,0], palette='colorblind')
sns.scatterplot(x='Salinity (PSU)', y='Mean pressure (dbar)', hue='Profile number', data=ctd, ax=axes[0,1], palette='colorblind', legend=False)
sns.scatterplot(x=f'C1 phase ({deg})', y='Pressure (dbar)', hue='Profile number', data=oxy, ax=axes[1,0], palette='colorblind', legend=False)
sns.scatterplot(x='Channel 1 a (Count)', y='Pressure (dbar)', hue='Profile number', data=eco, ax=axes[1,1], palette='colorblind', legend=False)
axc2 = axes[1,1].twiny()
sns.scatterplot(x='Channel 2 (Count)', y='Pressure (dbar)', hue='Profile number', data=eco, ax=axc2, palette='colorblind', legend=False)

axes[0,0].legend(fontsize=8, title='Profile #', title_fontsize=10)
axes[0,0].set_title(wmo, fontweight='bold', loc='left')

axes[0,0].set_ylim((35.5, -0.5))
axes[0,1].set_xlim((26, 33))
axes[1,1].set_xlim((0, 3500))
axes[1,1].set_xticks([0, 500, 1000, 1500])
axc2.set_xlim((-2000, 2500))
axc2.set_xticks([0, 1000, 2000])
axes[0,0].set_xlabel(f'Temperature ({deg}C)')
axes[0,1].set_xlabel('Salinity')
axes[1,0].set_xlabel(f'Optode Phase ({deg})')
axes[0,0].set_ylabel('Pressure (dbar)')
axes[1,0].set_ylabel('Pressure (dbar)')
axes[1,1].set_xlabel('Channel 1 (counts)', loc='left')
axc2.set_xlabel('Channel 2 (counts)', loc='right')
fig.tight_layout()

plt.show()
