import numpy as np
import matplotlib.pyplot as plt
category_names = ['RLK', 'RLP',
                  'CNL', 'TNL', 'NBS']
results = {
    'Chromosome 1': [10, 15, 17, 30, 26],
    'Chromosome 2': [26, 12, 29, 10, 13],
    'Chromosome 3': [25, 27, 7, 12, 19],
    'Chromosome 4': [22, 11, 19, 10, 23],
    'Chromosome 5': [21, 19, 5, 5, 40],
    'Chromosome 6': [8, 19, 5, 20, 28],
    'Chromosome 7': [18, 10, 24, 10, 28],
    'Chromosome 8': [11, 17, 25, 20, 22]
}
def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax
survey(results, category_names)
plt.show()
